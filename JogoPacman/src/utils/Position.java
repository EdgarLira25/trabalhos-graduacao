package utils;

import java.io.Serializable;


public class Position  implements Serializable{
    /* Elements are positioned in a grid layout (integers).
       However, walking is implemented with float steps (continuous).
       This is why x and y are double types.
       x and y ranges from 0 to CELL_SIZE*NUM_CELLS.
       The real pixel positioning is converted by the Drawing class.
       As consequence, any element has size 1x1 (x and y). */
    private double x;
    private double y;
    
    private double previousX;
    private double previousY;

    // Método que chama a função setPosition() e recebe como parâmetros as posições x e y
    public Position(double x, double y){
        this.setPosition(x,y);
    }
    // verifica se a posição que o Element esta tentando ir é valida
    public final boolean setPosition(double x, double y){
        int factor = (int)Math.pow(10, Consts.WALK_STEP_DEC_PLACES+1);
    
        x = (double)Math.round(x * factor) / factor;
        y = (double)Math.round(y * factor) / factor;
        
        if(x < 0 || x > utils.Consts.NUM_CELLS-1)
            return false;
        previousX = this.x;
        this.x = x;
        
        if(y < 0 || y > utils.Consts.NUM_CELLS-1)
            return false;
        previousY = this.y;
        this.y = y;
        return true;
    }
    // Retorna a x do Element
    public double getX(){
        return x;
    }
   // Retorna a posição y do Element 
    public double getY(){
        return y;
    }

    public boolean comeBack(){
        return this.setPosition(previousX,previousY);
    }
    // Move o Element para cima se a função setPosition() retornar true
    public boolean moveUp(){
        return this.setPosition(this.getX()-Consts.WALK_STEP, this.getY());
    }
    // Move o Element para baixo se a função setPosition() retornar true 
    public boolean moveDown(){
        return this.setPosition(this.getX()+Consts.WALK_STEP, this.getY());
    }
    // Move o Element para direita se a função setPosition() retornar true
    public boolean moveRight(){
        return this.setPosition(this.getX(), this.getY()+Consts.WALK_STEP);
    }
    // Move o Element para esquerda se a função setPosition() retornar true
    public boolean moveLeft(){
        return this.setPosition(this.getX(), this.getY()-Consts.WALK_STEP);        
    }
    // Calcula e retorna a distancia entre os Elements
	public double distance(Position pos) {
		return Math.sqrt(Math.pow(x-pos.getX(),2)+Math.pow(y-pos.getY(),2));
	}
    
}
