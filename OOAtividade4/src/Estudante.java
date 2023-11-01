public class Estudante implements Comparable<Object> {

    String id;
    String nome;
    Double nota;

    Estudante(String id, String nome, Double nota) {

        this.id = id;
        this.nome = nome;
        this.nota = nota;

    }

    public void setId(String id) {
        this.id = id;
    }

    public String getId() {
        return id;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

    public void setNota(Double nota) {
        this.nota = nota;
    }

    @Override
    public int compareTo(Object o) {

    if(getNota() - ((Estudante) o).getNota() > 0) 
    return 1;
    else if(getNota() - ((Estudante) o).getNota() < 0) 
    return -1;
    return 0;
    
    }

    public Double getNota() {
        return nota;
    }

    @Override
    public String toString() {

        return " Id: " + id + " Nome: " + nome + " Nota: " + nota;

    }
}
