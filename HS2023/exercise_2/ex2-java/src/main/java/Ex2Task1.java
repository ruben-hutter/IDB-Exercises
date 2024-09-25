import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class Ex2Task1 {

    public static void main(String[] args) {
        try {
            Connection con = DriverManager.getConnection(
                    "jdbc:postgresql://localhost:54321/demo", "demo", "demo");
            Statement statement = con.createStatement();
            ResultSet res = statement.executeQuery("SELECT version()");
            res.next();
            System.out.println(res.getString(1));
        } catch (SQLException e) {
            e.printStackTrace();
        }

    }
}
