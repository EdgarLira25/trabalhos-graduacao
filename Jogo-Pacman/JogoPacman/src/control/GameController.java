package control;

import elements.*;

import java.awt.Graphics;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.Random;

import javax.swing.JOptionPane;

import utils.Consts;
import utils.Position;

public class GameController implements Serializable {
	int scoreGhost;
// Desenha todos os elementos no mapa
	public void drawAllElements(ArrayList<Element> elemArray, Graphics g) {
		Pacman pacman = (Pacman) elemArray.get(0);
		int numberGhost = pacman.getNumberGhosttoEat();
		for (int i = numberGhost + 1; i < elemArray.size(); i++) {
			elemArray.get(i).autoDraw(g);
		}

		for (int i = 0; i <= numberGhost; i++) {
			elemArray.get(i).autoDraw(g);
		}

	}

// Desenha todos os elementos no mapa
	public void processAllElements(ArrayList<Element> elements, int[][] matrix, int cont) {
		if (elements.isEmpty())
			return;
		Pacman pacman = (Pacman) elements.get(0);
		int numberGhost = pacman.getNumberGhosttoEat();

		checkElementColideWall(elements, numberGhost);
		boolean overlapGhostPacman = checkOverlapGhostPacman(elements, pacman, numberGhost);

		if (overlapGhostPacman) {
			pacman.setNumberLifes(pacman.getLifes() - 1);
			if (pacman.getLifes() > 0) {

				pacman.setPosition(1, 1);

			} else {
				Main.gamePacMan.dispose();
				JOptionPane.showMessageDialog(null, "Fim do jogo");
				System.exit(0);
			}

		} else if (pacman.getNumberDotstoEat() == 0) {
			Main.level += 1;
			if (Main.level >= 5) {
				Main.gamePacMan.dispose();
				JOptionPane.showMessageDialog(null, "Fim do jogo");
				System.exit(0);
			} else {
				Main.gamePacMan.reStartGame(pacman.getLifes());
			}
		} else {
			checkPacmanEatSomeOneAndOrTimeFruittoDesappear(elements, pacman);
			checkTimetoAppearFruit(elements, matrix);
			checkTimeGhostBeNormal(elements, pacman);

			pacman.move();
			for (int i = 1; i <= pacman.getNumberGhosttoEat(); i++) {
				ElementMove elementMove = (ElementMove) elements.get(i);
				if (!elementMove.isMortal()) {
					elementMove.move();
				} else {
					if (elementMove.isMortal() && cont % 2 == 0) {
						elementMove.move();
					}
				}
			}
		}
	}
	//Checa se o pacman colidiu com um fantasma
	private boolean checkOverlapGhostPacman(ArrayList<Element> elements, Pacman pacman, int numberGhost) {
		boolean overlapGhostPacman = false;
		for (int i = 1; i <= numberGhost; i++) {
			if (elements.get(i).overlap(pacman) & !elements.get(i).isMortal()) {
				overlapGhostPacman = true;
			}
		}
		return overlapGhostPacman;
	}
	// checa se o pacman vai colidir com a parede ao se movimentar
	private void checkElementColideWall(ArrayList<Element> elements, int numberGhost) {
		for (int i = 0; i <= numberGhost; i++) {
			ElementMove elementMove = (ElementMove) elements.get(i);
			if (!isValidPosition(elements, elementMove)) {
				elementMove.backToLastPosition();
				elementMove.setMovDirection(ElementMove.STOP);

			}
		}

	}
// Checa o que o pacman comeu, e o tempo para as frutas ou determinados Elements desaparecerem
	private void checkPacmanEatSomeOneAndOrTimeFruittoDesappear(ArrayList<Element> elements, Pacman pacman) {

		Element eTemp;

		for (int i = 1; i < elements.size(); i++) {
			
			eTemp = elements.get(i);
			if (pacman.overlap(eTemp)) {
				if (eTemp.isTransposable() && eTemp.isMortal()) {
					elements.remove(eTemp);
					if (eTemp instanceof Ghost) {

						pacman.minusNumberGhotstoEat();
						pacman.addScore(scoreGhost);
						pacman.addRemainingScore(scoreGhost);
						imagemPonto ponto = null;

					//imagem ao comer fantasma
						if (scoreGhost == 200){
						ponto = new imagemPonto("200.png");
					}
						else if (scoreGhost == 400){
						ponto = new imagemPonto("400.png");
					} 	else if(scoreGhost == 800){
						ponto = new imagemPonto("800.png");
					}  	else {
						ponto = new imagemPonto("1600.png");
					}
							
						 
						ponto.setStartTime(System.currentTimeMillis());
						Position pos = pacman.getPos();
						ponto.setPosition(pos.getX(), pos.getY());
						elements.add(ponto);
						
						
						scoreGhost = scoreGhost * 2;
						
					}
					if (eTemp instanceof NewElement) {
						if (((NewElement) eTemp).getTakeLife() > 0)
							pacman.addLife();
						if (((NewElement) eTemp).getTakeLife() < 0) {
							pacman.rmvlife();
							if (pacman.getLifes() == 0) {
								Main.gamePacMan.dispose();
								JOptionPane.showMessageDialog(null, "Fim do jogo");
								System.exit(0);
							}
						}
					}

					if (eTemp instanceof ElementGivePoint) {
						pacman.addScore(((ElementGivePoint) eTemp).getNumberPoints());
						pacman.addRemainingScore(((ElementGivePoint) eTemp).getNumberPoints());

						if (eTemp instanceof PacDots) {
							pacman.minusNumberDotstoEat();
						}
						if (eTemp instanceof PowerPellet) {
							scoreGhost = 200;
							for (int k = 1; k <= pacman.getNumberGhosttoEat(); k++) {

								((Ghost) elements.get(k)).changeGhosttoBlue("ghostBlue.png");

							}
							pacman.setStartTimePower(System.currentTimeMillis());

						}

					}
				}
				int remainingScore = pacman.getRemainingScore();
				if (remainingScore > 10000) {
					pacman.addLife();
					pacman.setRemainingScore(remainingScore - 10000);
				}

			} else {
				if (eTemp instanceof imagemPonto){

					long elapsed = System.currentTimeMillis() - ((imagemPonto) eTemp).getStartTime();
					if (elapsed >= 1500) {
					elements.remove(eTemp);
					}
				}
				if (eTemp instanceof Cherry) {
					long elapsed = System.currentTimeMillis() - ((Cherry) eTemp).getStartTime();
					if (elapsed >= 15000) {
						elements.remove(eTemp);
					}

				}
				if (eTemp instanceof Strawberry) {
					long elapsed = System.currentTimeMillis() - ((Strawberry) eTemp).getStartTime();
					if (elapsed >= 15000) {
						elements.remove(eTemp);
					}
				}

				if (eTemp instanceof TakeLife) {
					long elapsed = System.currentTimeMillis() - ((TakeLife) eTemp).getStartTime();
					if (elapsed >= 15000) {
						elements.remove(eTemp);
					}

				}
				if (eTemp instanceof GiveLife) {
					long elapsed = System.currentTimeMillis() - ((GiveLife) eTemp).getStartTime();
					if (elapsed >= 15000) {
						elements.remove(eTemp);
					}
				}

			}
		}

	}

	//Checa o tempo para certas frutas aparecerem
	private void checkTimetoAppearFruit(ArrayList<Element> elements, int[][] matrix) {

		long elapsedTime = System.currentTimeMillis() - Main.time;

		if (elapsedTime % 3000 <= 10 && Main.level == 4) {

			GiveLife gLife = new GiveLife("lifep.png");
			gLife.setStartTime(System.currentTimeMillis());
			Position pos = getValidRandomPositionMatrix(matrix);
			gLife.setPosition(pos.getX(), pos.getY());
			elements.add(gLife);

		}

		if (elapsedTime % 3000 <= 10 && Main.level == 4) {

			TakeLife tLife = new TakeLife("lifep.png");
			tLife.setStartTime(System.currentTimeMillis());
			Position pos = getValidRandomPositionMatrix(matrix);
			tLife.setPosition(pos.getX(), pos.getY());
			elements.add(tLife);

		}

		if (elapsedTime % 75000 <= 10) {
			Strawberry straw = new Strawberry("strawberry.png");
			straw.setStartTime(System.currentTimeMillis());
			Position pos = getValidRandomPositionMatrix(matrix);
			straw.setPosition(pos.getX(), pos.getY());
			elements.add(straw);
		}
		if (elapsedTime % 50000 <= 10) {
			Cherry cherry = new Cherry("cherry.png");
			cherry.setStartTime(System.currentTimeMillis());
			Position pos = getValidRandomPositionMatrix(matrix);
			cherry.setPosition(pos.getX(), pos.getY());
			elements.add(cherry);
		}

	}

	// procura posições validas para adicionar as frutas
	private Position getValidRandomPositionMatrix(int[][] matrix) {
		Random gerador = new Random();
		int x;
		int y;
		Position pos = new Position(0, 0);
		do {
			x = gerador.nextInt(Consts.NUM_CELLS);
			y = gerador.nextInt(Consts.NUM_CELLS);
		} while (matrix[x][y] == 1 || matrix[x][y] == 7);
		pos.setPosition(x, y);
		return pos;
	}
// verifica o tempo para os fantasmas voltarem ao normal após pacman comer uma power pellet
	private void checkTimeGhostBeNormal(ArrayList<Element> elements,
			Pacman pacman) {
		long start = pacman.getStartTimePower();
		if (start != 0) {
			long elapsedTimePower = System.currentTimeMillis() - start;
			if (elapsedTimePower >= 7000) {

				pacman.setStartTimePower(0);
				Element e;
				for (int i = 1; i <= pacman.getNumberGhosttoEat(); i++) {
					e = elements.get(i);
					if (e instanceof Blinky) {
						((Blinky) e).changeGhosttoNormal("blinky.png");
					}
					if (e instanceof Pinky) {
						((Pinky) e).changeGhosttoNormal("pinky.png");
					}
					if (e instanceof Inky) {
						((Inky) e).changeGhosttoNormal("inky.png");
					}
					if (e instanceof Clyde) {
						((Clyde) e).changeGhosttoNormal("clyde.png");
					}

				}

			}

		}

	}
	// Checa checa se o Element esta em uma posição valida
	public boolean isValidPosition(ArrayList<Element> elemArray, Element elem) {
		Element elemAux;
		for (int i = 1; i < elemArray.size(); i++) {
			elemAux = elemArray.get(i);
			if (!elemAux.isTransposable())
				if (elemAux.overlap(elem))
					return false;
		}
		return true;
	}
}
