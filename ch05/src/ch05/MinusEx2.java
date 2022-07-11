package ch05;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
public class MinusEx2 {
	public static void main(String[] args) throws ClassNotFoundException, SQLException {
		//Connection con = null;
		//Statement stmt = null;
		//ResultSet rs = null;
		// 드라이버 로딩
		try{Connection 	con=DriverManager.getConnection("jdbc:oracle:thin:@127.0.0.1:1521:xe", "scott", "tiger");
		Statement stmt = con.createStatement();
			Class.forName("oracle.jdbc.driver.OracleDriver");//forname문자열로 주어진 드라이버를 메모리에 올려줌
		//연결
		//쿼리문전달객체 생성
		//쿼리문 작성
			String sql = "SELECT EMPNO, ENAME, SAL, DEPTNO FROM EMP MINUS SELECT EMPNO, ENAME, SAL, DEPTNO FROM EMP WHERE DEPTNO = 10";
		//결과출력
		ResultSet rs=stmt.executeQuery(sql);//jdbx_>dbms 전송 후 실행 결과 리턴
		  while(rs.next()) {
			  System.out.println(rs.getInt(1) + ":" + rs.getString(2) + ":" + rs.getInt(3) + ":" + rs.getInt(4));
		}}
		catch(Exception e) {System.out.println(e.getMessage());}
		//finally {
			//다끝났으니까 자원해제(소스해제)
			//rs 전역변수 선언 필요, try 안에 들어가 있어서 finally로 닫을 필요 없음
		
			
		}
	}

