package main.java.com.Listas;

import java.util.ArrayList;
import java.util.List;

public class AppListas {
    public static void main(String[] args) {
        List<String> listaDeConcursosQuePassei = new ArrayList<>();
        listaDeConcursosQuePassei.add("EBSERH - 2016");
        listaDeConcursosQuePassei.add("UFT -  2019");
        listaDeConcursosQuePassei.add("BRB - 2022");

        for (String concurso : listaDeConcursosQuePassei) {
            System.out.println(concurso);
        }

    }

}
