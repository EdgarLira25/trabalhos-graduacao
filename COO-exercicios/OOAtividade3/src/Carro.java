public class Carro implements EmissorCarb{

    int pessoas_carro;
    double motor;
    double distancia;
    
    public Carro(int pessoas_carro, double motor, double distancia){
        
        this.pessoas_carro = pessoas_carro;
        this.motor = motor;
        this.distancia = distancia;
    
    }

    public double getDistancia() {
        return distancia;
    }
    public double getMotor() {
        return motor;
    }
    public int getPessoas_carro() {
        return pessoas_carro;
    }
    public void setDistancia(double distancia) {
        this.distancia = distancia;
    }
    public void setMotor(double motor) {
        this.motor = motor;
    }
    public void setPessoas_carro(int pessoas_carro) {
        this.pessoas_carro = pessoas_carro;
    }

    @Override
    public double getCarbonoEmitido() {
        // TODO Auto-generated method stub
        return getDistancia()*10 + getMotor()*20 + getPessoas_carro()*5;
    }

    @Override
    public String toString() {
        // TODO Auto-generated method stub
        return "Carbono emitido = " + getCarbonoEmitido();
    }
    
}