public class App {
    public static void main(String[] args) throws Exception {
        Data data1 = new Data(22, 2, 2222); 
        Data data2 = new Data(11, 1, 1111); 

        System.out.println("data1 = " +  data1.toString());
        System.out.println("data2 = " + data2.toString());
        
        data1.troca_data(data2);

        System.out.println("data1 = " +  data1.toString());
        System.out.println("data2 = " + data2.toString());

 }
}
