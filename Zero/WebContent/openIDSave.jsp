<%@ page language="java" contentType="text/html; charset=UTF-8"   pageEncoding="UTF-8" %>         
<%@ include file="./ssi.jsp" %>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title> [openIDSave.jsp] </title>
</head>
<body bgcolor="yellow">

  <div align="center"> 
   <img src="images/bar.gif" width="350"> <br>
   <img src="images/bar.gif" width="350"> <br>
  </div> 
  
 <%
 //openIDSave.jsp
  Gdata = request.getParameter("userid");
  msg="select count(*) as cnt from guest where sabun = " + Gdata;
  ST=CN.createStatement();
  RS=ST.executeQuery(msg);
  if(RS.next()==true){ Gtotal=RS.getInt("cnt");}
  if( Gtotal>0){
%>	 
  <script type="text/javascript">
  	 alert("<%=Gdata%> 데이터는 이미 사용중입니다");
  	 location.href='openID.jsp?idx='+"" ;
  	 //opener.myform.sabun.value="";  
  	 //opener.myform.sabun.focus();
  	 //self.close();
  </script>	 
<%	 
 }else{
%>	 
  <script type="text/javascript">
     alert("<%=Gdata%> 데이터는 사용가능한 사번아이디 입니다");
     opener.myform.sabun.value=<%=Gdata%> ;
     opener.myform.name.focus();
     self.close();
  </script>	 
<%}%>	
</body>
</html>









