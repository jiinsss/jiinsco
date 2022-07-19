package ch05;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class StatementEx01 {

	public static void main(String[] args) {
		Connection con = null;
		Statement stmt= null;
		ResultSet rs = null;
		try {
			Class.forName("oracle.jdbc.driver.OracleDriver");//forname문자열로 주어진 드라이버를 메모리에 올려줌
			// connection 객체생성 
			 con = DriverManager.getConnection("jdbc:oracle:thin:@127.0.0.1:1521:xe", "scott", "tiger");
		     stmt = con.createStatement();
			int deptno=30;
			String job="SALESMAN";
			
			String sql="select * from emp where deptno="+job+ "and job like'"+job+"'";
			System.out.println("sql"+sql);
			
			//ResultSet rs=stmt.executeQuery(sql);
			//execute sql 모를때
			boolean isResult = stmt.execute(sql);
			System.out.println();
			if(isResult){
				rs=stmt.executeQuery(sql);

			while(rs.next()) {
				  System.out.println(rs.getInt(1) + ":" + rs.getString(2) + ":" + rs.getInt("sal"));
			}}
			else{
				int Count = stmt.executeUpdate(sql);
				System.out.println(Count);
				}

			
		}
		catch(Exception e){}
		finally{
			try{rs.close();
			stmt.close();
			con.close();}
			catch(Exception e){}
		}

	}

}
