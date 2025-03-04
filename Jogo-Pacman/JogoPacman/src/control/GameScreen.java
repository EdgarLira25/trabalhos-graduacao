package control;

import utils.*;
import elements.Blinky;

import elements.Cherry;
import elements.Clyde;
import elements.Inky;
import elements.PacDots;
import elements.Pinky;
import elements.PowerPellet;
import elements.Strawberry;
import elements.Pacman;
import elements.Element;
import elements.Wall;
import utils.Consts;
import utils.Drawing;
import utils.Stage;
import java.io.Serializable;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.Toolkit;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.io.Console;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.OutputStream;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Timer;
import java.util.TimerTask;
import java.util.logging.Level;
import java.util.logging.Logger;

import org.junit.ClassRule;

public class GameScreen extends javax.swing.JFrame implements KeyListener {
    private Blinky blinky;
    private Pacman pacman;
    private ArrayList<Element> elemArray;
    private final GameController controller = new GameController();
    private Stage stage;
    int cont = 0;
    String fileName = "jogo.ser";

    // Construtor do GameScreen

    public GameScreen() {
        Main.time = System.currentTimeMillis();
        Drawing.setGameScreen(this);
        initComponents();

        this.addKeyListener(this);

        this.setSize(Consts.NUM_CELLS * Consts.CELL_SIZE + getInsets().left + getInsets().right,
                Consts.NUM_CELLS * Consts.CELL_SIZE + getInsets().top + getInsets().bottom);
        elemArray = new ArrayList<Element>();
        pacman = null;

        if (Main.openSavedGame) {
            try {

                openSavedGame(fileName);

            } catch (FileNotFoundException e1) {
                System.err.println("Arquivo jogo.ser não existente. Iniciando novo jogo ...");
                this.stage = new Stage(Main.level);
                fillInitialElemArrayFromMatrix(stage.getMatrix());
            } catch (IOException e1) {
                e1.printStackTrace();
            } catch (ClassNotFoundException e1) {
                e1.printStackTrace();
            }

        } else {
            this.stage = new Stage(Main.level);
            fillInitialElemArrayFromMatrix(stage.getMatrix());

        }
    }

    // returna um blinky

    public Blinky getBlinky() {
        return blinky;
    }

    // Retorna um pacman

    public Pacman getPacman() {
        return pacman;
    }

    // Prenche o elemArray com os Elements necessários para ser lido e o jogo
    // iniciar
    private void fillInitialElemArrayFromMatrix(int[][] matrix) {

        pacman = new Pacman("pacman.png");
        pacman.setPosition(1, 1);
        this.addElement(pacman);

        blinky = new Blinky("blinky.png");
        blinky.setPosition(10, 8);
        this.addElement(blinky);

        Pinky pinky = new Pinky("pinky.png");
        pinky.setPosition(10, 9);
        this.addElement(pinky);

        Inky inky = new Inky("inky.png");
        inky.setPosition(10, 10);
        this.addElement(inky);

        Clyde clyde = new Clyde("clyde.png");
        clyde.setPosition(8, 9);
        this.addElement(clyde);

        for (int i = 0; i < Consts.NUM_CELLS; i = i + 1) {
            for (int j = 0; j < Consts.NUM_CELLS; j = j + 1) {
                switch (matrix[i][j]) {

                    case 1:

                        Wall wall1 = new Wall("bricks6.png");
                        wall1.setPosition(i, j);
                        this.addElement(wall1);
                        break;

                    case 0:

                        PacDots pacDot = new PacDots("pac-dot.png");
                        pacDot.setPosition(i, j);
                        this.addElement(pacDot);
                        pacman.addNumberDotstoEat();
                        break;

                    case 6:

                        PowerPellet power = new PowerPellet("power_Pellet.png");
                        power.setPosition(i, j);
                        this.addElement(power);
                        break;

                    case 7:

                        Wall wall2 = new Wall("parede5.jpg");
                        wall2.setPosition(i, j);
                        this.addElement(wall2);

                        break;

                    default:
                        break;
                }
            }
        }
    }

    // Adiciona Element no elemArray
    public final void addElement(Element elem) {
        elemArray.add(elem);
    }

    // Remove um Element do elemArray
    public void removeElement(Element elem) {
        elemArray.remove(elem);
    }

    // inicia uma nova fase
    public void reStartGame(int numberLifes) {

        int salvarScore = pacman.getScore();
        int salvarRemainingScore = pacman.getRemainingScore();

        elemArray.clear();
        elemArray = new ArrayList<Element>();
        pacman = null;

        this.stage = new Stage(Main.level);
        fillInitialElemArrayFromMatrix(stage.getMatrix());

        ((Pacman) elemArray.get(0)).setNumberLifes(numberLifes);
        ((Pacman) elemArray.get(0)).setScore(salvarScore);
        ((Pacman) elemArray.get(0)).setRemainingScore(salvarRemainingScore);

    }

    // Desenha os elementos na tela
    @Override
    public void paint(Graphics gOld) {
        Graphics g = getBufferStrategy().getDrawGraphics();

        Graphics g2 = g.create(getInsets().right, getInsets().top, getWidth() - getInsets().left,
                getHeight() - getInsets().bottom);

        for (int i = 0; i < Consts.NUM_CELLS; i = i + 1) {
            for (int j = 0; j < Consts.NUM_CELLS; j = j + 1) {
                try {
                    Image newImage = Toolkit.getDefaultToolkit()
                            .getImage(new java.io.File(".").getCanonicalPath() + Consts.PATH + stage.getBackground());
                    g2.drawImage(newImage,
                            j * Consts.CELL_SIZE, i * Consts.CELL_SIZE, Consts.CELL_SIZE, Consts.CELL_SIZE, null);

                } catch (IOException ex) {
                    Logger.getLogger(GameScreen.class.getName()).log(Level.SEVERE, null, ex);
                }
            }
        }

        cont++;
        this.controller.drawAllElements(elemArray, g2);
        this.controller.processAllElements(elemArray, stage.getMatrix(), cont);
        this.setTitle(pacman.getStringPosition() + " Score:" + pacman.getScore() + " Lifes:" + pacman.getLifes()
                + " Level:" + Main.level + " NumberDots:" + pacman.getNumberDotstoEat() + " NumberGhosts:"
                + pacman.getNumberGhosttoEat());

        g.dispose();
        g2.dispose();
        if (!getBufferStrategy().contentsLost()) {
            getBufferStrategy().show();
        }
    }

    public void go() {
        TimerTask task = new TimerTask() {

            public void run() {
                repaint();
            }
        };
        Timer timer = new Timer();
        timer.schedule(task, 0, Consts.DELAY);
    }

    // Verifica os botões pressionados no teclado e se estão listados faz alguma
    // ação
    public void keyPressed(KeyEvent e) {
        if (e.getKeyCode() == KeyEvent.VK_UP) {
            pacman.setMovDirection(Pacman.MOVE_UP);
        } else if (e.getKeyCode() == KeyEvent.VK_DOWN) {
            pacman.setMovDirection(Pacman.MOVE_DOWN);
        } else if (e.getKeyCode() == KeyEvent.VK_LEFT) {
            pacman.setMovDirection(Pacman.MOVE_LEFT);
        } else if (e.getKeyCode() == KeyEvent.VK_RIGHT) {
            pacman.setMovDirection(Pacman.MOVE_RIGHT);
        } else if (e.getKeyCode() == KeyEvent.VK_SPACE) {
            pacman.setMovDirection(Pacman.STOP);
        } else if (e.isControlDown() && e.getKeyCode() == KeyEvent.VK_S) {

            saveElemArrayandStage();

        }
    }

    // Salva o elemArray e o Stage
    private void saveElemArrayandStage() {

        try {

            FileOutputStream fluxo = new FileOutputStream(fileName);

            ObjectOutputStream faseSalva = new ObjectOutputStream(fluxo);

            faseSalva.writeObject(stage);

            faseSalva.writeObject(elemArray);

            faseSalva.close();

        } catch (IOException ioExc) {

            System.out.println(ioExc.getMessage());
            ioExc.printStackTrace();

        }

    }

    // Abre o save do jogo
    private void openSavedGame(String fileName) throws FileNotFoundException, IOException, ClassNotFoundException {

        FileInputStream fluxo = new FileInputStream(fileName);

        ObjectInputStream faseSalva = new ObjectInputStream(fluxo);

        stage = (Stage) faseSalva.readObject();

        elemArray = (ArrayList<Element>) faseSalva.readObject();

        faseSalva.close();

        pacman = (Pacman) elemArray.get(0);
        
        blinky = (Blinky) elemArray.get(1);
        
        
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */

    // inicia os componentes do jogo

    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated
    // Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Pacman");
        setCursor(new java.awt.Cursor(java.awt.Cursor.DEFAULT_CURSOR));
        setLocation(new java.awt.Point(20, 20));
        setResizable(false);

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
                layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                        .addGap(0, 500, Short.MAX_VALUE));
        layout.setVerticalGroup(
                layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                        .addGap(0, 500, Short.MAX_VALUE));

        pack();
    }
    // </editor-fold>//GEN-END:initComponents
    // Variables declaration - do not modify//GEN-BEGIN:variables
    // End of variables declaration//GEN-END:variables

    public void keyTyped(KeyEvent e) {
        // TODO Auto-generated method stub

    }

    public void keyReleased(KeyEvent e) {
        // TODO Auto-generated method stub

    }

    public void dispose() {
        super.dispose();
    }
}
