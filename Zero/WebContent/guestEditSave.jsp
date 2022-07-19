<%@ page language="java" contentType="text/html; charset=UTF-8"  pageEncoding="UTF-8" %>
<%@ include file="./ssi.jsp" %>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title> guestEditSave.jsp </title>
  <script type="text/javascript">
  </script>
</head>
<body>
 <h2> guestEditSave.jsp - 단독실행금지 </h2>

 <%
   Gsabun = Integer.parseInt( request.getParameter("sabun") );
   Gname =  request.getParameter("name") ;
   Gtitle = request.getParameter("title") ;
   Gpay = Integer.parseInt( request.getParameter("pay") );
   Gemail = request.getParameter("email") ;
      
   //이름,제목,급여,메일 변경가능
   msg="update guest set name='" +Gname+"', title='"+Gtitle+"', pay="+Gpay +", email='" +Gemail+"' where  sabun = "+ Gsabun ;
   //update guest set name='Tkim', title='Tsum', pay=345, email='Ta@kk.com' where sabun=7788
   out.println(msg);
   
   ST=CN.createStatement(); //ST생성함 진짜 수정처리는 안함
   int ok = ST.executeUpdate(msg); //진짜 수정처리는 완료
   
   //페이지이동담당 내장객체 response
   response.sendRedirect("guestList.jsp");
 %>	
 
 <p>
 <a href="guestWrite.jsp">[guestWrite]</a>
 <a href="index.jsp">[index]</a>
 <a href="guestList.jsp">[guestList]</a>
</body>
</html>




