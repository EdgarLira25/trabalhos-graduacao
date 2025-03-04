import java.util.ArrayList;
import java.util.LinkedList;

public class testeUniversidade {
    public static void main(String[] args) throws Exception {
        
        Turma list1 = new Turma(new ArrayList<>());
        Turma list2 = new Turma(new LinkedList<>());

        Estudante a = new Estudante("123", "Edgar", (double)5);
        Estudante b = new Estudante("142", "Brewgs",(double)8);
        Estudante c = new Estudante("122", "Bebeto",(double)7);
        Estudante d = new Estudante("135", "Hauses",(double)9);    
        Estudante e = new Estudante("158", "PepsBr", (double)4);
        
        list1.adiciona(a);
        list1.adiciona(b);
        list2.adiciona(c);
        list2.adiciona(d);
        list2.adiciona(e);

        // est.add(new Estudante("123", "Edgar", (double)5));
        // est.add(new Estudante("142", "Brewgs",(double)8));
        // est.add(new Estudante("122", "Bebeto",(double)7));
        // est.add(new Estudante("135", "Hauses",(double)9));
        // est.add(new Estudante("158", "PepsBr", (double) 4));

        list1.adiciona(new Estudante("123", "Edgar", (double)5));
        list1.adiciona(new Estudante("142", "Brewgs",(double)8));
        list2.adiciona(new Estudante("122", "Bebeto",(double)7));
        list2.adiciona(new Estudante("135", "Hauses",(double)9));
        list2.adiciona(new Estudante("158", "PepsBr",(double)4));

        list1.getMediaNotaTurma();
        list2.getMediaNotaTurma();

        System.out.println("turma 1" + list1);
        System.out.println("turma 2" + list2);
                
        System.out.println("Estudante maior nota T1:" + list1.MaiorNota());
        System.out.print("Estudante maior nota T2:" + list2.MaiorNota1());
        
        list1.estudantesAprovados();
        list2.estudantesAprovados();

        System.out.println();
        list1.juntaLista(list2);
        System.out.println("turma 1" + list1);
        list1.atualizaMedia();
        System.out.println("turma 2" + list2);

    }
}