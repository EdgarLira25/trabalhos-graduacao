public class App {
    public static void main(String[] args) throws Exception {
        
        
        Paralelogramo par = new Paralelogramo(3, 5, 45);
        Retangulo ret = new Retangulo(2, 2, 90);
        Quadrado qua = new Quadrado (3, 6, 90);
        
        System.out.println(par.toString());
        System.out.println(ret.toString());
        System.out.println(qua.toString());
        
    }
}
