package com.example.blog;

import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;


@Controller
public class GuestController {	
	
	@Autowired
	GuestDAO dao; 
	
	
	@RequestMapping("/guestWrite.do")
	public String guest_write() {
	  return "guestWrite";  //guestWrite.jsp
	}//end
	
	
	@RequestMapping("/guestInsert.do")
	public String guest_insert(GuestVO dto) {
	  System.out.println("guest_insert(GuestVO dto)함수" );
	  dao.dbInsert(dto); 
	  return "redirect:/guestList.do";
	}//end
	
	
	@RequestMapping("/guestList.do")
	public String guest_select(Model model, GuestVO guest) {
		int Gtotal = dao.dbCount();
		List<GuestVO> LG = dao.dbSelect(guest);
		model.addAttribute("Gtotal", Gtotal);
		model.addAttribute("LG", LG);
	    return "guestList"; 
	}//end--------------------------------------------------------
	

	@RequestMapping("/guestDetail.do")
	public String guest_detail(Model model, GuestVO guest) {
	  GuestVO dto=dao.dbDetail(guest);
	  model.addAttribute("dto", dto);
	  return "guestDetail";
	}//end

	
	@RequestMapping("/guestDelete.do")
	public String guest_delete(Model model, GuestVO guest) {
	   dao.dbDelete(guest);
	   return "redirect:/guestList.do";
	}//end
	
	
	@RequestMapping("/guestpreEdit.do")
	public String guest_preEdit(Model model, GuestVO guest) {
	  GuestVO dto=dao.dbDetail(guest);
	  model.addAttribute("dto", dto);
	  return "guestEdit";
	}//end
	
	@RequestMapping("/guestEdit.do")
	public String guest_edit(GuestVO dto) {
	  dao.dbEdit(dto); 
	  return "redirect:/guestList.do";
	}//end
}//Controller class END











