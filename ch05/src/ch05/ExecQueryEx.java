package ch05;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class ExecQueryEx {
   static { // static 초기화 static {}
      try {
         Class.forName("oracle.jdbc.driver.OracleDriver");
      } catch (ClassNotFoundException e) {
         e.printStackTrace();
      }

   }

   static public Connection getConnection() {
      Connection con = null;
      try {
         con = DriverManager.getConnection("jdbc:oracle:thin:@127.0.0.1:1521:xe", "scott", "tiger");

      } catch (SQLException e) {
         e.printStackTrace();
      }
      return con;
   }

   public void close(Connection con, Statement stmt, ResultSet rs) {
      try {
         rs.close();
         stmt.close();
         con.close();
      } catch (SQLException e) {
         e.printStackTrace();
      }
      
   }

}
