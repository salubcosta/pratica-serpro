package main.java.com.eleitor;

import java.time.LocalDate;

public class Cidadao {
    private LocalDate dataNascimento;

    public LocalDate getDataNascimento() {
        return this.dataNascimento;
    }

    public void setDataNascimento(LocalDate dataNascimento) {
        this.dataNascimento = dataNascimento;
    }

    public int idade() {
        return LocalDate.now().getYear() - getDataNascimento().getYear();
    }

    public String eleitor() {
        int idade = idade();
        if (idade < 16) {
            return "Não é eleitor!";
        } else if (idade > 15 && idade < 18 || idade > 70) {
            return "Eleitor facultativo";
        } else {
            return "Eleitor obrigatório";
        }
    }
}
