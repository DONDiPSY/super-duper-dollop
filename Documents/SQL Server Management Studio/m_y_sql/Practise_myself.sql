use myselfdb;
create table friends
(
Id int Not null,
Name char(10) Not null,
sex char Not null,
Occupation varchar(30) Not Null,
Address varchar(40) Not null
)
;
Alter table friends Add primary key (Id);
Alter table friends Add salary int;
Alter table friends modify Name char(30);
Insert into friends values
(1, 'Dondipsy', 'm', 'BI_Analyst', 'Ifo,Ogun-State', 10000),
(2, 'Tomilola', 'f', 'Survey', 'Sango,Ogun-State', 8000),
(3, 'Temitope', 'f', 'Data_Analyst', 'Ikeja,Lagos-State', 9000),
(4, 'Jame', 'm', 'software-Developer', 'Ogba,Lagos-State', 8000),
(5, 'Shuqrah', 'f', 'Account', 'Wusa, Abuja', 6000),
(6, 'Drey', 'm', 'Forex-Trader', 'Alaba,Lagos-State', 5000),
(7, 'Damilola', 'f', 'Baker', 'Agbado,Ogun-State', 7000),
(8, 'Demilade', 'm', 'Doctor', 'Yaba,Lagos-State', 5000)
;
select * from friends;
update friends set Address = 'VI,Lagos' where ID = 8;
Alter table friends Rename to friends_families;
select * from friends_families;
Select distinct salary from friends_families order by salary Asc;
Select * from friends_families where salary > 6500;
Alter table friends_families Add Percent decimal (5, 2);
Update friends_families Set percent =
case 
  when Id in (1, 3) then 0.06
  when Id in (2, 5) then 0.08
  when Id in (4, 6 ,8) then 0.05
  else 0.04
  end
  where Id in (1,2, 3, 4, 5, 6, 7, 8);
Select Id, Name, sex, occupation from friends_families where sex in ('f') ; 
Select Id, Name, sex, occupation from friends_families where Id between 1 and 6;
Select Id, Name, sex, occupation from friends_families where percent like '0.06';
select * from friends_families where percent > 0.05 order by occupation ASC;
-- check code 
select  Address, sum(salary) as Total_Salary from friends_families
where percent > 0.05 group by id order by salary Asc ;
select  Id, Name, count(salary) as Total_Salary from friends_families
where percent > 0.05 group by  Id, salary ;
select Id, Name, sum(salary) as Total_salary from friends_families group by id, Name Having sum(salary) > 6000 ;
create index idx_Name on friends_families(Name);
-- drop index idx_Name on friends_families;
select * from friends_families where Name = 'shuqrah'; 