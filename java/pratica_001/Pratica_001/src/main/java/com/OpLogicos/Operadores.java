package main.java.com.OpLogicos;

public class Operadores {
    boolean a(boolean valor) {
        System.out.println("a");
        return valor;
    }

    boolean b(boolean valor) {
        System.out.println("b");
        return valor;
    }

    boolean c(boolean valor) {
        System.out.println("c");
        return valor;
    }

    Operadores() {
        /**
         * Aplicação prática de short-circuit
         */
        System.out.println(a(true) || b(true) && c(true));
    }

    public static void main(String[] args) {
        new Operadores();
    }
}