import java.util.function.BiConsumer;

public class App {
    public static void main(String[] args) throws Exception {
       
        Casa casa = new Casa();
        Carro carro = new Carro(4,(double) 6,(double)100.0);
        Bicicleta bicicleta = new Bicicleta(10000);
        

        System.out.println(bicicleta.toString());
        


    }
}
