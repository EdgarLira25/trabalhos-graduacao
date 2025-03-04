
import java.io.BufferedReader;
import java.io.FileReader;
import java.net.URLDecoder;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Crypto {

    //Lista contendo as palavras do dicionario
    final private List<String> dicionario;

    //Cifra
    final private String cipher;

    //Alfabetos de substituição
    SubsAlfa sub;
    SubsAlfa temp;
    SubsAlfa temp1;
    SubsAlfa temp2;
    SubsAlfa temp3;
    SubsAlfa temp4;
    SubsAlfa temp5;
    SubsAlfa temp6;
    SubsAlfa temp7;
    SubsAlfa temp8;
    SubsAlfa temp9;

    Crypto(){
        dicionario = createListDicionario();
        cipher = readCipherFile();
        alfabetos = new ArrayList<>();
        palavras = new ArrayList<>();
    }

    String part;
    String cipherPart;
    List<String> alfabetos;

    List<String> palavras;

    /**
     * Método para ler arquivo com a cifra e retorna String com a cifra
     * @return String - cifra
     */
    private String readCipherFile() {
        try {

            BufferedReader br =
                    new BufferedReader(
                            new FileReader(
                                    //Caminho para o Grupo02_texto_cifrado.txt
                                    URLDecoder.decode(ClassLoader.getSystemResource("Grupo02_texto_cifrado.txt").getPath())
                            )
                    );
            String str = br.readLine();

            br.close();

            return str;

        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    /**
     * Método para ler arquivo dicionario e inicializa a lista com os elementos do dicionario.
     * Retorna Lista de String
     * @return ArrayList com elementos do dicionario
     */
    private List<String> createListDicionario() {
        try {

            BufferedReader br =
                    new BufferedReader(
                            new FileReader(
                                    //Caminho para o dicionario.txt
                                    URLDecoder.decode(ClassLoader.getSystemResource("dicionario.txt").getPath())
                            )
                    );

            List<String> lines = br.lines().toList();

            br.close();
            return lines;

        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    /**
     * Método para análise da cifra divididas posteriormente foi dividia em 3 métodos para cada
     */
    public void cipherAnalysis(){
        StringBuilder str = new StringBuilder();
        Map<Character, Integer> map = new HashMap<>();
        cipher.chars().forEach( c -> {
           char k = (char) c;
            if(map.containsKey(k)){
               map.put(k, map.get(k).intValue() + 1);
           } else
               map.put(k, 1);
        });
        System.out.println("Quantidade de letras usadas na cifras ");
        map.forEach((k, v) -> System.out.println("Letra " + k.toString().toUpperCase(Locale.ROOT) + " = " + v));
        System.out.println("Quantidade total de letras distintas usadas: " + map.size());

        //LETRAS MAIS USADAS
        //T U Z I J E

        //z j k y w x - sao as menos usadas
        //A G L V W X - não são usadas na cifra

        //O A E - SAO OS MAIS USADOS NO PORTUGUES
        //T Z U - SAO OS MAIS USADOS NA CIFRA

        //TIIZ
        //Palavra + palavra
        //Palavra + artigo + palavra
//        System.out.println("Analisando " + chars[0] + " && " + chars[1]);

        sub = new SubsAlfa();

        System.out.println();
        System.out.println(cipher);
        System.out.println();

        // ----------------------------------------------------------------------------------
        //METODOS COM AS TENTATIVAS ESCRITAS NO RELATORIO CADA TENTATIVA (EXCETO A 3) LEVA
        //DE 15 PARA MAIS MINUTOS

//       tentativa1();
//        tentativa2();
//        tentativa3();

        // ----------------------------------------------------------------------------------

        System.out.println();

        System.out.println("- - - - - - - - - - - - - - - - - - - - - - - - - - - ");

    }

    /**
     * Método para ler o arquivo verificados.txt e verificar se a existi a String de entrada no verificados.
     * @param str - String a ser verificado se ela está contida no verificador
     * @return boolean - true para caso a String está contida no verificador
     */
    public boolean verify(String str){
        try {
            BufferedReader br =
                new BufferedReader(
                        new FileReader(
                                //Caminho para o verificador.txt
                                URLDecoder.decode(ClassLoader.getSystemResource("verificador.txt").getPath())
                        )
                );

            String v = br.readLine();
            br.close();
            return (v.contains(str));

    } catch (Exception e) {
        throw new RuntimeException(e);
    }
    }

    /**
     * Método para verificar se a String decifrada até o momento (não completa) está contida no verificador e
     * se os caracteres seguidos da String str estão no verificador. Este Método não é usado
     * @param decipher - String com a cifra decifrada incompletamente.
     * @param str - String com um elemento do dicionario que está contida no verificador
     * @return boolean - true para ele pertence ao verificador e que os caracteres adjacentes são de acordo com o alfabeto
     * de substituição.
     */
    public boolean verifyDecipher(String decipher, String str){
        try {
            BufferedReader br =
                    new BufferedReader(
                            new FileReader(
                                    //Caminho para o verificador.txt
                                    URLDecoder.decode(ClassLoader.getSystemResource("verificador.txt").getPath())
                            )
                    );

            String v = br.readLine();
            br.close();
            int verIndex = v.indexOf(str);
            int decipherIndex = decipher.indexOf(str);
            if(verIndex != -1 && decipherIndex != -1){
                for (int i = decipherIndex; i < decipher.length(); i++) {
                    int incrementV = verIndex + i;
                    char c = decipher.charAt(i);
                    if( (c != '-') && (v.charAt(incrementV) != c) ){
                        return false;
                    }
                }
            }
            return true;

        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    /**
     * Primeira tentativa de decifrar cifra Monoalfabética. Foi verificado as frequencia dos caracteres da cifra e
     * a frequencia de letras do portugues, a fim de mapear algumas das letras para o alfabeto de substituição.
     * Fazendo isso, verificamos que os caracteres de maior frequencia e os caracteres que não foram utilizados,
     * os caracteres de maiores frequencias forram T, U e Z, e os caracteres que não foram utilizados foram
     * A, G, L, V, W e X. Para as 3 letras com as maiores frequencias, foi feita uma permutação com os caracteres
     * O, A, e E, que são os caracteres que mais ocorrem na Lingua portugues,
     * o que resulta em 6 alfabetos de substituição distintos. A partir disso, para cada um desses alfabetos,
     * a partir da posição 1 da cifra, foi feito um for para a iterar sobre os elementos da cifra até 11, podendo
     * ser aumentado, em seguida, em cada iteração são criados 3 alfabetos de substituição distintos onde cada
     * um é dado pela iteração de todos as letras do alfabeto e cada um herda o alfabeto do outro mais o resultado da permunta inicial,
     * isto é, atribui para o caracter b o valor de h, para o proximo alfabeto atribui c para i, e por último d
     * para o, o primeiro alfabeto só terá b para h, o segundo b para h e c para i, e o último terá todas as relações.
     * O último alfabeto corresponde a um "chute" para os 3 proximos caracteres a partir da posição dada pelo primeiro
     * for, sendo os 3 caracteres decifrado apos isso será feita a um ataque de dicionario, para ver quais palavras começam com os
     * 3 caracteres decifrados, pois são caracteres da cifra. Em seguida, as palavras são testadas para ver se elas se
     * "encaixam" na cifra, e caso elas "encaixem" é acresentado os valores para o alfabeto de substituição caso haja conflito, isto é,
     * o caractere ja foi atribuido a uma letra e com o acrescimo ele seria modificado, nesse caso e descatado as mudancas acrescidas.
     * Ao final é posto em uma lista os alfabetos de substituição gerados, o resultados para o laço inicial de 11 e as 6 permutas é maior que 18000.
     *
     */
    void tentativa1 (){


        //T Z U -> O A E
        permuta1();

        //T Z U -> O E A
        permuta2();

        //T Z U -> E A O
        permuta3();

        //T Z U -> E O A
        permuta4();

        //T Z U -> A O E
        permuta5();

        //T Z U -> A E O
        permuta6();
        System.out.println();
        
        alfabetos.forEach( s -> {
            SubsAlfa subsAlfa = new SubsAlfa(s);
            subsAlfa.printCleanDecipher(cipher);
        });


        // ----------------------------------------------------------------------------------

    }

    /**
     * Para a tentativa 2, foi feita 2 ataques de dicionario a fim de encontrar palavras consecutivas divididas por
     * 0 a 3 caracteres, 0 quando não ha caracter entre as duas palavras e 3 para quando existir por exemplo uma preposição.
     * esta tentativa é similar a primeira onde é feito um "chute" (iteração do alfabeto) para as 3 letras adjacentes na cifra sendo a posicao
     * inicial, a valor utilizado para a iteração no primeiro laço. Em seguida, é feita o ataque de dicionario palavras que comecam com o "chute",
     * para cada palavra encontrada é feito como na primeira tentativa,
     * em seguida e feita uma laco a partir da posicao do primeiro laco mais
     */
    void tentativa2(){
        for (int x = 1; x < 2; x++) {
            cipherPart = cipher.substring(x, x+3);
            System.out.println();
            System.out.println("Comeco iteracao separada "+x);
            for (int i = 0; i < SubsAlfa.abc.length()  ; i++) {
                temp1 = new SubsAlfa(sub.toString());
                if(!temp1.booleans[i]){
                    temp1.setChar(SubsAlfa.abc.charAt(i), cipherPart.charAt(0));
                    for (int j = 0; j < SubsAlfa.abc.length()  ; j++) {
                        temp2 = new SubsAlfa(temp1.toString());
                        if(!temp2.booleans[j]) {
                            temp2.setChar(SubsAlfa.abc.charAt(j), cipherPart.charAt(1));
                            for (int k = 0; k < SubsAlfa.abc.length(); k++) {
                                temp = new SubsAlfa(temp2.toString());
                                if(!temp.booleans[k]) {
                                    temp.setChar(SubsAlfa.abc.charAt(k), cipherPart.charAt(2));
                                    part = temp.decipherPart(cipherPart);
                                    for (String s: dicionario) {
                                        if(s.startsWith(part) ){
                                            temp3 = new SubsAlfa(temp.toString());
                                            if(temp3.setCharFromString(s,cipher.substring(x))){
//                                              //Proximas 5 letras depois da palavra obtida anteriormente
                                                for (int y = s.length() + x; y < s.length() + x + 5; y++) {
                                                    String cipherPart1 = cipher.substring(y, y+3);
                                                    for (int l = 0; l < SubsAlfa.abc.length()  ; l++) {
                                                        temp4 = new SubsAlfa(temp3.toString());
                                                        if(!temp4.booleans[l]){
                                                            temp4.setChar(SubsAlfa.abc.charAt(l), cipherPart1.charAt(0));
                                                            for (int m = 0; m < SubsAlfa.abc.length()  ; m++) {
                                                                temp5 = new SubsAlfa(temp4.toString());
                                                                if(!temp5.booleans[m]) {
                                                                    temp5.setChar(SubsAlfa.abc.charAt(m), cipherPart1.charAt(1));
                                                                    for (int n = 0; n < SubsAlfa.abc.length(); n++) {
                                                                        temp6 = new SubsAlfa(temp5.toString());
                                                                        if(!temp6.booleans[n]) {
                                                                            temp6.setChar(SubsAlfa.abc.charAt(n), cipherPart1.charAt(2));
                                                                            part = temp.decipherPart(cipherPart1);
                                                                            for (String t: dicionario) {
                                                                                if(s.startsWith(part) ){
                                                                                    temp7 = new SubsAlfa(temp.toString());
                                                                                    if(temp7.setCharFromString(t,cipher.substring(y))){
                                                                                        String s2 = temp7.maxContinuousString(cipher);
                                                                                        if (!palavras.contains(t)){
                                                                                            palavras.add(t);
                                                                                            alfabetos.add(temp3.toString());

                                                                                        }
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    void tentativa3(){
        // ir trocando t a, o, e
        sub.setChar('e', 't');
        sub.setChar('e', 'z');
        sub.setChar('o', 'u');
        temp = new SubsAlfa(sub.toString());

        String cipherPart = cipher.substring(cipher.indexOf("tiiz"), cipher.indexOf("tiiz")+4);
        System.out.println();
        System.out.println("Comeco iteracao separada "+ cipherPart);
        for (int i = 0; i < SubsAlfa.abc.length()  ; i++) {
            temp1 = new SubsAlfa(sub.toString());
            if(!temp1.booleans[i]){
                temp1.setChar(SubsAlfa.abc.charAt(i), cipherPart.charAt(0));
                for (int j = 0; j < SubsAlfa.abc.length()  ; j++) {
                    temp2 = new SubsAlfa(temp1.toString());
                    if(!temp2.booleans[j]) {
                        temp2.setChar(SubsAlfa.abc.charAt(j), cipherPart.charAt(1));
                        for (int k = 0; k < SubsAlfa.abc.length(); k++) {
                            temp = new SubsAlfa(temp2.toString());
                            if(!temp.booleans[k]) {
                                temp.setChar(SubsAlfa.abc.charAt(k), cipherPart.charAt(3));
                                part = temp.decipherPart(cipherPart);
                                for (String s: dicionario) {
                                    if(s.startsWith(part) ){
                                        temp3 = new SubsAlfa(temp.toString());
                                        if(temp3.setCharFromString(s,cipher.substring(cipher.indexOf("tiiz")))){
                                            String s1 = temp3.maxContinuousString(cipher);
                                                temp3.printCleanDecipher(cipher);
                                                System.out.println(s1);


                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }


        // ----------------------------------------------------------------------------------
    }

    /**
     * Uma das permutas da tentativa1.
     */
    void permuta1(){
        // ----------------------------------------------------------------------------------
        //T Z U -> O A E
        sub.setChar('o', 't');
        sub.setChar('a', 'z');
        sub.setChar('e', 'u');

        System.out.println();
        System.out.println("Comeco permuta1 T Z U -> O A E");
        for (int x =  0; x < 11; x++) {
            System.out.println("permuta1 iteracao " + x);
            cipherPart = cipher.substring(x, x + 3);
            for (int i = 0; i < SubsAlfa.abc.length(); i++) {
                temp1 = new SubsAlfa(sub.toString());
                if (!temp1.booleans[i]) {
                    temp1.setChar(SubsAlfa.abc.charAt(i), cipherPart.charAt(0));
                    for (int j = 0; j < SubsAlfa.abc.length(); j++) {
                        temp2 = new SubsAlfa(temp1.toString());
                        if (!temp2.booleans[j]) {
                            temp2.setChar(SubsAlfa.abc.charAt(j), cipherPart.charAt(1));
                            for (int k = 0; k < SubsAlfa.abc.length(); k++) {
                                temp3 = new SubsAlfa(temp2.toString());
                                if (!temp3.booleans[k]) {
                                    temp3.setChar(SubsAlfa.abc.charAt(k), cipherPart.charAt(2));
                                    part = temp3.decipherPart(cipherPart);
                                    for (String s : dicionario) {
                                        if (s.startsWith(part) ) {
                                            temp4 = new SubsAlfa(temp3.toString());
                                            if (temp4.setCharFromString(s, cipher.substring(x))) {
                                                temp4.printCleanDecipher(cipher);
                                                alfabetos.add(temp4.toString());

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

        sub.reset();
    }

    /**
     * Uma das permutas da tentativa1.
     */
    void permuta2(){
        // ----------------------------------------------------------------------------------

        //T Z U -> O E A
        sub.setChar('o', 't');
        sub.setChar('e', 'z');
        sub.setChar('a', 'u');

        System.out.println();
        System.out.println("Comeco permuta2 T Z U -> O E A");
        for (int x =  0; x < 11; x++) {
            System.out.println("permuta2 iteracao " + x);
            cipherPart = cipher.substring(x, x + 3);
            for (int i = 0; i < SubsAlfa.abc.length(); i++) {
                temp1 = new SubsAlfa(sub.toString());
                if (!temp1.booleans[i]) {
                    temp1.setChar(SubsAlfa.abc.charAt(i), cipherPart.charAt(0));
                    for (int j = 0; j < SubsAlfa.abc.length(); j++) {
                        temp2 = new SubsAlfa(temp1.toString());
                        if (!temp2.booleans[j]) {
                            temp2.setChar(SubsAlfa.abc.charAt(j), cipherPart.charAt(1));
                            for (int k = 0; k < SubsAlfa.abc.length(); k++) {
                                temp3 = new SubsAlfa(temp2.toString());
                                if (!temp3.booleans[k]) {
                                    temp3.setChar(SubsAlfa.abc.charAt(k), cipherPart.charAt(2));
                                    part = temp3.decipherPart(cipherPart);
                                    for (String s : dicionario) {
                                        if (s.startsWith(part) ) {
                                            temp4 = new SubsAlfa(temp3.toString());
                                            if (temp4.setCharFromString(s, cipher.substring(x))) {
                                                temp4.printCleanDecipher(cipher);
                                                alfabetos.add(temp4.toString());

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        sub.reset();

    }

    /**
     * Uma das permutas da tentativa1.
     */
    void permuta3(){
        // ----------------------------------------------------------------------------------

        //T Z U -> E A O
        sub.setChar('e', 't');
        sub.setChar('a', 'z');
        sub.setChar('o', 'u');

        System.out.println();
        System.out.println("Comeco permuta3 T Z U -> E A O");

        for (int x =  0; x < 11; x++) {
            System.out.println("permuta3 iteracao " + x);
            cipherPart = cipher.substring(x, x + 3);
            for (int i = 0; i < SubsAlfa.abc.length(); i++) {
                temp1 = new SubsAlfa(sub.toString());
                if (!temp1.booleans[i]) {
                    temp1.setChar(SubsAlfa.abc.charAt(i), cipherPart.charAt(0));
                    for (int j = 0; j < SubsAlfa.abc.length(); j++) {
                        temp2 = new SubsAlfa(temp1.toString());
                        if (!temp2.booleans[j]) {
                            temp2.setChar(SubsAlfa.abc.charAt(j), cipherPart.charAt(1));
                            for (int k = 0; k < SubsAlfa.abc.length(); k++) {
                                temp3 = new SubsAlfa(temp2.toString());
                                if (!temp3.booleans[k]) {
                                    temp3.setChar(SubsAlfa.abc.charAt(k), cipherPart.charAt(2));
                                    part = temp3.decipherPart(cipherPart);
                                    for (String s : dicionario) {
                                        if (s.startsWith(part) ) {
                                            temp4 = new SubsAlfa(temp3.toString());
                                            if (temp4.setCharFromString(s, cipher.substring(x))) {
                                                temp4.printCleanDecipher(cipher);
                                                alfabetos.add(temp4.toString());
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }


        sub.reset();


    }

    /**
     * Uma das permutas da tentativa1.
     */
    void permuta4(){
        // ----------------------------------------------------------------------------------

        //T Z U -> E O A
        sub.setChar('e', 't');
        sub.setChar('o', 'z');
        sub.setChar('a', 'u');

        System.out.println();
        System.out.println("Comeco permuta4 T Z U -> E O A");
        for (int x =  0; x < 11; x++) {
            System.out.println("permuta4 iteracao " + x);
            cipherPart = cipher.substring(x, x + 3);
            for (int i = 0; i < SubsAlfa.abc.length(); i++) {
                temp1 = new SubsAlfa(sub.toString());
                if (!temp1.booleans[i]) {
                    temp1.setChar(SubsAlfa.abc.charAt(i), cipherPart.charAt(0));
                    for (int j = 0; j < SubsAlfa.abc.length(); j++) {
                        temp2 = new SubsAlfa(temp1.toString());
                        if (!temp2.booleans[j]) {
                            temp2.setChar(SubsAlfa.abc.charAt(j), cipherPart.charAt(1));
                            for (int k = 0; k < SubsAlfa.abc.length(); k++) {
                                temp3 = new SubsAlfa(temp2.toString());
                                if (!temp3.booleans[k]) {
                                    temp3.setChar(SubsAlfa.abc.charAt(k), cipherPart.charAt(2));
                                    part = temp3.decipherPart(cipherPart);
                                    for (String s : dicionario) {
                                        if (s.startsWith(part) ) {
                                            temp4 = new SubsAlfa(temp3.toString());
                                            if (temp4.setCharFromString(s, cipher.substring(x))) {
                                                temp4.printCleanDecipher(cipher);
                                                alfabetos.add(temp4.toString());


                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

        sub.reset();


    }

    /**
     * Uma das permutas da tentativa1.
     */
    void permuta5(){
// ----------------------------------------------------------------------------------

        //T Z U -> A O E
        sub.setChar('a', 't');
        sub.setChar('o', 'z');
        sub.setChar('e', 'u');

        System.out.println();
        System.out.println("Comeco permuta5 T Z U -> A O E");
        for (int x =  0; x < 11; x++) {
            System.out.println("permuta5 iteracao " + x);
            cipherPart = cipher.substring(x, x + 3);
            for (int i = 0; i < SubsAlfa.abc.length(); i++) {
                temp1 = new SubsAlfa(sub.toString());
                if (!temp1.booleans[i]) {
                    temp1.setChar(SubsAlfa.abc.charAt(i), cipherPart.charAt(0));
                    for (int j = 0; j < SubsAlfa.abc.length(); j++) {
                        temp2 = new SubsAlfa(temp1.toString());
                        if (!temp2.booleans[j]) {
                            temp2.setChar(SubsAlfa.abc.charAt(j), cipherPart.charAt(1));
                            for (int k = 0; k < SubsAlfa.abc.length(); k++) {
                                temp3 = new SubsAlfa(temp2.toString());
                                if (!temp3.booleans[k]) {
                                    temp3.setChar(SubsAlfa.abc.charAt(k), cipherPart.charAt(2));
                                    part = temp3.decipherPart(cipherPart);
                                    for (String s : dicionario) {
                                        if (s.startsWith(part) ) {
                                            temp4 = new SubsAlfa(temp3.toString());
                                            if (temp4.setCharFromString(s, cipher.substring(x))) {
                                                temp4.printCleanDecipher(cipher);
                                                alfabetos.add(temp4.toString());
//
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }


        sub.reset();

    }

    /**
     * Uma das permutas da tentativa1.
     */
    void permuta6(){
        // ----------------------------------------------------------------------------------

        //T Z U -> A E O
        sub.setChar('a', 't');
        sub.setChar('e', 'z');
        sub.setChar('o', 'u');

        System.out.println();
        System.out.println("Comeco permuta6 T Z U -> A E O");

        for (int x =  0; x < 11; x++) {
            System.out.println("permuta6 iteracao " + x);
            cipherPart = cipher.substring(x, x + 3);
            for (int i = 0; i < SubsAlfa.abc.length(); i++) {
                temp1 = new SubsAlfa(sub.toString());
                if (!temp1.booleans[i]) {
                    temp1.setChar(SubsAlfa.abc.charAt(i), cipherPart.charAt(0));
                    for (int j = 0; j < SubsAlfa.abc.length(); j++) {
                        temp2 = new SubsAlfa(temp1.toString());
                        if (!temp2.booleans[j]) {
                            temp2.setChar(SubsAlfa.abc.charAt(j), cipherPart.charAt(1));
                            for (int k = 0; k < SubsAlfa.abc.length(); k++) {
                                temp3 = new SubsAlfa(temp2.toString());
                                if (!temp3.booleans[k]) {
                                    temp3.setChar(SubsAlfa.abc.charAt(k), cipherPart.charAt(2));
                                    part = temp3.decipherPart(cipherPart);
                                    for (String s : dicionario) {
                                        if (s.startsWith(part) ) {
                                            temp4 = new SubsAlfa(temp3.toString());
                                            if (temp4.setCharFromString(s, cipher.substring(x))) {
                                                temp4.printCleanDecipher(cipher);
                                                alfabetos.add(temp4.toString());

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

        sub.reset();
    }

    /**
     * Métodos onde é feito a recursão até atingir um certo número de caracteres. A recursão é feita a fim
     * de procurar palavras que se "encaixem" na cifra decifrada até o momento com o alfabeto de substituição criado.
     * Será feita 3 laços cada um indicando as primeiras 3 letras de uma possivel palavra, e em seguida e feita um ataque
     * de dicionario a fim de verificar se a palavra "encaiza", e será feita a chamada novamente para entrar em recursão.
     * @param inicio - int com posição de inicio, indica a posição na cifra
     * @param subsAlfa - String com o alfabeto de substituição
     * @return  String com alfabeto de substituição depois de ter atingido seu objetivo
     */
    String recursao(int inicio, String subsAlfa) {
        SubsAlfa temp5;
        SubsAlfa temp6;
        SubsAlfa temp7;
        SubsAlfa temp8;
        String cipherPart;
        String part;
        if (inicio > 50) {
            return subsAlfa;
        } else {
            for (int x = inicio; x < inicio + 3; x++) {
                cipherPart = cipher.substring(x, x + 3);
                for (int i = 0; i < SubsAlfa.abc.length(); i++) {
                    temp5 = new SubsAlfa(subsAlfa);
                    if (!temp5.booleans[i]) {
                        temp5.setChar(SubsAlfa.abc.charAt(i), cipherPart.charAt(0));
                        for (int j = 0; j < SubsAlfa.abc.length(); j++) {
                            temp6 = new SubsAlfa(temp5.toString());
                            if (!temp6.booleans[j]) {
                                temp6.setChar(SubsAlfa.abc.charAt(j), cipherPart.charAt(1));
                                for (int k = 0; k < SubsAlfa.abc.length(); k++) {
                                    temp7 = new SubsAlfa(temp6.toString());
                                    if (!temp7.booleans[k]) {
                                        temp7.setChar(SubsAlfa.abc.charAt(k), cipherPart.charAt(2));
                                        part = temp7.decipherPart(cipherPart);
                                        for (String s : dicionario) {
                                            if (s.startsWith(part) ) {
                                                temp8 = new SubsAlfa(temp7.toString());
                                                if (temp8.setCharFromString(s, cipher.substring(x))) {
                                                    return recursao(s.length() + x, temp8.toString());
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
            return null;
        }

    }
}
