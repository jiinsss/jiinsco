package com.example.blog;


import java.util.Date;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;


import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
@ToString
@Entity
@Table
public class GuestVO  { 
	@Id
	@GeneratedValue(strategy=GenerationType.AUTO)
	private int seq;
	
	@Column(name="sabun")
	private int sabun ;
	
	@Column(name="name")
	private String name ;
	
	@Column(name="title")
	private String title ;
	
	@Column(name="wdate", insertable = true, updatable = false,  columnDefinition = "date default sysdate")
	private Date wdate;
	
	@Column(name="pay")
	private int pay ;
	
	@Column(name="hit",insertable = true, updatable = false, columnDefinition = "number default 0")
	private int hit;
	
	@Column(name="email")
	private String email;

	
	public int getSeq() {return seq;}
	public void setSeq(int seq) {this.seq = seq;}
	public int getSabun() {	return sabun;	}
	public void setSabun(int sabun) {	this.sabun = sabun;	}
	public String getName() {	return name;	}
	public void setName(String name) {this.name = name;	}
	public String getTitle() {	return title;	}
	public void setTitle(String title) {this.title = title;	}
	public Date getWdate() {return wdate;}
	public void setWdate(Date wdate) {this.wdate = wdate;}
	public int getPay() {return pay;}
	public void setPay(int pay) {this.pay = pay;	}
	public int getHit() {return hit;}
	public void setHit(int hit) {this.hit = hit;}
	public String getEmail() {return email;}
	public void setEmail(String email) {this.email = email;}	
	
}//class END


