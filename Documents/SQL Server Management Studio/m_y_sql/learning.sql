-- creating and using the database
create database SampleDB;
use  SampleDB;

-- creating a table
create table customers(
ID int not null,
cust_name varchar(20) not null,
Address char(40) not null,
department varchar(30) not null,
salary int not null,
percent decimal(5,3) not null,
primary key (ID)
);
create table orders(
Order_ID int not null,
Order_details varchar(60) not null,
primary key (Order_ID)
);
create table cust_Order(
Cust_ID int not null,
Order_ID int not null,
sale_Date datetime,
primary key(cust_ID, Order_ID)
);

-- inserting a records into table
insert into customers values
(1, 'Dondipsy', 'ifo', 'BI_Analyst', 9000, 0.089),
(2, 'Tomilola', 'ogun', 'Survey_Analyst', 6000, 0.008),
(3, 'Damilola', 'Agbado', 'Baker', 5000, 0.049),
(4, 'Damilade', 'ikeja', 'Biologist', 7000, 0.059),
(5, 'Temitope', 'Allen', 'Data_Analyst', 6000, 0.039),
(6, 'Samad', 'Delta', 'Student', 2000, 0.023);

-- using Alter to Add a column to a table
Alter table customers Add sex char(2);

-- updating the table with 
-- a case (it just like and if and else condition)
update customers Set sex =
Case 
when ID in (1, 4, 6) then 'm'
when ID in (2, 3, 5) then 'f'
end
where ID in (1 ,2 ,3, 4, 5, 6);


update customers set department = 'Writer' where ID = 6;

-- verification
Select * from Customers;

-- insert records into table 2
insert into Orders values
(1, ' dior perfume'),
(2, 'Addias Track- suit'),
(3, ' Mixers'),
(4, 'V_Trousers'),
(5, 'Books'),
(6, 'Playstation 5')
;
-- insert records into table 3
insert into cust_Order values
(1, 6, '2025-4-21 10:20:00'),
(2, 1, '2025-4-20 09:04:00'),
(3, 3, '2025-4-11 10:20:00'),
(4, 2, '2025-4-10 10:06:00'),
(5, 4, '2025-4-12 10:10:00'),
(6, 5, '2025-4-15 09:20:00');

/* This is a cross join  it will give duplicate of all column */
select * from customers, Orders, cust_Order;

/* using sql join*/
-- table.column so there won't be duplicate column while using join
select customers.id as cus_id ,
customers.cust_name , customers.address as cus_add, 
customers.department as cus_dept,
customers.salary as cus_sal,
customers.percent as cus_per, customers.sex, 
customers.total_salary as cus_tot,
cust_order.Order_ID, cust_order.Cust_ID, 
cust_order.sale_Date, orders.Order_details
 from Customers 
join Cust_Order On Customers.ID = Cust_Order.Cust_ID
join Orders On cust_order.Order_ID = Orders.Order_ID;


/*Sql  logical(exists) operators*/
 select * from customers join cust_order on customers.ID = cust_order.Cust_ID 
 where exists(
 select Order_ID , salary from cust_order where Order_ID > 3 and salary > 5000
 );
 alter table customers add total_salary int not null;
 update customers set total_salary =
 Case
     when id in  (1, 2, 3, 4) then Salary * percent
	 when id in  (5, 6) then Salary * percent
     end
	where id in (1, 2, 3, 4, 5, 6);
select current_timestamp;
select * from customers join cust_order on customers.ID = cust_order.Cust_ID 
 where sale_Date > '2025-4-10 10:06:00';
 select count(*)from customers;
 /* change username for mysql connection*/
 rename user 'root'@'localhost' to 'Ayodeji_Adedolapo'@'localhost';
  
/* to show all user and host in mysql*/
/* this brought out % meaning any host or ip*/
 select user, host from mysql.user;
 flush privileges;
 
 /* to delete user name */
 drop user 'Dipsy_analyst'@'%';
 show databases;
use performance_schema;
show tables;

select Table_Name from information_schema.Tables
where Table_Schema = 'sampledb';

-- i don't get this 
select Table_Name from information_schema.Columns
where Table_Name = 'customers' and Table_schema ='sampledb';

create database lovedb;
use lovedb;
show databases;
drop database if exists lovedb;

create table calender(Months date Not null);
insert into calender(Months) values
('2023-01-01'),
('2023-02-01'),
('2023-03-01'),
('2023-04-01'),  
('2023-12-01');
select * from calender;
create database jump;

-- mysql doesn't support complex filtering
-- However you can't combine show with info_schemas
show schemas;
use Sampledb;
show columns from customers;

select table_schema, table_name
from information_schema.columns
where column_name = 'address';

-- % it a wildcard char it use specifically in like clause
-- it means matches zero or more character 
show databases like 'sample%';
select * from customers;

-- if you want to disable safe update  mode only for your current session
-- temporary (session only) solution
set sql_safe_updates = 0;

delete from customers where cust_name = 'samad' or Address = 'ikeja'; 

-- if you want to re-enable safe update mode for your current session
set sql_safe_updates = 1;

delete from customers;
 alter table customers drop total_salary;
insert into customers values
(1, 'Dondipsy', 'ifo', 'BI_Analyst', 9000, 0.089, 'm'),
(2, 'Tomilola', 'ogun', 'Survey_Analyst', 6000, 0.008, 'f'),
(3, 'Damilola', 'Agbado', 'Baker', 5000, 0.049, 'f'),
(4, 'Damilade', 'ikeja', 'Biologist', 7000, 0.059, 'm'),
(5, 'Temitope', 'Allen', 'Data_Analyst', 6000, 0.039, 'f'),
(6, 'Samad', 'Delta', 'Student', 2000, 0.023, 'f');
alter table customers add total_salary int not null;
update customers set total_salary =
case
when id in (1, 2, 3) then salary * percent 
when id in (4, 5, 6) then salary * percent
end 
where id in (1, 2, 3, 4, 5, 6);
select * from customers;
select * from customers where department in ('Survey_Analyst');
select * from customers where salary between 4500 and 6000;
select cust_name, Address, salary from customers where salary > 6000 order by Address desc;
Select distinct salary from customers;
select * from customers where salary > 5000 group by id, salary;
-- FIND EXAMPLE ON HOW TO USE HAVING Clause
 
-- creating a table from an existing table 
create table big select cust_name, address, salary from customers where salary > 6000;
drop table big ;
select * from big;
alter table cust_order drop primary key;

/* below is drop a foreign key  
alter table cust_order drop foreign key order_con ;
*/

alter table cust_order Add Primary key (cust_id);
alter table cust_order Add constraint order_con foreign key 
(order_id) references orders(order_id);




/* creating table,
 using  insert  and select to copy the records from 
 an existing table */
 
 create table ballin
 (ID int not null,
cust_name varchar(20) not null,
Address char(40) not null,
department varchar(30) not null,
salary int not null,
percent decimal(5,3) not null,
sex char(2),
total_salary int not null,
primary key (ID));

 /*using  insert  and select to copy the records from 
 an existing table*/
 
insert into ballin
(ID, cust_name, Address, department, salary, percent, sex, total_salary)
select * from customers;

-- verification
select * from ballin;

/* insert table from another table with the same structure */
-- create table 

create table callin
 (ID int not null,
cust_name varchar(20) not null,
Address char(40) not null,
department varchar(30) not null,
salary int not null,
percent decimal(5,3) not null,
sex char(2),
total_salary int not null,
primary key (ID));

insert into callin table ballin;

-- verification
select * from callin;

truncate table callin;

-- this is use to disable update and delete in table when = 0
-- but when = 1, it is use  enable  update and delete in a table
set sql_safe_updates = 1;
desc callin;

insert into callin
(ID, cust_name, Address, department, salary, percent,total_salary) 
select ID, cust_name, Address, department, salary, percent,total_salary from ballin; 

select 40* 100;

-- concat mathematical  statement
-- concat is use  for join two column to be a single column

select concat(id, '  ', cust_name) as details, Address, salary from ballin;

-- insert into -- select using the where clause to insert a specific records 
insert into callin select * from ballin where cust_name like 'D%';
select * from ballin;

-- using the limit 
insert  into callin select * from ballin order by id asc limit 4;

-- updating multiple column data without a where clause 
update ballin set salary = salary + 2000 , total_salary = total_salary * 100; 

-- sorting result set in a preferred order
select * from ballin order by (case Address
when 'Agbado' then 1
when 'Allen' then 2
when 'Delta' then 3
when  'ifo'  then 4
when  'ikeja' then 5
else 100 end) Asc;

-- to create a view 
create view  cust_view as select * from  customers; 

-- verification
select * from cust_view;

-- create view with a where clause 
create view ballin_view  as select * from ballin where salary > 5000;

-- verification
select * from ballin_view;
-- The with check option
/** 
The purpose of the WITH CHECK OPTION is to ensure that all 
UPDATE and INSERT statements satisfy the condition(s) 
specified by the WHERE clause.
**/
create view  callin_view as select cust_name, total_salary, sex
from callin where sex = 'm' with check option;

select * from callin_view;

insert into callin values
(5,'Bola', 'Abuja', 'Insurance', 15000, 0.043, 'm', 51000),
(6,'Shuqrah', 'Ilorin', 'Marketing', 12000, 0.063, 'f', 60000);

update callin set sex = 'm' where cust_name = 'Damilola';

set sql_safe_updates = 1;

-- update view
-- update made to view will also affect table  
update ballin_view set cust_name = 'wasiu' where id = 4;

-- verification
select * from ballin_view;

-- a metadata query to list views in schema
select table_schema, table_name from information_schema.views
where table_schema = 'sampledb';

-- drop view if exists
Drop view if exists Demo_view;

alter table ballin rename column total_salary to salary_total;
show create view sampledb.ballin_view;
show tables like 'ballin';
 describe ballin;
 
 SELECT User, Host FROM mysql.user WHERE User = 'Ayodeji_Adedolapo';
 drop view ballin_view;
 create view ballin_view as select * from ballin;