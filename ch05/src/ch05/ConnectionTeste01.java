package ch05;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class ConnectionTeste01 {

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
		
		//쿼리문 작성
		String sql="SELECT * FROM EMP";
		//쿼리문 전송객체 생성
		Statement stmt = con.createStatement();
		
		ResultSet rs=stmt.executeQuery(sql);//jdbx_>dbms 전송 후 실행 결과 리턴
		
		//System.out.println("empno \t ename \t job \t mgr \t hiredate \t sal \t comm \t deptno");

		//while(rs.next()) {
			
		//결과셋에서 정수 추출 getint("칼럼명"), 실수getdouble() 문자열 getStirng("칼럼명")
		//날짜 getDate("칼럼명"),날짜 getString("칼럼명")
			//System.out.println(rs.getInt("empno"));//empno만 뽑겠다
			//int seq=1;//
			//int empno,mgr,sal,comm,deptno;
			//String ename,job,hiredate;
			//empno=rs.getInt("empno");//getint()안에 칼럼명이나 db의 인덱스 삽입 가능 db 인덱스는 1부터시작
			//ename=rs.getString("ename");//혹은 seq++를 입력해 증감 연산자로도 표현가능
			//job=rs.getString("job");
			//mgr=rs.getInt("mgr");
			//hiredate=rs.getString("hiredate");
			//sal=rs.getInt("sal");
			//comm=rs.getInt("comm");
			//deptno=rs.getInt("deptno");
			//System.out.println(empno+"\t"+ename+"\t"+ job +"\t"+mgr+"\t"+hiredate+"\t"+sal+"\t"+comm+"\t"+deptno);

		
		//}
		while (rs.next()) {}
		//다끝났으니까 자원해제(소스해제)
		rs.close();
		stmt.close();
		con.close();
	}

}
