package elements;

import utils.Drawing;
import java.awt.Graphics;
import java.io.Serializable;
/*
 * 
 * Elemento criado qe foi pedido no EP 
 * 
 */
public class NewElement extends Element {
    protected  int takeLife=0;

    // retorna o valor da variavel TakeLife
	public int getTakeLife(){
		return takeLife;
	}
    
    // construtor do elemento
    public NewElement (String imageName) {
        super(imageName);
        this.isMortal = true;        
    }

    // Desenha o elemento
    @Override
    public void autoDraw(Graphics g) {
        Drawing.draw(g, this.imageIcon, pos.getY(), pos.getX());
    }
    
}