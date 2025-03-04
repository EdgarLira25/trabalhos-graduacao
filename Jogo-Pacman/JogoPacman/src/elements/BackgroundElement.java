package elements;

import utils.Consts;
import utils.Drawing;
import java.awt.Graphics;

public abstract class BackgroundElement extends Element{
    //construtor do Background
    public BackgroundElement(String imageName) {
        super(imageName);
    }
    //Método abstract para desenhar o Element
    public abstract void autoDraw(Graphics g);
}
