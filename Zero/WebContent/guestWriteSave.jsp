<%@ page language="java" contentType="text/html; charset=UTF-8"  pageEncoding="UTF-8" %>
<%@ include file="./ssi.jsp" %>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title> guestWriteSave.jsp </title>
  <script type="text/javascript">
  </script>
</head>
<body>
 <h2> guestWriteSave.jsp - 단독실행금지 </h2>

 <%
   //데이터값을 받을때 request내장객체, 페이지이동 response내장객체, 웹화면에출력 out내장객체
   Gsabun = Integer.parseInt( request.getParameter("sabun") );
   Gname =  request.getParameter("name") ;
   Gtitle = request.getParameter("title") ;
   Gpay = Integer.parseInt( request.getParameter("pay") );
   Gemail = request.getParameter("email") ;
      
   msg="insert into guest values("+Gsabun+", '"+ Gname+"', '"+Gtitle+"', sysdate,"+ Gpay +", 0, '" +Gemail+"')" ;
   
   ST=CN.createStatement(); //CN참조해서 명령어 ST생성
   int ok = ST.executeUpdate(msg);
   if(ok>0){System.out.println(Gsabun + "데이터 guest저장 성공"); }
   
   out.println("<br>");
   out.println(msg); 
   System.out.println(msg); 
   
   //페이지이동담당 내장객체 response
   response.sendRedirect("guestList.jsp");
 %>	
 
 <p>
 <a href="guestWrite.jsp">[guestWrite]</a>
 <a href="index.jsp">[index]</a>
 <a href="guestList.jsp">[guestList]</a>
</body>
</html>




