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
alter table table_notnull modify(tel not null);
/*제약 조건명 변경*/
alter table table_notnull rename constraint tbl_ligid to tbl_id;
/*제약조건 삭제*/
alter table table_notnull drop constraint tbl_id;


/* UNIQUE */
create table table_unique(
id varchar2(20) primary key,
name varchar2(20) unique,
pwd varchar2(20) not null,
tel varchar2(20)
);

select * from user_constraints where table_name like '%UNI%';
insert into table_unique values('a','홍길동','124','010');
select * from table_unique;
insert into table_unique values('b','홍길동','124','010');
insert into table_unique values('c','임꺽정','123','010');

create table prim_table(
col1 number,
col2 number,
col3 varchar2(10),
primary key(col1, col2)
);

select * from user_constraints where table_name like 'PRI%';

insert into prim_table values(1,1,'a');
insert into prim_table values(1,1,'b'); -- 오류
insert into prim_table values(1,2,'b');
select * from prim_table;


/*foreing key*/
select * from user_constraints where table_name in ('emp','dept');

select * from emp;

rename emp to emp_bak;

create emp to emp_bak;

select lower(column_name), lower(data_type) from cols where table_name='EMP_BAK' order by column_id;
from cols where table_name='EMP_BAK' order by column_id;

create table emp(
ename varchar2(10),
job varchar2(9),
mgr varchar2(4),
hiredate date,
sal number(7,2),
comm number(7,2),
deptno number(2)
);
constraint emp_deptno_fk references dept (deptno)); /*!dept를 참조하는 emp_deptno*/
/*참조키 제약 조건은 참조되는 테이블의 칼럼이 primary key여야함*/
select * from user_constraints where table_name like '%DEPT%';
/*테이블 생성 후 primary key제약조건 추가하기
 * aleter table 테이블 명 add constraint 제약조건명 primar key(칼럼)
 * */
alter table dept add constraint pk_dept primary key (deptno);
/*참조하는 자식칼럼이 존재하면 삭제 불가*/
delete from dept where deptno=30;/*!안돼*/
select * from dept_tmp01;
select * from dept;
insert into dept select * from dept_tmp01 where deptno=30;

select * from emp;
insert into emp select * from emp_bak;
commit

/*부모칼럼의 값의 범위(도메인) 벗어난 값 입력 불가*/
insert into emp
values (9998,'홍길동','CLERK',7789,sysdate,500,null,99);
/**/
insert into emp
values(9998,'홍길동','CLERK',7789,sysdate,500,null,null);

/**/
create table table_check(
id varchar2(20) constraint tbl_chk_pk primary key,
id varchar2(20) constraint tbl_chk_pk check (length(pwd)>5),
tel varchar2(20)
);

insert into table_check values('1','1234','010');
select * from table_check;
insert into table_check values('2','1234','010');
/*default 제약조건*/
create table table_default(
id varchar2(20) primary key,
pwd varchar2(20) default '1234',
name varchar2(20),
regate date default sysdate,
point number(10) default 1000

);

insert into table_default 
values('hong','5678','홍길동','2022-07-01',3000);
select * from table_default;

insert into table_default(id,name) 
values('kim','김길동'); /*id와 이름을 제외한 값들은 위에서 default로 지정한 값*/
select * from table_default;/* sysdate 와 1000이 나온다*/

/*제약조건 활성화, 비활성화*/
select * from user_constraints where table_name in ('EMP','DEPT';)
alter table emp disable constraint EMP_DEPTNO_FK;
delete from dept where deptno=30;
select * from dept;
alter table emp enable constraint EMP_DEPTNO_FK;



