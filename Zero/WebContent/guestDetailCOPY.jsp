<%@ page language="java" contentType="text/html; charset=UTF-8"   pageEncoding="UTF-8"%>
<%@ include file="./ssi.jsp" %>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title> guestDetailCOPY.jsp </title>

  <script type="text/javascript">
  </script>
</head>
<body>
<h2> guestDetailCOPY.jsp - 상세문서 복사본 </h2>
<%
 String data = request.getParameter("idx"); 
 msg = "select * from guest  where sabun  =  " + data ;
 System.out.println(msg);
 
 ST = CN.createStatement();
 RS = ST.executeQuery(msg);
 if(RS.next()==true){
   Gsabun = RS.getInt("sabun");
   Gname = RS.getString("name");
   Gtitle = RS.getString("title");
   Gwdate = RS.getDate("wdate") ; 
   Gpay  = RS.getInt("pay");
   Ghit  = RS.getInt("hit");
   Gemail = RS.getString("email");
 }
%>
  사번 <%= Gsabun %> <br>
  이름 <%= Gname %> <br>
  제목 <%= Gtitle %> <br>
  날짜 <%= Gwdate %> <br>
  급여 <%= Gpay %> <br>
  조회수 <%= Ghit %> <br>
  이메일 <%= Gemail %> <p>
  

  <img src="images/bar.gif"><br>
  <img src="images/bar.gif"><br>
 <p>
 <a href="guestWrite.jsp">[guestWrite]</a>
 <a href="index.jsp">[index]</a>
 <a href="guestList.jsp">[guestList]</a>
</body>
</html>





