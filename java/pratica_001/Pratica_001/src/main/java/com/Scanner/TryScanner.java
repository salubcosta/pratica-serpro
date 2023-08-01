package main.java.com.Scanner;

import java.util.Scanner;

public class TryScanner {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Informe seu nome: ");
        String nome = scanner.nextLine();
        System.out.println("Seu nome é: " + nome);
        scanner.close();
    }
}
