package elements;

import utils.Drawing;
import java.awt.Graphics;

public class Pacman extends ElementMove {

	private int score = 0;
	private int remainingScore = 0;
	private int numberLifes = 1;
	private int numberDotstoEat = 0;
	private int numberGhosttoEat = 4;
	private long startTimePower = 0;

	// Construtor do Pacman
	public Pacman(String imageName) {
		super(imageName);
		this.isMortal = true;

	}

	// Retorna o Score do Pacman
	public int getScore() {
		return this.score;
	}

	// Returna o valor da variavel RemainingScore
	public int getRemainingScore() {
		return this.remainingScore;
	}

	// Retorna o numero de vidas do pacman
	public int getLifes() {
		return this.numberLifes;
	}

	// Define o score do pacman
	public void setScore(int score) {
		this.score = score;
	}

	// Retorna o numero o NumberDotstoEat
	public int getNumberDotstoEat() {
		return this.numberDotstoEat;
	}

	// Retorna o valor da variavel startTimePower
	public long getStartTimePower() {
		return this.startTimePower;
	}

	// Redefine o valor da variavel startTimePower
	public void setStartTimePower(long start) {
		this.startTimePower = start;
	}

	// Redefine o valor da variavel remainingScore
	public void setRemainingScore(int remainingScore) {
		this.remainingScore = remainingScore;
	}

	// Redefine o numero de vidas do Pacman
	public void setNumberLifes(int numberLifes) {
		this.numberLifes = numberLifes;
	}

	// Soma 1 no numero de vidas do pacman
	public void addLife() {
		this.numberLifes++;
	}

	// Subtrai 1 no numero de vidas do pacman
	public void rmvlife() {
		this.numberLifes--;
	}

	// Adiciona 1 no numberDotstoEat
	public void addNumberDotstoEat() {
		this.numberDotstoEat++;
	}

	// Subtrai 1 no numberDotstoEat
	public void minusNumberDotstoEat() {
		this.numberDotstoEat--;
	}

	// Subtrai 1 no numberGhosttoEat
	public void minusNumberGhotstoEat() {
		this.numberGhosttoEat--;
	}

	// Adiciona um valor ao score
	public void addScore(int i) {
		score = score + i;
	}

	// Soma um valor no remainingScore
	public void addRemainingScore(int i) {
		this.remainingScore = this.remainingScore + i;
	}

	// Desenha o Element Pacman
	@Override
	public void autoDraw(Graphics g) {
		Drawing.draw(g, this.imageIcon, pos.getY(), pos.getX());
	}

	// Retorna o numberGhosttoEat
	public int getNumberGhosttoEat() {
		return numberGhosttoEat;
	}

}