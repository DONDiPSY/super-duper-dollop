create database Practisedb;
use Practisedb;
/*stop excuting*/
create table employee_table(
ID int Not null,
Name char(20) Not null,
Address varchar (30) Not null,
Department char Not null,
Salary  int Not null,
percent decimal (5, 2) Not null,
primary key (ID)
);
Alter table employee_table modify Department char(50) Not null;
Alter table employee_table Add Sex char(1) Not null;
Alter table employee_table Add Age int  Not null;
select * from employee_table;
insert into employee_table values
(1, 'Dipsy', 'Kwara', 'HR', 7000, 0.05, 'm', 29),
(2, 'Bolu', 'Lagos', 'Sec', 2500, 0.02, 'm', 20),
(3, 'Tomi', 'Kwara', 'Manger', 5000, 0.03, 'f', 23),
(4, 'Faithia', 'Ogun', 'Accountant', 3500, 0.03, 'f', 24),
(5, 'Akon', 'Delta', 'Ass_Sec', 2000, 0.02, 'm', 25),
(6, 'Shruqah', 'Abuja', 'HR', 7000, 0.05, 'f', 27),
(7, 'Temi', 'Ibadan', 'CEO', 10000, 0.05, 'f', 33);
select * from employee_table;
desc employee_table;
update employee_table set Address = 'Ekiti' where ID = 2;
select * from employee_table;
create table Big_Bank
(
Account_no int Not null,
Account_name char(100) Not null,
Address varchar(100) Not null,
primary key (Account_no)
);
select * from Big_Bank;
/*drop table Big_Bank;*/
insert into big_bank values
(3455,' Raheem Adedolapo', 'ifo'),
(2344,' Raheem Tomilola', 'sango'),
(4455,' Ibrahim Shuqrah', 'wuse'),
(6455,' Adebayo Temitope', 'ikeja'),
(7455,' Risikat Raheem', 'ilorin');
select * from Big_Bank;
update employee_table set Name = 'shuqrah' where ID = 6;
update employee_table set Department = 'Ass_HR' where ID = 6;
select * from employee_table;
/*truncate table big_bank;*/
Select distinct Address, percent from employee_table order by percent asc;
/*ALTER TABLE employee_table
ADD PRIMARY KEY (ID); */
