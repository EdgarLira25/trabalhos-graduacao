
public class SubsAlfa {
    StringBuilder alfa;
    final static String abc = "abcdefghijklmnopqrstuvwxyz";

    //True quer dizer que sofreu mudanca
    boolean[] booleans = new boolean[26];
    int numMax = 0;

    SubsAlfa(){
        alfa = new StringBuilder();
        for (int i = 0; i < 26; i++) {
            alfa.append("-");
            booleans[i] = false;
        }
    }

    SubsAlfa(SubsAlfa subsAlfa){
        this.alfa = new StringBuilder(subsAlfa.alfa);
        this.booleans = subsAlfa.booleans.clone();
    }

    SubsAlfa(String alfa){
        this.alfa = new StringBuilder(alfa);
        for (int i = 0; i < 26; i++) {
            if(alfa.charAt(i) == '-'){
                booleans[i] = false;
            } else
                booleans[i] = true;
        }
    }

    /**
     * Método para adicionar caracter para o alfabeto de substituicao.
     * @param indexOf - Posicao da Letra do alfabeto que sera posto no alfabeto de substituição
     * @param cipherChar - o caracter correspondente ao parametro anterior
     * @return True para quando o caracter for atribuido
     *         False para quando caracter nao for atribuido
     */
    public boolean setChar(char indexOf, char cipherChar){
        int i = abc.indexOf(indexOf);
        int exists = alfa.indexOf(String.valueOf(cipherChar));
        if(!booleans[i] && exists == -1){
            alfa.setCharAt(i, cipherChar);
            numMax++;
            booleans[i] = true;
            return true;
        } else{
//            System.out.println("Chamada setChar Com " +
//                    indexOf + " e " +
//                    newChar + ". ERRO: Letra da posicao ja preenchida com " +
//                    alfa.charAt(i));
            return false;
        }

    }

    /**
     * método para "esvaziar" alfabeto de substituição.
     */
    public void reset(){
        alfa = new StringBuilder();
        for (int i = 0; i < 26; i++) {
            alfa.append("-");
            booleans[i] = false;

        }
    }

    /**
     * Transforma o alfabeto de substituição em String
     * @return String  alfabeto de substituição
     */
    public String toString(){
        return alfa.toString();
    }

    /**
     * Print decifrando a cifra dada como parametro utilizando o alfabeto de substituição. Para caracteres nao atribuido é posto '-'
     * @param cipher cifra
     */
    public void printCleanDecipher(String cipher){
        char[] cipherCharArray = cipher.toCharArray();
        for (int i = 0; i < cipherCharArray.length; i++) {
            int x = alfa.indexOf(String.valueOf(cipherCharArray[i]));
            if(x >= 0 ){
                cipherCharArray[i] = abc.charAt(x);
            } else
                cipherCharArray[i] = '-';
        }
        for (char c: cipherCharArray) {
            System.out.print(c);
        }
        System.out.println();
    }


    /**
     * retorna a String decifrando a cifra dada como parametro utilizando o alfabeto de substituição. Para caracteres nao atribuido é posto '-'
     * @param cipher cifra
     * @return String decifrada
     */
    public String stringCleanDecipher(String cipher){
        char[] cipherCharArray = cipher.toCharArray();
        for (int i = 0; i < cipherCharArray.length; i++) {
            int x = alfa.indexOf(String.valueOf(cipherCharArray[i]));
            if(x >= 0 ){
                cipherCharArray[i] = abc.charAt(x);
            } else
                cipherCharArray[i] = '-';
        }
       return new String(cipherCharArray);
    }

    /**
     * Usado para decifrar somente uma parte da cifra
     * @param cipherPart parte da cifra
     * @return String decifrada
     */
    public String decipherPart(String cipherPart){
        char[] cipherCharArray = cipherPart.toCharArray();
        for (int i = 0; i < cipherCharArray.length; i++) {
            int x = alfa.indexOf(String.valueOf(cipherCharArray[i]));
            if(x >= 0 ){
                cipherCharArray[i] = abc.charAt(x);
            }
        }
        return new String(cipherCharArray);
    }

    /**
     * Usado para decifrar somente um caracter
     * @param c caracter cifrado
     * @return Caracter decifrado
     */
    public char decipherChar(char c){

            int x = alfa.indexOf(String.valueOf(c));
            if(x >= 0 ){
                return abc.charAt(x);
            }
            return '-';
    }

    /**
     * Print do alfabeto de substituição.
     */
    public void printAlfa(){
        char[] c = abc.toCharArray();
        for (int i = 0; i < c.length; i++) {
            if(booleans[i]){
                c[i] = abc.charAt(i);
            } else
                c[i] = '-';
        }

        System.out.println("Alfabeto de Substituicao");
        for (char ch: c) {
            System.out.print(ch);
        }
        System.out.println();
        System.out.println(alfa.toString());
    }

    /**
     * Atribui caracteres para o alfabeto de Substituicao a partir dos caracteres da String.
     * @param str String com os caracteres que serão atribuidos
     * @param cipherSubString substring da cifra
     * @return boolean confirmando se todos os caracteres foram atribuidos sem conflitos
     */
    public boolean setCharFromString(String str, String cipherSubString){
        char strChar = 0;
        char cipherChar = 0;
        for (int i = 0; i < str.length(); i++) {

            strChar = str.charAt(i);
            cipherChar = cipherSubString.charAt((i));

            if (!setChar(strChar, cipherChar)){
                //verificar o caracter na string decifrada eh igual a da cifra
                if( !(strChar == decipherChar(cipherChar) )){
                    return false;
                }
            }
        }
        //nao houve dobra
        return true;
    }

    /**
     * Dada a cifra decifrada identifica qual a String com mais caracteres presente
     * @param cipher cifra
     * @return o String com o maior numero de caracteres
     */
    public String maxContinuousString(String cipher){
        int lenght = 0;
        int maxLenght = 0;
        String result = "";
        StringBuilder str = new StringBuilder();
        char[] cipherCharArray = cipher.toCharArray();
        for (int i = 0; i < cipherCharArray.length; i++) {
            int x = alfa.indexOf(String.valueOf(cipherCharArray[i]));
            if(x >= 0 ){
                lenght++;
                str.append(abc.charAt(x));
            } else {
                if (maxLenght < lenght){
                    maxLenght = lenght;
                    result = str.toString();
                    lenght = 0;
                    str.delete(0, str.length());
                } else {
                    //reset
                    lenght=0;
                    str.delete(0, str.length());
                }

            }
        }
        return result;
    }

}
