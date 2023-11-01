package utils;

import control.GameScreen;
import java.awt.Graphics;

import javax.swing.ImageIcon;

public class Drawing{
    static GameScreen screen;

    //Retorna a screen do GameScreen
    public static GameScreen getGameScreen() {
        return screen;
    }
    //Muda a GameScreen para uma nova
    public static void setGameScreen(GameScreen newScreen) {
        screen = newScreen;
    }    
    // Desenha o Element na tela
    public static void draw(Graphics g, ImageIcon imageIcon, double y, double x) {
        //System.out.println("y="+(y * Consts.CELL_SIZE)+", x="+(x * Consts.CELL_SIZE));
        imageIcon.paintIcon(screen, g, (int)Math.round(y * Consts.CELL_SIZE),(int)Math.round(x * Consts.CELL_SIZE));
    }
}
