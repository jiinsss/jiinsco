select * from dept;

update dept set loc = '수원' where deptno = 60;
commit -- auto commmit 에서 manual commit 으로 바꾸고 난 뒤*/

select * from dept_tcl;

create table dept_tcl as select * from dept where deptno <= 40;
commit*/

insert into dept_tcl values(50, 'DATABASE', 'SEOUL');
update dept_tcl set loc = 'BUSAN' where deptno = 50;
delete from dept_tcl where dname = 'RESEARCH';

select * from dept_tcl;

commit*/
/*rollback*/


create table bank(
owner varchar2(50) primary key,
balance number(10)
);


select * from bank;
insert into bank values('홍길동',80000);
insert into bank values('일지매',0);
/*commit*/
select * from bank;

update bank set balance = balance -10000 where owner='홍길동';
update bank set balance = balance +10000 where owner='일지매';
commit*/
update bank set balance = balance -10000 where owner='홍길동';
update bank set balance = balance +10000 where where owner='일지매';
/*오류시 Rollback*/

create table emp_alter as select * from emp;
/*table 변경 alter table 테이블명 modify [add][drop]~~~*/
select * from test;
/*alter table 테이블명 add 칼럼명 데이터 타입 [제약조건]*/
alter table test add hp varchar2(10);

/*테이블 자르기 truncate*/
select * from test;
truncate table test;

/*데이터 딕셔너리*/
select * from dict;
select * from dictionary;
select * from dictionary where table_name like 'USER%';
select * from all_table_cols;

/*view-민감한정보-급여,입사일자,커미션여부*/
create view view_emp
as
select empno,ename,job,deptno
from emp order by empno;
/*민감정보 제외된거 볼 수 있음*/
select * from view_emp;


/*코드 재활용 한거 보기*/
create or replace view view_salgrade
as
/*여기 코드 재활용*/
create or replace view view_salgrade as -- 없으면 만들고 있으면 replace
select empno, ename, job, dname, loc, grade
  from emp e, dept d, salgrade s
 where e.deptno=d.deptno
   and sal between losal and hisal
 order by empno;
 
select * from view_salgrade;
select * from user_objects;



select * from dept;
create or replace veiw view_dept
as
select * from dept;
select * from view_dept;
update view_dept
set loc='제주'
where deptno=60;
commit


/* 뷰 */
select view_name, text_length, text
  from user_views;
  
  drop view view_salgrade;
  
 /* top-n */
(select rownum as rn, empno, ename
   from emp
  where rownum <= 6
   order by empno)
  where rn <= 2;

create sequence mySeq;
select mySeq.nextval from dual;
select mySeq.currval from dual; -- currval은 nextval를 쓴 다음 써야함
select mySeq.nextval, mySeq.currval from dual;
 
drop sequence emp_seq;

create sequence emp_seq
start with 9991
increment by 10
minvalue 9900
maxvalue 9999
cycle
--nocycle;
cache 10;
 
select emp_seq.nextval from dual;

create table emp_tmp01 as select * from emp;

select * from emp_tmp01;
insert into emp_tmp01
values(emp_seq.nextval, '홍길동','CLERK',7839,sysdate,500,null,40);

insert into emp_tmp01
values((select max(empno)+10 from emp), '홍길동','CLERK',7839,sysdate,500,null,40);