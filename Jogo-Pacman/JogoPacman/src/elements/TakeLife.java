package elements;

import utils.Drawing;
import java.awt.Graphics;
import java.io.Serializable;

public class TakeLife extends NewElement {
	private long startTime=0;
	/*
	 * Construtor do Elemento criado
	 * e retira vida se for comido pelo fantasma
	 * 
	 */
	public TakeLife(String imageName) {
        super(imageName);
        this.takeLife=-1;
        this.startTime=System.currentTimeMillis();
    }
	// Retorna o valor da variavel startTime
	public long getStartTime() {
		return this.startTime;
	}
	// Muda o valor do startTime
	public void setStartTime(long start){
		this.startTime=start;
	}
	
}
