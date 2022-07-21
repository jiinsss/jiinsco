<%@ page language="java"   contentType="text/html; charset=UTF-8"    pageEncoding="UTF-8"  %>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title> [guestWrite.jsp] </title>
	<style type="text/css">
	  *{ font-size: 16pt;  }
	  a{ font-size: 16pt; text-decoration:none; color:blue ; font-family: Comic Sans MS; }
	  a:hover{ font-size: 16pt; text-decoration:underline; color:green ; font-family: Comic Sans MS; }
	</style>

	<script type="text/javascript">
	
	</script>
</head>
<body>
	<b> guestWrite.jsp </b> <p>
	<form  name="myform" action="guestInsert.do" >
		사번: <input type="text" name="sabun" > <br>
		이름: <input type="text" name="name" value="kim" > <br>
		제목: <input type="text" name="title" value="book"> <br>
		급여: <input type="text" name="pay"  value="97"> <br>
		메일: <input type="text" name="email" value="mo@it.net"> <br>
		    <input type="submit" value="guest부트저장"> &nbsp;
		    <input type="reset" value="입력취소">
	</form>
	
	<p>
	<a href="index.jsp">[index.jsp]</a> 
  	<a href="guestWrite.do">[guestWrite]</a>
  	<a href="guestList.do">[guestList]</a>
</body>
</html>






