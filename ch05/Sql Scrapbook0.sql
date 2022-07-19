create table table_e_notnull(
login_id varchar2(20) not null,
login_pwd varchar(20) not null,
tel      varchar2(20)
);
/* 필수 입력 해야하는 칼럼은 not null 제약조건을 지정 */
insert into table_e_notnull values(null, '1234', '010');
insert into table_e_notnull values('hong', null, '010');
insert into table_e_notnull values('hong', '1234', '010');
insert into table_e_notnull values('hong', '1234', null);


select * from table_e_notnull;
/* not null 제약조건으로 지정된 칼럼의 값을 null로 update 불가 */
update table_e_notnull set login_id = null where login_id = 'hong'; -- 오류

/* 제약조건 이름 지정 */
create table table_notnull( 
login_id varchar2(20) constraint tbl_ligid not null,

);

/*칼럼 수정 제약조건 추가*/