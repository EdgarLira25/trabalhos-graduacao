package elements;

import utils.Consts;
import utils.Drawing;
import utils.Position;

import java.awt.Graphics;
import java.io.Serializable;
import java.util.Random;

public class Clyde extends Ghost {

	// Construtor do fantasma Clyde
	public Clyde(String imageName) {
		super(imageName);
	}

	// Define a direção que o fantasma Clyde vai se movimentar e também desenha o
	// fantasma
	@Override
	public void autoDraw(Graphics g) {
		Pacman pacman = Drawing.getGameScreen().getPacman();
		Position posPacman = pacman.getPos();
		double distancia = posPacman.distance(this.pos);

		if (distancia < Consts.DISTANCEGHOST) {
			moveRandom();
		} else {
			if (!this.isMortal) {
				followPacman();
			} else {
				escapePacman();
			}
		}

		Drawing.draw(g, this.imageIcon, pos.getY(), pos.getX());

	}

}
