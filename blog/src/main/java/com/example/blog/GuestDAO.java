package com.example.blog;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;



@Service
public class GuestDAO  { 
	
  @Autowired
  private GuestRepository temp ;
	
   public void dbInsert(GuestVO guest) {
		temp.save(guest); 
   }//end	
	
	public List<GuestVO> dbSelect( GuestVO guest) {
	   return (List<GuestVO>)temp.findAll();
	}//end
	
	public int dbCount() {
	  return (int)temp.count();
	}//end
	
	public GuestVO dbDetail(GuestVO guest) {
	 return	temp.findById(guest.getSeq()).get();
	}//end
	
	public void dbDelete(GuestVO guest) {
		temp.deleteById(guest.getSeq());
		//temp.deleteById(guest.getSabun());
	}//end
	
	 public void dbEdit(GuestVO guest) {
		GuestVO gg = temp.findById(guest.getSeq()).get();
		gg.setName(guest.getName());
		gg.setTitle(guest.getTitle());
		gg.setPay(guest.getPay());
		gg.setEmail(guest.getEmail());
		System.out.println("수정데이터  "+ guest.getTitle());
		temp.save(guest);
	 }//end	
	 
}//class END

