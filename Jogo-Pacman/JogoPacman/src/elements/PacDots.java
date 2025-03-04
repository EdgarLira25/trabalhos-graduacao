package elements;

import utils.Drawing;
import java.awt.Graphics;
import java.io.Serializable;


public class PacDots extends ElementGivePoint{
    
		// Construtor dos PacDots e também define o valor deles
    public PacDots(String imageName) {
        super(imageName);
        this.numberPoints = 10;
    }  
    
}
