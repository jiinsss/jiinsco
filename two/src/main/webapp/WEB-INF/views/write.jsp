<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>


<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>write.jsp</title>
<!-- bootstrap 게시판용 -->
<link rel="stylesheet"
	href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css"
	integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk"
	crossorigin="anonymous">

<!-- include libraries(jQuery, bootstrap) -->
<link
	href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"
	rel="stylesheet">
<script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
<script
	src="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
<!-- include summernote css/js -->
<link
	href="https://cdn.jsdelivr.net/npm/summernote@0.8.18/dist/summernote.min.css"
	rel="stylesheet">
<script
	src="https://cdn.jsdelivr.net/npm/summernote@0.8.18/dist/summernote.min.js"></script>

<style type="text/css">
.container {
	width: 70%;
}

.id_form{
	padding-bottom : 10em;
}

.input-group {
	float: left;
}

.input-group-prepend {
	height: 34px;
	width: 200px;
	float: left;
}

.text_size {
	width: 200px;
	margin-left : -11em;
	float: left;
}

.text_size#text_title{
	width: 400px !important;
}
</style>
<script type="text/javascript">

	function userid_chk(){
		if(myform.userid.value == null || myform.userid.value == ""){
			alert("아이디를 입력하세요");
			myform.userid.focus();
			return false;
		} else{
			myform.name.focus();
			return true;
		}
	}//end


	function title_chk(){
		if(myform.title.value == null || myform.title.value == ""){
			alert("제목을 입력하세요");
			myform.title.focus();
			return false;
		} else {return true;}
	}//end

	
	function nullCheck(){
		if(confirm('저장하시겠습니까?') == true) {
		  if(!(userid_chk() && title_chk()) == false )	
			  document.myform.submit();
		}
		
	}//end
</script>
</head>
<body>

<div class="container">
  <p> <h2> 양지인 spring boot 글쓰기 </h2> </p>

   <form name="myform" action="">
	<div class="id_form">
		<div class="input-group mb-3">
			<div class="input-group-prepend">
				<span class="input-group-text" id="inputGroup-sizing-default">아이디</span>
			</div>
			<div class="text_size">
				<input type="text" class="form-control" name="userid" 
					aria-label="Sizing example input"
					aria-describedby="inputGroup-sizing-default">
			</div>
			</div>
			
			<div class="input-group mb-3">
			<div class="input-group-prepend">
				<span class="input-group-text" id="inputGroup-sizing-default">이 &nbsp; 름</span>
			</div>
			<div class="text_size">
				<input type="text" class="form-control" name="name"
					aria-label="Sizing example input"
					aria-describedby="inputGroup-sizing-default">
			</div>
			</div>
			
			<div class="input-group mb-3">
			<div class="input-group-prepend">
				<span class="input-group-text" id="inputGroup-sizing-default">제 &nbsp; 목</span>
			</div> 
			<div class="text_size" id="text_title">
				<input type="text" class="form-control" name="title"
					aria-label="Sizing example input"
					aria-describedby="inputGroup-sizing-default">
			</div>
		</div>
    </div>
		

	<textarea id="summernote" name="detail"></textarea>
		<script>
			$(document).ready(function() {
				$('#summernote').summernote({
					placeholder : '텍스트를 입력하세요.',
					tabsize : 2,
					height : 300
				});
			});
		</script>
	
		<p class="text-right">
			<button type="button" class="btn btn-outline-primary"  onclick="nullCheck();">글올리기</button>
			<button type="button" class="btn btn-outline-primary" 	onclick="location.href=''">목록으로</button>
			<button type="button" class="btn btn-outline-primary" 	onclick="location.href='index.jsp'">index</button>
		</p>
   </form>
</div>

</body>
</html>