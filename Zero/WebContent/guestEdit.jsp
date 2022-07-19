<%@ page language="java" contentType="text/html; charset=UTF-8"   pageEncoding="UTF-8"%>
<%@ include file="./ssi.jsp" %>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title> guestEdit.jsp </title>

  <script type="text/javascript">
  </script>
</head>
<body>

 <%
   String Gdata = request.getParameter("idx");
   System.out.println("guestEdit.jsp문서 넘어온 idx=" + Gdata);  

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
<!--  guestEdit.jsp 데이터수정하는 화면 페이지  -->
 <form  name="myform" method="get"  action="guestEditSave.jsp">
    수정사번:<input type="text" name="sabun" value="<%=Gsabun%>" readonly> <br>
    수정이름:<input type="text" name="name" value="<%=Gname%>"> <br>
    수정제목:<input type="text" name="title" value="<%=Gtitle%>"> <br>
    수정급여:<input type="text" name="pay"  value="<%=Gpay%>"> <br>
    수정메일:<input type="text" name="email" value="<%=Gemail%>" > <br>
      <input type="submit"  value="서브밋수정하기">
      <input type="reset" value="수정취소">
 </form>
 
 <p>
 <a href="guestWrite.jsp">[guestWrite]</a>
 <a href="index.jsp">[index]</a>
 <a href="guestList.jsp">[guestList]</a>	
</body>
</html>