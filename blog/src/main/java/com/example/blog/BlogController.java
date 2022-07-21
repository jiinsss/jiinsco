package com.example.blog;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;


@Controller
public class BlogController {
	
	//http://localhost:8099/
	@RequestMapping("/")
	public @ResponseBody String home() {
	  return "<font color=blue size=6> <b> Spring Summer Winter </b></font><p>"; 
	}//end

	
	// http://localhost:8099/blog/main
	@RequestMapping("/blog/main")
	public String boardMain() { 
	   return "main" ;   
	   //2초후 guest입력란화면으로이동 http://localhost:8099/guest.do
    }
	
	
	// http://localhost:8099/blog/index
	@RequestMapping("/blog/index")
	public String boardIndex() { 
	   return "index" ;
	  //2초후 write입력란화면으로이동 http://localhost:8099/blog/write
    }
	
	
	@RequestMapping("/blog/write")
	 public String boardWrite() {
	   return "write" ;
	}
}//class END
