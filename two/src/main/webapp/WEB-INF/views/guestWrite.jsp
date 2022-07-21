<%@ page language="java" contentType="text/html; charset=UTF-8"   pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title> guestWrite.jsp </title>
  <style type="text/css">
    *{font-size: 16pt; font-weight: bold; }
    a{font-size: 16pt; color:blue; text-decoration: none; }
    a:hover{font-size: 20pt; color:blue; text-decoration:underline; }
  </style>

  <script type="text/javascript">
    flag = false; //전역변수 
    
    function nullCheck(){
      var data = document.myform.sabun.value;
      var nick = document.myform.name.value;
      if(data==null || data ==""){
    	 alert("사번데이터가 공백입니다") ;
    	 myform.sabun.focus();
    	 return false; //아래문장처리안함 
      }else{ myform.name.focus(); }
      
      if(nick==null || nick==""){
    	  alert("이름데이터가 공백입니다");
    	  myform.name.focus();
    	  return false; //아래문장처리안함 
      }else{ myform.title.focus();}
      
      //공백이 아니니까 등록가능한 문서 action=guestWriteSave.jsp넘어가야죠
      if(flag==false){
    	alert("아이디중복체크 먼저 하세요 ") ;
      }else{ document.myform.submit(); }
    }//end
    
    
    function idCheck(){ 
      flag = true;
      var data = document.myform.sabun.value;
      if(data==null || data ==""){
       	 alert("중복체크 사번데이터가 공백입니다") ;
       	 myform.sabun.focus();
       	 return false; 
      } 
      //window개체 open(파일, 표시, "크기위치")
      window.open("openID.jsp?idx="+data, "bb", "width=500,height=120,left=300,top=200")
    }//end
   
  </script>
</head>
<body>
  <h2> guestWrite.jsp 입력화면 </h2>
	
  <form  name="myform" method="post"  action="">
    사번:<input type="text" name="sabun" size="10" maxlength="4" > 
        <input type="button" onClick="idCheck()" value="아이디중복">    <br>
    이름:<input type="text" name="name" value="hong"> <br>
    제목:<input type="text" name="title" value="komi"> <br>
    급여:<input type="text" name="pay"  value="56"> <br>
    메일:<input type="text" name="email" value="do@it.org" > <br>
      <input type="submit"   value="스프링등록하기">
      <input type="reset" value="입력취소">
  </form>
	
 <br>
 <a href="#">[등록]</a>
 <a href="#">[index]</a>
 <a href="#">[전체출력]</a>
 <p><br>
</body>
</html>




