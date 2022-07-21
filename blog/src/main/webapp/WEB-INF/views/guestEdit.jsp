
<%@ page language="java"
         contentType="text/html; charset=UTF-8"   
         pageEncoding="UTF-8"  %>


<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title> [guestEdit.jsp] </title>
	<style type="text/css">
	  *{ font-size: 16pt;  }
	  a{ font-size: 16pt; text-decoration:none; color:blue ; font-family: Comic Sans MS; }
	  a:hover{ font-size: 16pt; text-decoration:underline; color:green ; font-family: Comic Sans MS; }
	</style>

	<script type="text/javascript">
	
	</script>
</head>
<body>
	guestEdit.jsp <p>
	<form  name="myform" action="guestEdit.do" >
		사번: <input type="text" name="sabun"  value="${dto.sabun}"> <br>
		이름: <input type="text" name="name" value="${dto.name}" > <br>
		제목: <input type="text" name="title" value="${dto.title}"> <br>
		급여: <input type="text" name="pay"  value="${dto.pay}"> <br>
		메일: <input type="text" name="email" value="${dto.email}"> <br>
		    <input type="submit" value="guest수정"> &nbsp;
		    <input type="reset" value="입력취소">
	</form>
	
	<p>
	<a href="index.jsp">[index.jsp]</a> 
  	<a href="guestWrite.do">[guestWrite]</a>
  	<a href="guestList.do">[guestList]</a>
</body>
</html>






