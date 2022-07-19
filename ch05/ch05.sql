select sysdate from dual;

/* union 중복 제거, union all 중복 허용(포함) */
select 10 from dual
union
select 10 from dual;

select 10 from dual
union all
select 10 from dual;

select empno, ename, sal from emp where deptno=30
union
select empno, ename, sal from emp where deptno=10;

select empno, ename, sal from emp where deptno=10
union all
select empno, ename, sal from emp where deptno=10;

/* minus */
select 10 from dual         /* A */
minus
select 20 from dual;      /* B */

select 20 from dual         /* A */
minus
select 10 from dual;      /* B */

/*  */
select * from
 (select 10 from dual
  union
  select 20 from dual)       /* A  (10, 20) */
minus
select * from
 (select 30 from dual
  union
  select 20 from dual);      /* B  (20, 30) */
  
/*q4*/
  select * from emp
  where not (sal>=2000 and sal<=3000);
  
/*단일행 함수, 문자처리함수 -upper,lower,initcap(첫글자만 대문자 나머지는 소문자)*키워드 걍 대충 소문자로 써도 알아먹음*/
  select ename, upper(ename),lower(ename), initcap(ename), initcap('SMITH MCDO') from emp;
  /*where절에서 */
  select*
  from emp
  where ENAME= upper('smith');
  select * 
  from emp
  where lower(ENAME)='smith';
  /*문자열 추출 substr(문자, 시작, 개수)*/
  select job, substr(job,1,2),substr(job,3,2),substr(job,10) from emp;
  select job, substr(job,-length(job)), substr(job,-length(job),2), substr(job,-3) from emp;
  /*특정 패턴이 시작될때 index출력 */
  select instr('hello,oracle','ora'),instr('hello,oracle','ora',5),instr('hello,oracle','ora',2,2) from dual;
  /*이름에 S 포함 여부*/
  select * from emp where instr(ename,'S')>0;/*인덱스 값이 0보다 클때 문자가 존재 0미면 없다는 뜻*/
  select * from emp where like '%S%';
  /*주민보ㅓㄴ호 20020505-3333333*/
  select instr('20020505-3333333','-')from dual;/*instr로 위치 찾고*/
  select substr('20020505-3333333',1,9-1)from dual;/*substr로 자름*/
  select substr('20020505-3333333',9+1)from dual;
  select substr('20020505-3333333',1) first, substr('20020505-3333333',1instr('20020505-3333333','-')+1) last from dual;
  /*대체*/
  select '010-1234-5678' ,replace('010-1234-5678','-',''),replace('010-1234-5678','-') from dual;
  /*공백채우기*/
  select 'Oracle' ,lpad('Oracle',10,'#'),/*왼쪽부터(L)#으로 채워서 oracle포함10자리만듦*/
  rpad('Oracle',10,'#'),lpad('Oracle',10), rpad('Oracle',10),length(rpad('Oracle',10,'#')),length(rpad('Oracle',10))
  from dual;
  /*비번처리*/
  select rpad('971225-',14,'*') from dual;
  /*문자열 결합함수 concat,결합연산자 ||   concat 은 두개씩 합치기 가능 ||는 더 많이도 가능*/
  select concat(empno,ename),empno||ename from emp;
  select empno || ename, empno|| ':' ||ename from emp;
  /*'hello' 'hi'  'i am tom'를 concat써서 합치기 -> concat(concat())하면 됨*/
  select concat(concat('hello',' hi'),'i am tom')
    from dual;
  /**/
  select Trim('  Oracle  ') as trim,
         Trim(leading from '  Oracle  '),
         trim(trailing from '  Oracle  '),
         trim(both from '  Oracle  ') from dual;
         /*Ltrim=leading, Rtrim=trailing, (왼쪽부터 글자가 시작하는 한국의 경우만 다음 경우가 일치함)*/
 /*반올림*/
 select round(1234.5678),
        round(1234.5678,0),
        round(1234.5678,1),/*2번째 자리에서 반올림해 1번쨰 까지 나타냄*/
        round(1234.5678,2),
        round(1234.5678,-1),/*반올림해10자리까지 나타냄*/
        round(1234.5678,-2)/*반올림해 100까지*/
     from dual;
/*버림*/
 select trunc(1234.5678),
        trunc(1234.5678,0),
        trunc(1234.5678,1),/*1번쨰 까지 나타냄*/
        trunc(1234.5678,2),
        trunc(1234.5678,-1),/*10자리까지 나타냄*/
        trunc(1234.5678,-2)/* 100까지*/
     from dual;
     
/*정수로 올림 버림*/
 select ceil(3.14),floor(3.14),ceil(-3.14),floor(-3.14) from dual;
 /**/
 select mod(15,6),from dual;
 /*계산 값이 0인지 양수인지 음수인지에 따라 양수면1 음수면 -1 0은0*/
 select sign(1-10) from dual;
/*오늘 내일 어ㅈㅔ*/
 select sysdate, sysdate+1 as "내일", sysdate-1 as "어제" from dual; 
 /*오늘 다음달 저번달*/
 select sysdate, add_months(sysdate,1),add_months(sysdate,-1) from dual;
 /*10년뒤 add month써서*/
 select empno,ename,hiredate,add_months(sysdate,120) from emp;
 
 select *
   from emp
   where add_months(hiredate,384)>sysdate /*고용일로부터 384개월 후의 날짜가 오늘 날짜보다 클 경우*/
 
 /*두 날짜간의 개월수 구하기 months_between()*/
   select empno, ename, hiredate,sysdate,
          months_between(hiredate,sysdate),
          months_between(sysdate,hiredate),/*<주의>앞에서 뒤를 빼줌 sys-hire*/
          trunc(months_between(sysdate,hiredate))/*round,ceil.. 날짜함수에도 반올림 등이 가능ㅎ다*/
         from emp;.
/*요일, 월의 마지막 날짜*/         
select next_day(sysdate,'월요일') from dual;
select last_day(sysdate) from dual;
select last_day('1996-08-01') from dual;
select to_number(to_char(last_day('1996-08-01'),'dd')) from dual;/*두글자의 day로 표현?*/
/*함수별 포멧 문자*/
select sysdate, round(sysdate,'cc')/*세기 기준 반올림*/, Round(sysdate,'yyyy'), /*년도기준반올림*/
Round(sysdate,'Q'),/*2분기의 반 초과해 3분기로 반올림*/
round(sysdate,'mm'),
round(sysdate,'ddd')
   from dual;
/*숫자형 문자열이 아니면 숫자값과 연산시 오류 발생 */
   select 'ABCD' + empno,ename from emp where ename='SMITH';

/**문자열 변환함수 to_char()*/
   select to_char(sysdate) from dual;
   
   select to_char(sysdate,'cc'), to_char(sysdate,'yyyy'), to_char(sysdate,'yy'),to_char(sysdate,'mm'),/*mm은 두글자로(06) mon은 jul로 나옴*/to_char(sysdate,'mon'),to_char(sysdate,'month') from dual;
   select to_char(sysdate,'dy')/*요일줄임말*/,to_char(sysdate,'day'),to_char(sysdate,'dd'),to_char(sysdate,'w')/*몇째주*/ from dual;
/*특정지역언어 출력*/
   select sysdate, to_char(sysdate,'mon'), to_char(sysdate,'mon','nls_date_language=korean'),to_char(sysdate,'mon','nls_date_language=English') from dual;
   
   
   /*시간 형식 출력*/
   select to_char(sysdate,'HH24:MI:SS'), to_char(sysdate,'HH12:MI:SS'),to_char(sysdate,'HH:MI:SS P.M.') from dual;
   /*숫자 자리 및 출력 포멧*/
   select 123456, to_char(123456,'$999,999'),to_char(123456,'L999,999')/*$는 $로시작하는거 L은 local지역변수*/ from emp;
   /*문자열을 날짜로 변환*/
   select to_date('2022-06-27')from dual;/
   
   /*상황에 따라 데이털르 반환/case/decode 기준 데이터에따라 반환할 값 지정,case 기준데이터 없ㅇ믐 문*/
   select decode(10,'참','거짓','몰라')from dual;
   select empno,ename,job,sal, decode(job,'MANAGER',sal*1.1,'SALESMAN',SAL*1.05,'ANALYST',SAL*1,SAL*1.03) from emp;
   
   select empno,
       case
       when comm is null then '수당없음'
       when comm =0 then'수당업ㅇ,ㅁ'
       when comm > 0 then '수당없'||comm
       end as comm_txt 
       from emp;
       
//
select count(sal),count(comm) from emp;
select count(*)from emp;
//
select deptno,job,count(*),max(sal),avg(sal)
from emp
group by rollup(deptno,job);
select deptno,job,count(*),max(sal),avg(sal)
from emp;
select deptno,job,count(*),max(sal),avg(sal)
from emp
group by cube(deptno,job);
select *
from(select deptno,job,sal from emp)
pivot(max(sal) for deptno in(10,20,30))
order by job;
/*pivot,decode을 활용해 2차원 출력도 가능*/
select *
  from(select deptno,
              max(decode(job,'CLERK',sal)) as "clerk",
              max(decode(job,'SALESMAN',sal)) as "SALESMAN",
              max(decode(job,'PRESIDENT',sal)) as "PRESIDENT",
              max(decode(job,'MANAGER',sal)) as "MANAGER",
              max(decode(job,'ANALYST',sal)) as "ANALYST"
              from emp
              group by deptno
              order by deptno)/*select문이아닌 from문에서 읽어줌*/
              
/******************************6.28*/
select * from emp;
select count(*) from emp;/*행 개수를 출력*/
select ename,sum(sal) from emp group by ename;

/*중복을 제외한 distinct,sum은 null을 자동제외함?*/
select sum(distinct sal),sum(all sal), sum(sal) from emp;
/*count함수 null값을 제외하고 count 함*/
select count(sal),count(comm) from emp;
select sal,comm from emp;
/*데이터 건수 확인 count(*) */
select count(*) from emp;
/*null을 제외한 count와 조건을 붙여 null도 포함시켜 count 시키기*/
select sum(comm)/count(comm),
       round(sum(comm)/count(*),1),
       round(sum(comm)/count(nvl(comm,0)))/*comm이 null이면 0입력 따라서 count(*)이랑 같은 뜻*/ from emp;

select count(nvl(comm,0)) from emp;

/*null이 아닌것만 집계하기 ?*/
select count(comm) from emp where comm is not null;

select max(sal) from emp;
/*문자*/
select max(ename) from emp;
select ename from emp; /*알파벳순서끝,소문자(영문),영어보단 한글이 더 큼*/
select min(hiredate),max(hiredate) from emp;
select avg(sal), sum(sal)/count(sal) from emp;

/*union all 조회한 결과를 합쳐줌 all은 중복 허용 그냥 union은 중복 제거*/
select avg(sal) from emp where deptno=10
union all 
select avg(sal) from emp where deptno=20
union all 
select avg(sal) from emp where deptno=30;

/*group by로 그룹화*/
select deptno, avg(sal) from emp group by deptno;
select deptno, avg(sal) from emp;
select * from emp;


/*나올수 있는 모든 경우의 수 카티션곱*/
select * from emp,dept;
/*where = 등가조인*/
select * from emp,dept where emp.deptno=dept.deptno;
/*별칭부여*/
select * from emp e , dept d where e.deptno = d.deptno;
/*조인하면 각 다른 테이블에 있는 것들을 select 가능*/
select e.empno, e.ename, e.sal, d.dname, d.loc from emp e, dept d where e.deptno = d.deptno; 
/*두개 테이블 모두 존재하면 테이블명.칼럼명으로 표시, 각각 하나씩만 존재하면 ㅇ름만 써도 됨*/
select empno, ename, sal, dname, loc ,e.deptno from emp e, dept d where e.deptno = d.deptno; 
/*where 뒤 and로 조건을 주기*/            
select empno, ename, sal, dname, loc ,e.deptno from emp e, dept d where e.deptno = d.deptno and sal>=3000; 

/**/
select empno, ename, job, hiredate,sal,comm,e.deptno,d.deptno,dname,loc
from emp e, dept d where e.deptno = d.deptno and sal<=2500 and empno <=9999 order by empno;

/*1.비등가 조인 case 를 사용해서 */
select * from salgrade;

select empno,sal,
       case when sal>= 700 and sal<=1200 then 1
            when sal>= 1201 and sal<=1400 then 2
            when sal>= 1401 and sal<=2000 then 3
            when sal>= 2001 and sal<=3000 then 4
            when sal>= 3001 and sal<=9999 then 5
            end as salgrade
            from emp order by empno;
 /*2.salgrade 테이블이 있으니까 이거랑 조인해서 구하기*/
select empno, sal, grade from emp e, salgrade s
where sal between losal and hisal; /*sal이 losal과 hisal 사이에 걸쳐질떄 select*/
/* where sal >= losal and sal <=hisal*/

/*자체 조인 ,별칭*/
select * from emp;
select a.empno,a.ename,a.job,/*사원의*/ a.mgr,b.empno,b.ename/*매니저의 총 두개의 테이블 */
from emp a, emp b where a.mgr=b.empno;
/*outer join right*/
select * from emp;
select a.empno,a.ename,a.job,/*사원의*/ a.mgr,b.empno,b.ename/*매니저의 총 두개의 테이블 */
from emp a, emp b where a.mgr(+)=b.empno;
/


/*자연 조인에서는 조인 조건을 기술하지 않아도 자동으로 공통 컬럼을 찾아서 조인한다
 * 자연 조인에서 사용하는 테이블간에 동일한 이름과 형식의 컬럼이 둘 이상인 경우 자연 조인을 사용할 수 없다.
이럴 경우 USING 절을 이용한 조인문을 이용하면 조인문을 구사할 수 있다*/
/*natural join 양쪽 테이블에 공통 칼럼이 join 기준 select시 해당 칼럼 칼럼명 표시 여기서는 deptno가 join 칼럼*/
select e.empno,e.ename,e.mgr,e.hiredate,e.sal,e.comm deptno, d.dname, d.loc
from emp e natural join dept d
order by deptno, e.empno;
/*join using */
select e.empno,e.ename,e.mgr,e.hiredate,e.sal,e.comm deptno, d.dname, d.loc
from emp e join dept d using(deptno)
where sal>=3000
order by deptno, e.empno;
/*join on   /on 쪽에 칼럼도 표시 해줘야함*/
select e.empno,e.ename,e.mgr,e.hiredate,e.sal,e.comm deptno, d.dname, d.loc
from emp e join dept d on(e.deptno=d.deptno)
where sal>=3000
order by deptno, e.empno;
/*left outer join*/
select e.empno,e.ename,e.mgr,e.hiredate,e.sal,e.comm deptno, d.dname, d.loc
from emp e left outer join dept d on(e.deptno=d.deptno);

/*조건문 안에 쿼리 넣기*/
/*alen의 추가수당(cmm) 보다 많은 수당을 받는 사원*/
select comm from emp where ename=upper('allen');
select * from emp where comm>(/*조건문 안에 쿼리문 들어감*/select comm from emp where ename=upper('allen')/**/)

/*smith의 입사일자보다 먼저 입사한 사원*/
select hiredate from emp where lower(ename)='smith';
select * from emp where hiredate < (select hiredate from emp where lower(ename)='smith');
select empno, hiredate from emp order by hiredate;
/*평균 급여보다 많은 급여를 받는 사원들*/
select avg(sal) from emp;
/*select * from emp where sal>2077.08*/
select * from emp where sal> (select avg(sal) from emp);
/*평균 이하의 급여를 받고 부서번호가 20인 사원들*/
select * from emp where sal<= (select avg(sal) from emp)
                 and deptno=20 ;

/*다중 행*/
select deptno from dept where loc in ('DALLAS','CHICAGO');
select * from emp where deptno in(20,30);

select * from emp where sal<all(select sal from emp where deptno=30);
/*다중열 비교*/
select * from emp where(deptno,sal) in
(select deptno, max(sal) from emp group by deptno);
/*인라인 뷰 가상테이블 만들기*/
/*select * from emp where deptno = 10;
select * from dept;*/
select * 
from (select * from emp where deptno = 10) a
     (select * from dept) b
     where a.deptno = b.deptno ;
     
/*with 절 사용하기*/
with a as (select * from emp where deptno = 10)
   b as (select * from dept)
   select * from a,b where a.deptno=b.deptno;
   
/**/
 
   select * from dept;

update dept set loc = '수원' where deptno = 60;
commit -- auto commmit 에서 manual commit 으로 바꾸고 난 뒤

select * from dept_tcl;

create table dept_tcl as select * from dept where deptno <= 40;

