package control;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.Action;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;

import utils.Consts;

public class InitialScreen extends javax.swing.JFrame {
	private static final long serialVersionUID = 1L;

	private final String nomeImagemInicial = "inicialimagem.png";

	// Construtor da classe InitialScreen
	public InitialScreen() {

		menu();
	}

	// configuração do Menu
	private void menu() {

		int sizeWidth = Consts.NUM_CELLS * Consts.CELL_SIZE + getInsets().left + getInsets().right;
		int sizeHeight = Consts.NUM_CELLS * Consts.CELL_SIZE + getInsets().top + getInsets().bottom;

		setSize(sizeWidth, sizeHeight);

		setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
		setTitle("SCC0604 - Pacman");
		setCursor(new java.awt.Cursor(java.awt.Cursor.DEFAULT_CURSOR));
		setLocation(new java.awt.Point(20, 20));
		setResizable(false);

		try {

			setContentPane(
					new JLabel(new ImageIcon(new File(".").getCanonicalPath() + Consts.PATH + nomeImagemInicial)));
		} catch (IOException ex) {
			System.out.println(ex.getMessage());
		}

		JMenuBar mb = new JMenuBar();

		JMenu inicia = new JMenu("Inicia:");

		JMenuItem iniciaItem = new JMenuItem("Iniciar");
		inicia.add(iniciaItem);

		JMenu open = new JMenu("Open");
		JMenuItem openItem = new JMenuItem("Abrir Save");
		open.add(openItem);

		JMenu sair = new JMenu("Exit");

		JMenuItem sairItem = new JMenuItem("Exit");

		JMenuItem level1 = new JMenuItem("Level 1");

		JMenuItem level2 = new JMenuItem("Level 2");

		JMenuItem level3 = new JMenuItem("Level 3");

		JMenuItem level4 = new JMenuItem("Level 4");

		JMenu levels = new JMenu("Levels");

		level1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent ev) {

				Main.level = 1;
				System.out.println("level 1");

			}
		});

		level2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent ev) {

				Main.level = 2;
				System.out.println("level 2");

			}
		});

		level3.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent ev) {

				Main.level = 3;
				System.out.println("level 3");

			}
		});

		level4.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent ev) {

				Main.level = 4;
				System.out.println("level 4");

			}
		});

		iniciaItem.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent ev) {
				Main.initialScreen.setVisible(false);
				Main.initialScreen.dispose();
				Main.startGame();
			}
		});

		sairItem.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent ev) {
				System.exit(0);
			}
		});

		openItem.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent ev) {
				Main.initialScreen.setVisible(false);
				Main.initialScreen.dispose();
				Main.openSavedGame = true;
				Main.startGame();
			}

		});

		sair.add(sairItem);
		levels.add(level1);
		levels.add(level2);
		levels.add(level3);
		levels.add(level4);
		mb.add(inicia);
		mb.add(levels);
		mb.add(open);
		mb.add(sair);
		setJMenuBar(mb);

	}

	// Método para startar um game ao clicar no menu iniciar
	public class HandlerStartButton implements ActionListener {
		public void actionPerformed(ActionEvent ev) {
			Main.initialScreen.setVisible(false);
			Main.initialScreen.dispose();
			Main.startGame();
		}
	}

	// Método para abrir um jogo salvo
	public class HandlerOpenButton implements ActionListener {
		public void actionPerformed(ActionEvent ev) {
			Main.initialScreen.setVisible(false);
			Main.initialScreen.dispose();
			Main.openSavedGame = true;
			Main.startGame();
		}
	}
}