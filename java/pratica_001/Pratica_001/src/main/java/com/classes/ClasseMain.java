package main.java.com.classes;

public class ClasseMain {
    public static void main(String[] args) {

        Cliente cliente = new Cliente();

        cliente.setRenda(10000);
        cliente.setSexo('M');
        cliente.setAnoNascimento(1991);

        System.out.println("Renda: " + cliente.getRenda());
        System.out.println("Sexo: " + cliente.getSexo());
        System.out.println("Ano de Nasc.: " + cliente.getAnoNascimento());
    }
}
