<%@ page language="java" contentType="text/html; charset=UTF-8"   pageEncoding="UTF-8"%>
<%@ page import="java.util.Date"  %>
<%@ page import="java.sql.Connection" %>
<%@ page import="java.sql.DriverManager" %>
<%@ page import="java.sql.*" %>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title> </title>
  <style type="text/css">
    *{font-size: 16pt; font-weight: bold; }
    a{font-size: 16pt; color:blue; text-decoration: none; }
    a:hover{font-size: 20pt; color:green; text-decoration:underline; font-weight: bold; }
  </style>

</head>
<body>
 
<%!
  Connection CN = null ; //DB서버연결
  Statement ST = null ;  //명령어생성
  PreparedStatement PST = null; //명령어
  ResultSet RS = null ; //조회한결과값을 기억  select 쿼리문
 
  String msg  ;
  int Grn, Gsabun, Gpay, Ghit ; // Grn=행번호, 사번=code, 급여, 조회수 
  String Gname  ;
  String Gtitle ;
  java.util.Date  Gwdate  ;
  String Gemail  ;
  
  int Gtotal=0, Stotal=0, total=0 , GGtotal=0; 
  String Gdata;
  int Rcnt=0;
  
  //페이징+검색
  String pnum; //<a href="guestList.jsp?pageNum=14"> [14] </a>
  int pageNUM, pagecount;  
  int start, end;
  int startpage, endpage ;
  int tmp; 
 
  String sqry=" ";
  String skey="", sval="" ;
  String returnpage="";
%>   
  
<%
try{
  Class.forName("oracle.jdbc.driver.OracleDriver");
  String url="jdbc:oracle:thin:@127.0.0.1:1521:XE";
  CN=DriverManager.getConnection(url, "scott", "tiger");
  //System.out.println("오라클 db서버 연결 성공입니다 07-18-월요일"); //주석처리하세요
}catch(Exception ex){System.out.println("에러 " + ex); }
%>




