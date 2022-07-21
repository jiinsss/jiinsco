<%@ page language="java" contentType="text/html; charset=UTF-8"   pageEncoding="UTF-8"%>
<%@ taglib prefix="c"   uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title> [guestList.jsp] </title>
	<style type="text/css">
	  *{ font-size: 16pt;  }
	  a{ font-size: 16pt; text-decoration:none; color:blue ; font-family: Comic Sans MS; }
	  a:hover{ font-size: 16pt; text-decoration:underline; color:green ; font-family: Comic Sans MS; }
	</style>

	<script type="text/javascript">	
	  function clearText(){
		document.myform.keyword.value="";
		document.myform.keyword.focus();
	  }
	</script>
</head>
<body>

 <table width=900 border=1 cellspacing=0>
   <tr align="right">
  	<td colspan="4"> 전체레코드갯수: ${Gtotal} &nbsp;</td>
  </tr>
  
 	<tr bgcolor="pink">
 	  <td>사 번</td> <td>이 름</td> <td>제 목</td> <td>조회수</td>
 	</tr>
  
  <c:forEach var="bean" items="${LG}">
 	<tr>   
 		<td> ${bean.sabun} </td>
 		<td> ${bean.name} </td>
 		<td> <a href="guestDetail.do?seq=${bean.seq}"> ${bean.title} </a> </td>
 		<td> ${bean.hit}  </td>
 	</tr>	 
  </c:forEach>
 
  <tr align="center">
  	<td colspan="4"> </td>
  </tr>
  
  <tr align="center">
  	<td colspan="4">
  	  <form name="myform">
  	  	  검색 :     
  	  	 <select name="keyfield" onchange="clearText();">  
  	  	 	<option value="">-----선택하세요----- </option>
  	  	 	<option value="name"> 이름필드 </option>
  	  	 	<option value="title"> 제목필드 </option>
  	  	 	<option value=""> 내용필드 </option>
  	  	 	<option value=""> 전체출력 </option>
  	  	 </select>
  	  	 <input type="text" name="keyword" size=10>
  	  	 <input type="submit" value="검색">
  	  </form>
  	</td>
  </tr>
 </table>
 
    <p>
	<a href="/blog/main">[main]</a> 
	<a href="index.jsp">[index.jsp]</a> 
  	<a href="guestWrite.do">[guestWrite]</a>
  	<a href="guestList.do">[guestList]</a>
</body>
</html>











