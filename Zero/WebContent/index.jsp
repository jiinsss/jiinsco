<%@ page language="java" contentType="text/html; charset=UTF-8"   pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title> [index.jsp] </title>
  <script type="text/javascript">
    setTimeout("location.href='guestList.jsp'" , 3000) ;
  </script>
  
  <style type="text/css">
    #pline { margin-top: 50px;}
    *{font-size: 16pt; font-weight: bold; }
    a{font-size: 16pt; color:blue; text-decoration: none; }
    a:hover{font-size: 20pt; color:green; text-decoration:underline; font-weight: bold; }
  </style>
</head>
<body>
 <p id="pline">
 <div align="center">
 	<font size=6  color="blue"> <b>index.jsp시작페이지 </b></font><p>
 	
 	<video  width="600" autoplay  muted  loop  controls="controls">
 	  <source src="images/scuba.mp4" type="video/mp4" />
 	</video>
 	 <br>
 	 <a href="guestWrite.jsp">[guestWrite]</a>
 	 <a href="index.jsp">[index]</a>
 	 <a href="guestList.jsp">[guestList]</a>
 </div>
 
 

</body>
</html>






