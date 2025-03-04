import java.util.Comparator;

public class NotaComparator implements Comparator<Estudante> {

    @Override
    public int compare(Estudante e1, Estudante e2) {

        if (e1.getNota() < e2.getNota()) {
            return -1;
        } else {
            return 1;
        }

    }

}