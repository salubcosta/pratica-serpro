package main.java.com.tipos;

import java.util.Arrays;

public class Tipos {

    public static void main(String[] args){
        System.out.println("Minha aplicação Java\n");

        // Inteiro e Double
        int idade = 31;
        double peso = 80.5;

        System.out.println("Idade: " + idade + "\nPeso: " + peso);
        System.out.printf("Idade: %d Peso: %.2f", idade, peso);

        // Char e Boolean
        char sexo = 'M';
        boolean necessidadesEspeciais = false;
        
        System.out.println("\nSexo: " + sexo);
        System.out.println("Tem necessidades especiais: " + (necessidadesEspeciais ? "Sim!": "Não!"));

        // Vetor

        int[] vetorDeInt = {0, 1, 2, 3, 4, 5};

        //  Lendo vetor
        for (var vet : vetorDeInt){
            System.out.println(vet);
        }
        for (int i : vetorDeInt) {
            System.out.println(i);
        }
        System.out.println(Arrays.toString(vetorDeInt));

        int[] vetor3 = new int[4];
        for (int i = 0; i < vetor3.length; i++) {
            vetor3[i] = 100 * (i+1);
        }
        System.out.println(Arrays.toString(vetor3));

        // Matriz
        System.out.println("Matriz:");

        double[][] matriz = {{0,1,2,3},{4,5,6,7}};
        System.out.println(Arrays.toString(matriz[0]));
        System.out.println(Arrays.toString(matriz[1]));

        double[][] matriz2 = new double[2][3];

        for (int i = 0; i < matriz2.length; i++) {
            for (int j = 0; j < matriz2[i].length; j++) {
                matriz2[i][j] = i * matriz2[i].length+j;
            }
        }

        for (int i = 0; i < matriz2.length; i++) {
            for (int j = 0; j < matriz2[i].length; j++) {
                System.out.print(matriz2[i][j] + " ");
            }
            System.out.println();
        }


    }
}