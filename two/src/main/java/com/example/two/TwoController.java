package com.example.two;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class TwoController {

	@RequestMapping("/mytest.komi")
	public @ResponseBody  String test() {
		String msg="<h1> rain rain 10:15  </h1>";
		return msg ;
	}//end
	@RequestMapping("/kakaowrite.komi")
	public  String guest_write() {
			return "guestWrite" ;
	}//end
	@RequestMapping("/summerwrite.komi")
	public  String summer_write() {
			return "write" ;
	}//end
	
}//class END
