package ch03;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class WhereExec01 {

	public static void main(String[] args) throws ClassNotFoundException, SQLException {
		Class.forName("oracle.jdbc.driver.OracleDriver");
		Connection con = DriverManager.getConnection("jdbc:oracle:thin:@127.0.0.1:1521:xe", "scott", "tiger");
		Statement stmt = con.createStatement();
	    ResultSet rs = stmt.executeQuery("SELECT * FROM EMP WHERE DEPTNO=30");
	    while(rs.next()) {
	    	System.out.println(rs.getInt(1)+":"+rs.getString(2)+":"+rs.getInt("sal"));}//인덱스기억 안나면걍 칼럼명으로
	    rs.close();
	    stmt.close();
	    con.close();

	}

}
