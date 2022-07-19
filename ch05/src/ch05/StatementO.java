package ch05;
import java.sql.Statement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
/* JDBC 2.0 */
public class StatementO {
	 public static void main(String[] args) {
	      Connection con = null;
	      Statement stmt = null;
	      ResultSet rs = null;
     try {
	         Class.forName("oracle.jdbc.driver.OracleDriver");
	         con = DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe", "scott", "tiger");
	         stmt = con.createStatement(ResultSet.TYPE_SCROLL_SENSITIVE, ResultSet.CONCUR_UPDATABLE);
	         int deptno = 30;
	         String job = "SALESMAN";
	         String sql = "select * from emp where deptno=" + deptno + " and job like '" + job + "'";
	         System.out.println("sql:" + sql);
	         rs = stmt.executeQuery(sql);
	         while (rs.next()) {
	            System.out.println(rs.getInt(1) + ":" + rs.getString(2) + ":" + rs.getInt("sal"));
	         }
	         System.out.println("--------------------------------");
	         rs.absolute(2);
	         System.out.println(rs.getInt(1) + ":" + rs.getString(2) + ":" + rs.getInt("sal"));
	         System.out.println("--------------------------------");
	         rs.previous();
	         System.out.println(rs.getInt(1) + ":" + rs.getString(2) + ":" + rs.getInt("sal"));
	         System.out.println("--------------------------------");
	         rs.next();
	         System.out.println(rs.getInt(1) + ":" + rs.getString(2) + ":" + rs.getInt("sal"));
	         System.out.println("--------------------------------");
	         rs.first();
	         System.out.println(rs.getInt(1) + ":" + rs.getString(2) + ":" + rs.getInt("sal"));
	         System.out.println("--------------------------------");
	         rs.last();
	         System.out.println(rs.getInt(1) + ":" + rs.getString(2) + ":" + rs.getInt("sal"));
	         System.out.println("--------------------------------");
	      } catch (Exception e) {

	      } finally {
	         try {
	            rs.close();
	            stmt.close();
	            con.close();
	         } catch (Exception e) {
	         }
	      }
	   }
	}
