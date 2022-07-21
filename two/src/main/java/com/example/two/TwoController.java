package com.example.two;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class TwoController {

	@RequestMapping("/mytest.komi")
	public @ResponseBody  String test() {
		String msg="<h1> snow coffee cake 2:54  4:12  </h1>";
		return msg ;
	}//end
	@RequestMapping("/kakaowrite.komi")
	public  String guestinsert() {
			return "guestWrite" ;
	}//end
	
}//class END
