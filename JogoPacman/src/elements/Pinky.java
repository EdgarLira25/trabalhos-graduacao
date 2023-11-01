package elements;

import utils.Drawing;
import utils.Position;
import utils.Consts;
import java.awt.Graphics;
import java.io.Serializable;
import java.util.Random;

public class Pinky extends Ghost {

	// Construtor do fantasma Pinky
	public Pinky(String imageName) {
		super(imageName);
	}

	// Define a direção o fantasma Pinky vai se movimentar e também desenha o
	// fantasma
	@Override
	public void autoDraw(Graphics g) {
		Pacman pacman = Drawing.getGameScreen().getPacman();
		Position posPacman = pacman.getPos();
		int movDirectionPacman = pacman.getMoveDirection();

		if (movDirectionPacman == MOVE_LEFT || movDirectionPacman == MOVE_RIGHT) {
			if (!this.isMortal) {
				followPacmanHorizontal(movDirectionPacman, posPacman);
			} else {
				escapePacmanHorizontal(movDirectionPacman, posPacman);
			}
		} else {
			moveRandom();

		}

		Drawing.draw(g, this.imageIcon, pos.getY(), pos.getX());

	}

}
