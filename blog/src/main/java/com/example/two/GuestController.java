package com.example.two;
import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;


@Controller
public class GuestController {

	@RequestMapping("/mylist.komi")
	public String guest_list() {
		return "guestList" ;
	}//end
	@RequestMapping("/mywrite.komi")
	public String guest_write() {
		return "guestwrite" ;
	}//end
	
	@RequestMapping("/guestInsert.do")
	public void guest_insert(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
	      
		response.setContentType("text/html; charset=UTF-8");
	    PrintWriter out = response.getWriter();
	    int Gsabun = Integer.parseInt( request.getParameter("sabun") );
	    String Gname =  request.getParameter("name") ;
	    String Gtitle = request.getParameter("title") ;
	    int Gpay = Integer.parseInt( request.getParameter("pay") );
	    String  Gemail = request.getParameter("email") ;
	    System.out.println(Gsabun+" " + Gname+" " + Gtitle+" " + Gpay+ " " + Gemail);
	    out.println(Gsabun+" " + Gname+" " + Gtitle+" " + Gpay+ " " + Gemail);
	      
	    return;  //guestWrite.jsp에서 작성된 값 넘기는거 받아오기
	  }//end

	
}//class END
