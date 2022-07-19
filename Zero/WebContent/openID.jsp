<%@ page language="java" contentType="text/html; charset=UTF-8"   %>

<%@ include file="./ssi.jsp" %>
<!DOCTYPE html>
<html> <head>
<title> [openID.jsp]</title>
   <style type="text/css">
	  *{font-size:14pt; font-weight:bold;  font-family: Comic Sans MS ; margin-left: 10px; }
	  a{font-size:14pt; text-decoration:none; font-weight:bold; color:blue;  font-family: Comic Sans MS ; }
	  a:hover{font-size:16pt; text-decoration:underline; color:green;  font-family: Comic Sans MS ; }
   </style>
   
   <script type="text/javascript">
     function first(){
       open_form.userid.focus();
     }
   </script>
</head>
<body bgcolor="yellow" onLoad="first();">
 <%
  String Gdata = request.getParameter("idx");
  System.out.println("openID.jsp 넘어온idx=" +   Gdata );
%>	
<div>
  <img src="images/bar.gif" width=400><br>
	<form name="open_form" method="get" action="openIDSave.jsp">
	  userid:<input type="text" name="userid" size="10" value="<%=Gdata %>">
	         <input type="submit" value="중복처리">
	</form>
  <img src="images/bar.gif" width=400><br>
</div>
</body>
</html>



