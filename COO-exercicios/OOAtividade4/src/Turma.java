import java.util.*;

public class Turma {

    private List<Estudante> listaTurma;

    private double mediaNotaTurma;

    Turma(List <Estudante> x) {

        
        mediaNotaTurma = 0;
        
        listaTurma = x;

    }

    public void adiciona(Estudante x) {

        listaTurma.add(x);

    }

    public void remove(Estudante x) {

        listaTurma.remove(x);

    }

    public void juntaLista(Turma x) {

        listaTurma.addAll(x.listaTurma);
        x.setMediaNotaTurma(0);
        x.listaTurma.removeAll(x.listaTurma);

    }

    public double atualizaMedia() {

        double total = 0;
        double i = 0;
        for (Estudante a : listaTurma) {

            a.getNota();
            total += a.getNota();
            i = i + 1;

        }

        mediaNotaTurma = total / i;

        return mediaNotaTurma;
    }

    /*public Estudante MaiorNota() {

        Estudante maior = listaTurma.get(0);

        for (Estudante a : listaTurma) {

            if (a.nota >= maior.nota)
                maior = a;

        }
        return maior;
    }*/
    
      public Estudante MaiorNota(){

      return Collections.max(listaTurma, new NotaComparator());
      
      }
      public Estudante MaiorNota1(){

        return Collections.max(listaTurma, new NotaComparator());
        
        }

    public void estudantesAprovados() {
        System.out.print("\naprovados: ");

        for (Estudante a : listaTurma) {

            if (a.nota >= 7) {
                System.out.print(a);

            }
        }
    }

    public double getMediaNotaTurma() {

        double total = 0;
        double i = 0;

        for (Estudante a : listaTurma) {

            a.getNota();
            total += a.getNota();
            i = i + 1;

        }

        mediaNotaTurma = total / i;

        return mediaNotaTurma;
    }

    public void setMediaNotaTurma(double mediaNotaTurma) {
        this.mediaNotaTurma = mediaNotaTurma;

    }

    @Override
    public String toString() {

        return listaTurma.toString();

    }

}
