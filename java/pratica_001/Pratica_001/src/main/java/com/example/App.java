package main.java.com.example;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;


public class App {
    private static final String PASSWORD = "###";
    private static final String USERNAME = "root";
    private static final String JDBC_URL = "jdbc:mysql://127.0.0.1:3306/pratica_01";
    public static void main(String[] args) throws Exception {
        new App();
    }

    public App(){
        try(var conn = getConnection()){
            System.out.println("Conectado ao MySQL!");
        } catch (SQLException e){
            System.out.println("Não foi possível conectar ao banco de dados. Falha: " + e.getMessage());
        }
    }

    private Connection getConnection() throws SQLException {
        return DriverManager.getConnection(JDBC_URL, USERNAME, PASSWORD);
    }
}
