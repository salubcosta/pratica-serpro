package testMain.rewrite;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class App {
    private static final String URL_DB = "jdbc:mysql://localhost:3306/pratica_01";
    private static final String USERNAME = "root";
    private static final String PASSWORD = "dbBar80%a$";

    public static void main(String[] args){
        new App();
    }

    public App(){
        try(var Conn = getConnection()){
            System.out.println("Connectado!");
        }catch(SQLException e){
            System.out.println("Falha ao conectar. Falha: " + e.getMessage());
        }
    }

    public Connection getConnection() throws SQLException{
        return DriverManager.getConnection(URL_DB, USERNAME, PASSWORD);
    }
}