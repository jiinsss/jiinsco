package ch05;

import java.sql.Connection;
import java.sql.DriverManager;

import java.sql.SQLException;


public class Eeee {

	public static void main(String[] args) throws ClassNotFoundException, SQLException {
		// 드라이버 로딩
		Class.forName("oracle.jdbc.driver.OracleDriver");//forname문자열로 주어진 드라이버를 메모리에 올려줌
		// connection 객체생성 
		Connection con = DriverManager.getConnection("jdbc:oracle:thin:@127.0.0.1:1521:xe", "scott", "tiger");
		if (con!=null) {
			System.out.println("성공");
	
		}
		else {
			System.out.println("성공");
		}
	}
}
		