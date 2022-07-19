<%@ page language="java" contentType="text/html; charset=UTF-8"   pageEncoding="UTF-8"%>
<%@ include file="./ssi.jsp" %>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title> guestListCOPY1.jsp </title>
  <script type="text/javascript">
  </script>
</head>
<body>
 <h2> guestListCOPY1.jsp </h2>
<%
 msg = "select count(*) cnt from  guest " ;
 ST = CN.createStatement();
 RS = ST.executeQuery(msg);
 if(RS.next()==true){ Gtotal = RS.getInt("cnt"); }
%> 
 
 <table border="1" width="900" cellspacing="0">
  <tr align="right">
    <td colspan=6> 레코드갯수: <%= Gtotal %> &nbsp; &nbsp;</td>
  </tr>
  
  <tr bgcolor="yellow">
   <td>행번호</td> <td>사 번</td> <td>이 름</td> <td>제목</td> <td>날 짜</td> <td>조회수</td>
  </tr>
  

<%
 msg = "select * from  guest " ; //행번호없이 출력
 msg = "select rownum rn, sabun,name,title,wdate,pay, hit ,email from guest ";
 ST = CN.createStatement();
 RS = ST.executeQuery(msg); //select문장쿼리는 무조건 RS=executeQuery(select~)
 while(RS.next()==true) {
	 Grn = RS.getInt("rn") ;
	 Gsabun = RS.getInt("sabun");
	 Gtitle = RS.getString("title");
     Gwdate = RS.getDate("wdate") ;
%> 
  
  <tr>
   <td> <%= Grn %> </td>
   <td> <%= Gsabun %> </td>
   <td> <%= RS.getString("name") %>  </td>
   <td> <a href="guestDetail.jsp?idx=<%=Gsabun%>">  <%= Gtitle %> </a> </td>   
   <td> <%= Gwdate %> </td>
   <td> <%= RS.getInt("hit") %> </td>
  </tr>
  
 <% } %> 
 </table>
 
 <p>
 <a href="guestWrite.jsp">[guestWrite]</a>
 <a href="index.jsp">[index]</a>
 <a href="guestList.jsp">[guestList]</a>
</body>
</html>





