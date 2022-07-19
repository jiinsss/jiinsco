package ch04;

import java.sql.Connection;
import java.sql.DriverManager;

//이게 싱크론 방식-> getinstace()로 객체를 빌려 사용한 후 반납하는것 (주소가 다 같다)
//그 반대가 멀티톤 방시 new생성자()로 힙에 여러개 만듬(주소가 다 다르다)
public class OracleDAO {
	public static OracleDAO instance=new OracleDAO(); //static영역에 초기화 시켜서 올라갔는데 new로ㄴㄴ 안되고 get instance로 가져올 수 있다
	
//new oracledao로는 샌성 불가 private로 만들어서
private OracleDAO() {}

public static OracleDAO getInstance() {
	return instance;}

public static Connection getConnection() {
	Connection con =null;
	try {Class.forName("oracle.jdbc.driver.OracleDriver");
	con = DriverManager.getConnection("jdbc:oracle:thin:@127.0.0.1:1521:xe", "scott", "tiger");
	}
	catch(Exception e){  e.printStackTrace();}
	
return con;
}

}


