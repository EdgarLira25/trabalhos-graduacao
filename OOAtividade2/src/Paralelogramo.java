public class Paralelogramo {

    double a;
    double h;
    double angulo;

    public Paralelogramo(double a, double h, double angulo){
    
        this.a = a; 
        this.h = h;
        this.angulo = angulo;
    
    }
    public double perimetro(){
        return 2*a + 2*h; 
    }

    public double area(){
        return a * h * Math.sin(angulo*Math.PI/180);     
    }

    public double getA() {
        return a;
    }
    public double getAngulo() {
        return angulo;
    }
    public double getH() {
        return h;
    }
    public void setA(double a) {
        this.a = a;
    }
    public void setAngulo(double angulo) {
        this.angulo = angulo;
    }
    public void setH(double h) {
        this.h = h;
    }
    @Override
    public String toString() {
        // TODO Auto-generated method stub
        return "lado1 = "+ a +" lado2 = "+ h +" ângulo = " + angulo +" perimetro = " + perimetro() + " área = "+ area()        
        ;
    }
}
