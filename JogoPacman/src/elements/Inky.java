package elements;

import utils.Consts;
import utils.Drawing;
import utils.Position;
import java.awt.Graphics;
import java.io.Serializable;
import java.util.Random;

public class Inky extends Ghost {
	// Construtor do fantasma Inky
	public Inky(String imageName) {
		super(imageName);
	}
	// Método que desenha o Fantasma Inky e define sua movimentação
	@Override
	public void autoDraw(Graphics g) {
		
		 Blinky blinky = Drawing.getGameScreen().getBlinky();
		 Position posBlinky=blinky.getPos();
		 double distancia=posBlinky.distance(this.pos);
		
		if (distancia > Consts.DISTANCEGHOST) {

		moveRandom();
		
	}

		else {
			if (!this.isMortal) {
				followPacman();
			} else {
				escapePacman();
			}
		}


		Drawing.draw(g, this.imageIcon, pos.getY(), pos.getX());

	}
}
