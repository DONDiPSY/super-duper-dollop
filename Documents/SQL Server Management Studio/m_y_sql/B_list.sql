create database  Revisiondb;
drop database jump;
use Revisiondb;
create table Bucket_list
(
Id int not null primary key,
Country char(30) not null,
Book  char (40) not null,
want_to_see char (40) not null,
job char (20) not null,
thing_want_to_do text(1000) not null
);
insert into bucket_list values
(1, 'United kingdom', 'Atomic Habit', 'Museum', 'inter:BI_Analyst', 'getting a degree BSC(Hons)'),
(2, 'USA', '7_Habits_of_Highly_Effective_People', 'miami_beach', 'jr:BI_Analyst', 'Take care of my family'),
(3, 'Makkarh', 'Data_Science_for_Business', 'kabbah', 'sr:BI_Analyst', 'Take my family to Makkarh'),
(4, 'Canada','Books_by_Ryan_Holiday', 'sponsor_lil_Angel_MSC', 'tomi_get_a_job', 'This will make me the happiest brother');

select * from bucket_list;
