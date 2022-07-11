package ch02;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import ch05.ExecQueryEx;

public class SQLExec3 {

   public static void main(String[] args) throws SQLException {
      
      ExecQueryEx q1 = new ExecQueryEx();
      Connection con = q1.getConnection();
      String sql = "SELECT * FROM EMP ORDER BY DEPTNO ASC, SAL DESC";
      Statement stmt = con.createStatement();
      ResultSet rs = stmt.executeQuery(sql);

      while(rs.next()) {
         
         System.out.println(rs.getInt("empno") + ":" + rs.getString("ename") + ":" + rs.getInt("sal"));
         
      }
      
      q1.close(con, stmt, rs);
   }

}