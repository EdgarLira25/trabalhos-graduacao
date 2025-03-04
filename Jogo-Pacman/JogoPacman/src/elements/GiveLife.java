package elements;


import utils.Drawing;
import java.awt.Graphics;
import java.io.Serializable;

public class GiveLife extends NewElement {

	private long startTime=0;
	// Contrutor do Element GiveLife
    public GiveLife(String imageName) {
        super(imageName);
        this.takeLife=1;
        this.startTime=System.currentTimeMillis();
    }
	// Retorna o valor da variavel startTime
	public long getStartTime() {
		return this.startTime;
	}
	// Define o valor da variavel startTime
	public void setStartTime(long start){
		this.startTime=start;
	}

}