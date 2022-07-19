package ch05;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;
public class TransactionEx01 {
	 public static void main(String[] args) throws ClassNotFoundException, SQLException {
	      Scanner scanner = new Scanner(System.in);
	      /* 드라이버 로딩 */
	      Class.forName("oracle.jdbc.driver.OracleDriver");
	      /* Connection 객체 생성 */ 
	      Connection con = DriverManager.getConnection("jdbc:oracle:thin:@127.0.0.1:1521:xe", "scott", "tiger");
	      //Manual commit으로 전화
	      con.setAutoCommit(false);//manual commit으로바꿈 오류난 부분 roll back으로 돌려주려고
	      System.out.println("이체할 금액>>");
	      int amount = scanner.nextInt();
	      /* 쿼리문 작성 */
	      String update1 = "update bank set balance = balance - " + amount + " where owner='홍길동'";
	      String update2 = "update bank set balance = balance - " + amount + " where owner='일지매'";
	      //update - executeUpdate() - 리턴결과 update된 행의 수
	        int count1=0, count2=0;
	      /* 쿼리문 전달객체 생성 */ 
	      Statement stmt = con.createStatement();
	      try {
	      count1 = stmt.executeUpdate(update1);
	      count2 = stmt.executeUpdate(update2);
	      if(count1 + count2 == 2) System.out.println("정상 이체 완료");   
	      con.commit(); // 정상인 경우 db 반영 처리
	   }catch (Exception e) {
	      System.out.println("이체 오류");
	      con.rollback(); // 롤백처리
	   }finally {
	      con.setAutoCommit(true);
	   }
	  }
	}
