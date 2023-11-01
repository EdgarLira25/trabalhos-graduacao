package elements;

import utils.Consts;
import utils.Position;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.io.Serializable;
import javax.swing.ImageIcon;
public abstract class Element implements Serializable{

    protected ImageIcon imageIcon;
    protected Position pos;
    protected boolean isTransposable; 
    protected boolean isMortal;       
    // Construtor do Element
    protected Element(String imageName) {
        this.pos = new Position(1, 1);
        this.isTransposable = true;
        this.isMortal = false;
        
        try {
            imageIcon = new ImageIcon(new java.io.File(".").getCanonicalPath() + Consts.PATH + imageName);
            Image img = imageIcon.getImage();
            BufferedImage bi = new BufferedImage(Consts.CELL_SIZE, Consts.CELL_SIZE, BufferedImage.TYPE_INT_ARGB);
            Graphics g = bi.createGraphics();
            g.drawImage(img, 0, 0, Consts.CELL_SIZE, Consts.CELL_SIZE, null);
            imageIcon = new ImageIcon(bi);
            
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }
    }
    // Verifica colisão entre Elements
    public boolean overlap(Element elem) {
        double xDist = Math.abs(elem.pos.getX() - this.pos.getX());
        double yDist = Math.abs(elem.pos.getY() - this.pos.getY());
        
        if (xDist < 1.0 && yDist < 1.0)
            return true;
        else
            return false;
    }

    // Retorna uma String dizendo a posição do Element
    public String getStringPosition() {
        return ("(" + pos.getX() + ", " + pos.getY() + ")");
    }

    // Retorna a posição do Element
    public Position getPos(){
    	return pos;
    }
    // Define a posição do Element se retorna true
    public boolean setPosition(double x, double y) {
        return pos.setPosition(x, y);
    }
    // Retorna true ou false para a variavel isTransposable
    public boolean isTransposable() {
        return isTransposable;
    }
    // Retorna true ou false para a variavel isMortal
    public boolean isMortal() {
        return isMortal;
    }
    //Método que define como true ou false a variavel isTransposable
    public void setTransposable(boolean isTransposable) {
        this.isTransposable = isTransposable;
    }
    //Método abstrato para desenhar o Element
    abstract public void autoDraw(Graphics g);

 
}
