/*orlcstudy 유저 생성*/
drop user orclstudy;
create user orclstudy identified by ORACLE;
default tablespace users
temporary tablespace temp
quota unlimited on users
account lock;

select * from dba_users;

select * from user_objects;

create table temp(
col1 varchar2(20),
col2 varchar2(20)
);

/*사용자 정의 롤*/
create role rolestudy;

grant connect,resource,create view, create synonym to rolestudy;

select * from dba_role_privs where grantee like 'ORCL%';
select * from dba_sys_privs where grantee like 'ORCL%';