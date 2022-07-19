package ch03;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

public class WhereExec02 {

	public static void main(String[] args) throws ClassNotFoundException, SQLException {
		Class.forName("oracle.jdbc.driver.OracleDriver");
		Connection con = DriverManager.getConnection("jdbc:oracle:thin:@127.0.0.1:1521:xe", "scott", "tiger");
		Statement stmt = con.createStatement();
		//스캐너 객체 생성
		Scanner scanner = new Scanner(System.in);
		System.out.println("이름");
		String ename= scanner.next();
		String sql ="SELECT * FROM EMP WHERE ename ='"+ename+"' " ; // string일떄는 '"값" '
		System.out.println("생성된거"+sql);
		ResultSet rs=stmt.executeQuery(sql);

	    while(rs.next()) {
	    	System.out.println(rs.getInt(1)+":"+rs.getString(2)+":"+rs.getInt("sal"));}//인덱스기억 안나면걍 칼럼명으로
	    rs.close();
	    stmt.close();
	    con.close();

	}

}