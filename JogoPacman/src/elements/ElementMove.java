package elements;

import utils.Drawing;
import utils.Position;

import java.awt.Graphics;
import java.io.Serializable;
import java.util.Random;

public abstract class ElementMove extends Element{
    
    public static final int STOP = 0;
    public static final int MOVE_LEFT = 1;
    public static final int MOVE_RIGHT = 2;
    public static final int MOVE_UP = 3;
    public static final int MOVE_DOWN = 4;
    
    private int movDirection = STOP;
    // Retorna um int que define a direção que o Element irá se mover
    public int getMoveDirection(){
    	return movDirection;
    }
    // Contrutor do Element move
    public ElementMove(String imageName) {
        super(imageName);
    }
    
    //  Método abstrato para desenhar o ElementMove
    abstract public void autoDraw(Graphics g);
    
    // Elemento volta para a ultima posição valida
    public void backToLastPosition(){
        this.pos.comeBack();
    }
    
    // Define o valor da variavel movDirection
    public void setMovDirection(int direction) {
        movDirection = direction;
    }
    // move o Elemento para direção definida
    public void move() {
        switch (movDirection) {
            case MOVE_LEFT:
                this.moveLeft();
                break;
            case MOVE_RIGHT:
                this.moveRight();
                break;
            case MOVE_UP:
                this.moveUp();
                break;
            case MOVE_DOWN:
                this.moveDown();
                break;
            default:
                break;
        }
    }
    //retorna true se o elemento pode se mover para cima
    public boolean moveUp() {
        return this.pos.moveUp();
    }

    //retorna true se o elemento pode se mover para baixo
    public boolean moveDown() {
        return this.pos.moveDown();
    }

    //retorna true se o elemento pode se mover para direita
    public boolean moveRight() {
        return this.pos.moveRight();
    }
    
    //retorna true se o elemento pode se mover para esquerda
    public boolean moveLeft() {
        return this.pos.moveLeft();
    }


}
