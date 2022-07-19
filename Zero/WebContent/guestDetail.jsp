<%@ page language="java" contentType="text/html; charset=UTF-8"   pageEncoding="UTF-8"%>
<%@ include file="./ssi.jsp" %>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title> guestDetail.jsp </title>

  <script type="text/javascript">
  </script>
</head>
<body>

<%
 String Gdata = request.getParameter("idx");
 
 ST=CN.createStatement();
 msg="select * from guest where sabun = " + Gdata ; 
 RS=ST.executeQuery(msg);
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

<p>
 <table width="900" border="1" cellspacing="0" cellpadding="7">
   <tr align="center">
    <td colspan="2">
        guestDetail.jsp  <br>
    	<font color=blue>[ <%= RS.getString("name") %>]님의 상세페이지</font> 
    </td>
   </tr>

   <tr>
   	 <td rowspan="5" align="center"> <img src="images/bbb.gif" width="300" height="250" >  </td>
   	 <td width="400"> 사번: <%= Gsabun %> </td> 
   </tr>  
   
   <tr>	<td> 제목: <%= Gtitle %>  </td>   </tr>
   <tr> <td> 날짜: <%= RS.getDate("wdate") %> </td>  </tr>    
   <tr> <td> 급여: <%= RS.getInt("pay") %> </td>    </tr>  
   <tr> <td> 메일: <%= RS.getString("email") %> </td>  </tr>  
   
   <tr align="center">
    <td colspan="2">
        <a href="guestEdit.jsp?idx=<%=Gsabun%>">[수정]</a>
    	<a href="guestWrite.jsp">[등록]</a>
    	<a href="guestDelete.jsp?idx=<%=Gsabun%>">[삭제]</a>
 		<a href="index.jsp">[index]</a>
 		<a href="guestList222.jsp">[전체출력222]</a>
    </td>
   </tr>
 </table>
 	
</body>
</html>








