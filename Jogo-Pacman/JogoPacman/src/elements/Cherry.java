package elements;

import utils.Drawing;
import java.awt.Graphics;
import java.io.Serializable;

public class Cherry extends ElementGivePoint{
	private long startTime=0;
	// Construtor do Element Cherry
    public Cherry(String imageName) {
        super(imageName);
        this.numberPoints=100;
        this.startTime=System.currentTimeMillis();
    }
	// Retorna o valor da variavel startTime
	public long getStartTime() {
		return this.startTime;
	}
	// Redefine o valor da variavel startTime
	public void setStartTime(long start){
		this.startTime=start;
	}

    
}
