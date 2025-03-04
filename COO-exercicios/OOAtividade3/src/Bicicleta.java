public class Bicicleta implements EmissorCarb{

    int distancia;

    public Bicicleta(int distancia){

        this.distancia = distancia;

    }


    @Override
    public double getCarbonoEmitido() {

        return 0 * distancia;
    }
    @Override
    public String toString() {
        // TODO Auto-generated method stub
        return "Carbono Emitido = " + getCarbonoEmitido();
    }

}
