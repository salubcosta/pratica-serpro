import java.sql.*;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("CRUD em JAVA");
        new App();
    }

    public App() {
        try (var conn = this.getconnection()) {
            System.out.println("Conectado!");
            // this.createAluno(conn, "Karolina", "karol.karol@hotmail.com", 1);
            // this.updateAluno(conn, "Karolina K.", "karol.k10", 1, 20);
            // this.desativarAluno(conn, false, 20);
            // this.desativarAluno(conn, true, 20);
            this.readAlunos(conn);
        } catch (SQLException e) {
            System.out.println("Falha: " + e.getMessage());
        }
    }

    private Connection getconnection() throws SQLException {
        return DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/python_udemy", "root", "dbBar80%a$");
    }

    public void createAluno(Connection conn, String nome, String email, int status) throws SQLException {
        try {
            String sql = "INSERT INTO alunos (nome, email, status) VALUES (?,?,?)";
            PreparedStatement preparedStatement = conn.prepareStatement(sql);
            preparedStatement.setString(1, nome);
            preparedStatement.setString(2, email);
            preparedStatement.setInt(3, status);
            preparedStatement.executeUpdate();
            System.out.println("Aluno cadastrado com sucesso!");
        } catch (SQLException e) {
            System.err.println("Falha ao cadastrar novo aluno!");
            e.printStackTrace();
        }
    }

    public void readAlunos(Connection conn) throws SQLException {
        try {
            String sql = "SELECT * FROM alunos;";
            Statement statement = conn.createStatement();
            ResultSet resultSet = statement.executeQuery(sql);
            while (resultSet.next()) {
                int id = resultSet.getInt("id");
                String nome = resultSet.getString("nome");
                String email = resultSet.getString("email");
                int status = resultSet.getInt("status");
                System.out.println("ID: " + id + ", Nome: " + nome + ", Email: " + email + ", Status: " + status);
            }
        } catch (SQLException e) {
            System.err.println("Falha ao buscar alunos!");
            e.printStackTrace();
        }
    }

    public void updateAluno(Connection conn, String nome, String email, int status, int id) throws SQLException {
        try {
            String sql = "update alunos set nome=?, email=?, status=? where id=?;";
            PreparedStatement preparedStatement = conn.prepareStatement(sql);
            preparedStatement.setString(1, nome);
            preparedStatement.setString(2, email);
            preparedStatement.setInt(3, status);
            preparedStatement.setInt(4, id);
            preparedStatement.executeUpdate();
            System.out.println("Aluno atualizado com sucesso!");
        } catch (SQLException e) {
            System.err.println("Falha ao atualizar Aluno!");
            e.printStackTrace();
        }
    }

    public void desativarAluno(Connection conn, boolean withDelete, int id) throws SQLException {
        try {
            String sql = withDelete ? "DELETE FROM ALUNOS WHERE id=?" : "UPDATE ALUNOS SET STATUS = 0 WHERE ID=?";
            PreparedStatement preparedStatement = conn.prepareStatement(sql);
            preparedStatement.setInt(1, id);
            preparedStatement.executeUpdate();
            System.out
                    .println(withDelete ? "Aluno desativado e excluído com sucesso!" : "Aluno desativado com sucesso!");
        } catch (SQLException e) {
            System.err.println("Falha ao excluir registro!");
            e.printStackTrace();
        }
    }
}
