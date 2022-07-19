package ch05;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class Eddd {

	public static void main(String[] args) throws ClassNotFoundException, SQLException {
		// 드라이버 로딩
		Class.forName("oracle.jdbc.driver.OracleDriver");//forname문자열로 주어진 드라이버를 메모리에 올려줌
		// connection 객체생성 
		Connection con = DriverManager.getConnection("jdbc:oracle:thin:@127.0.0.1:1521:xe", "scott", "tiger");
		
		//쿼리문 작성
		String sql="SELECT * FROM EMP";
		
		
		//쿼리문 전송객체 생성
		Statement stmt = con.createStatement();
		ResultSet rs=stmt.executeQuery(sql);//jdbx_>dbms 전송 후 실행 결과 리턴

	
		//결과
		while (rs.next()) {}
		//다끝났으니까 자원해제(소스해제)
		rs.close();
		stmt.close();
		con.close();
	}

}