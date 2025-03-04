package elements;

import utils.Drawing;
import java.awt.Graphics;

public class imagemPonto extends Element {
    private long startTime=0;
    // Construtor da imagem que da ponto
    public imagemPonto(String imageName) {
        super(imageName);
        this.isTransposable = true;
    }
    // Desenha a imagem do Element imagemPonto
    public void autoDraw(Graphics g) {
        Drawing.draw(g, this.imageIcon, pos.getY(), pos.getX());
    }        

    // Retorna o valor da variável startTime 
    public long getStartTime() {
		return this.startTime;
	}
	// Redefine o valor da variável startTime 
	public void setStartTime(long start){
		this.startTime=start;
	}
}
