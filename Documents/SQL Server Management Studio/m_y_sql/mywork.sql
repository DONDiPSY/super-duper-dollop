create database rundb;
use rundb;
create table Books
(
id int not null,
your_name char(100) not null,
Age int not null,
sex char (6) not null,
Address char(50) not null,
salary int not null,
primary key (id)
);
insert into books values
(1, 'Adedolapo', 29, 'male', 'ogun', 20000),
(2, 'Tomilola', 23, 'female', 'ogun', 10000),
(3, 'Demilade', 27, 'male', 'Agbado', 40000),
(4, 'Ayodeji', 25, 'male', 'oshodi', 30000),
(5, 'Damilola', 29, 'female', 'sango', 50000),
(6, 'Temitope', 33, 'female', 'ikeja', 60000),
(7, 'Abdulilah', 32, 'male', 'Allen', 20000),
(8, 'Temitayo', 26, 'female', 'wuse', 70000); 
select * from books;
update books set address = 'ifo' where id = 1;
alter table books modify percent decimal (5,3) not null;
update books set percent =
case
  when sex in ('male') then 0.045
  when sex in ('female') then 0.025
  end
where id in (1, 2, 3, 4, 5, 6, 7, 8);
alter table books rename to table_data;
select * from table_data; 
select  distinct id, salary from table_data where percent = 0.045;
select * from table_data where salary in (20000);
select * from table_data where salary between 40000 and 50000;
create index idx_name on table_data(your_name);
show databases;
rename table table_data to data_table; 
alter table data_table rename column your_name to people_name;

-- simple cloning 
create table  table_data select * from data_table;
select * from table_data;
desc table_data;

-- shallow cloning
create table my_data like table_data;
select * from my_data;
desc my_data;

-- deep cloning
create table your_data like data_table;
insert into your_data select * from data_table;
select * from  your_data;
desc your_data;