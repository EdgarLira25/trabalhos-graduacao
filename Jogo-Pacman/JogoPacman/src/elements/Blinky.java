package elements;

import utils.Drawing;
import utils.Position;
import utils.Consts;
import java.awt.Graphics;
import java.io.Serializable;
import java.util.Random;

public class Blinky extends Ghost {

	// construtor do fantasma Blinky
	public Blinky(String imageName) {
		super(imageName);
	}

	// Define a direção que o fantasma Blinky vai se movimentar e também desenha o fantasma
	@Override
	public void autoDraw(Graphics g) {

		if (!this.isMortal) {
			followPacman();
		} else {
			escapePacman();
		}

		Drawing.draw(g, this.imageIcon, pos.getY(), pos.getX());
	}
}
