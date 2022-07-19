<%@ page language="java" contentType="text/html; charset=UTF-8"   pageEncoding="UTF-8"%>
<%@ include file="./ssi.jsp" %>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title> guestDelete.jsp </title>
  <style type="text/css">
    *{font-size: 16pt; font-weight: bold; }
    a{ font-size: 16pt; color:green; text-decoration:none; }
	a:hover{ font-size:20pt; color:blue; text-decoration:underline; }
  </style>

  <script type="text/javascript">
  </script>
</head>
<body>
  <p style="margin-top:50px;">
  <div align="center" > 
   <h2> guestDelete.jsp - 삭제문서 </h2>
   <img src="images/tulips.png"> <br>
  </div> 
  
<%
 //request,response,out,page,session세션 내장객체
 String temp =(String)session.getAttribute("naver");
 if (temp==null || temp==""){
%>
	<script type="text/javascript">
		alert("삭제권한이 없습니다 로그인후 이용하세요");
		location.href="login.jsp";
	</script>
<%
 }else{
  String Gdata = request.getParameter("idx"); 
  msg="delete from guest where sabun = " + Gdata;
  ST = CN.createStatement();
  ST.executeUpdate(msg);
%>
 	<script type="text/javascript">
		alert("데이터삭제가 성공했습니다. 복귀작업은 안됩니다");
		location.href="guestList.jsp";
	</script>
<% } %>
<p> 
 %>
</body>
</html>