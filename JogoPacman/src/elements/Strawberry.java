package elements;

import utils.Drawing;
import java.awt.Graphics;
import java.io.Serializable;

public class Strawberry extends ElementGivePoint {
	private long startTime=0;
	public Strawberry(String imageName) {
        super(imageName);
        this.numberPoints=300;
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
