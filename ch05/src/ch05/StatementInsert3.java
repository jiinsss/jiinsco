package ch05;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;

public class StatementInsert3 {

	public static void main(String[] args) {
		Connection con = null;
		//Statement stmt= null;
		PreparedStatement pstmt= null;
		ResultSet rs = null;
		try {
			Class.forName("oracle.jdbc.driver.OracleDriver");//forname문자열로 주어진 드라이버를 메모리에 올려줌
			// connection 객체생성 
			 con = DriverManager.getConnection("jdbc:oracle:thin:@127.0.0.1:1521:xe", "scott", "tiger");
		     
			int deptno=30;
			
			String loc="제주";
			String sql="insert into dept loc=? where deptno=?";
			
			
			 //stmt = con.createStatement();
           // stmt.executeUpdate(sql);
            pstmt = con.prepareStatement(sql);
            pstmt.setInt(2,deptno);
         
            pstmt.setString(1,loc);
            int count=pstmt.executeUpdate();
                  
            System.out.println("sql:"+sql);
            if(count>0) {System.out.println("수정완료");
            }
			
			
		
         	}catch(Exception e){}
			finally{
				try{rs.close();
				pstmt.close();
				con.close();}
				catch(Exception e){}}
			

			
		}
		
		}

	

