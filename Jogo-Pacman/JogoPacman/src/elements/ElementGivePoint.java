package elements;

import utils.Drawing;
import java.awt.Graphics;
import java.io.Serializable;

public class ElementGivePoint extends Element{
    protected  int numberPoints=0;
    
    //Retorna o numero de pontos que o Element tem
	public int getNumberPoints(){
		return numberPoints;
	}

    //Contrutor do ElementGivePoint
    public ElementGivePoint(String imageName) {
        super(imageName);
        this.isMortal = true;        
    }

    //Desenha o ElementGivePoint
    @Override
    public void autoDraw(Graphics g) {
        Drawing.draw(g, this.imageIcon, pos.getY(), pos.getX());
    }
    
}
