public class Data {
    
    int dia, mes, ano;

    public Data(int dia, int mes, int ano ){

        this.dia = dia;
        this.mes = mes;
        this.ano = ano;

    }

    public void troca_data(Data data){

        Data temp = new Data(dia, mes, ano);

        ano = data.ano;
        mes = data.mes;
        dia = data.dia;

        data.setAno(temp.ano);
        data.setDia(temp.dia);
        data.setMes(temp.mes);

    }

    public int getAno() {
        return ano;
    }
    public int getDia() {
        return dia;
    }
    public int getMes() {
        return mes;
    }
    public void setAno(int ano) {
        this.ano = ano;
    }
    public void setDia(int dia) {
        this.dia = dia;
    }
    public void setMes(int mes) {
        this.mes = mes;
    }

    @Override
    public String toString() {
        return this.dia + "/"+ this.mes + "/" + this.ano;
    }
}
