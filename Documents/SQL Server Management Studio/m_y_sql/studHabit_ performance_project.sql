use real_lifedb;
create table Habit_and_performance(
student_id char (5) not null primary key,
age int not null,
gender varchar (6) not null,
study_hours_per_day float not null,
social_media_hours_per_day float  not null,
netflix_hours_per_day float  not null,
part_time_job char(3) not null,
attendance_percentage float  not null,
sleep_hours  float  not null,
diet_quality char (4) not null,
exercise_frequency int not null,
parental_education_level char (15) not null,
mental_health_rating int not null,
extracurricular_participation char (3) not null,
exam_score int not null
);
Alter table Habit_and_performance Add internet_quality char (8) not null;
Alter table Habit_and_performance modify exam_score float not null;
desc habit_and_performance;
insert into habit_and_performance values 
('S1000', 23, 'Female', 0, 1.2, 1.1, 'No', 85, 8, 'Fair', 6, 'Master', 8, 'Yes', 56.2, 'Average'),
('S1001', 20, 'Female', 6.9, 2.8, 2.3, 'No', 97.3, 4.6, 'Good', 6, 'High School', 8, 'No', 100, 'Average'),
('S1002', 21, 'Male', 1.4, 3.1, 1.3, 'No', 94.8, 8, 'Poor', 1, 'High School', 1, 'No', 34.3, 'Poor'),
('S1003', 23, 'Female', 1, 3.9, 1, 'No', 71, 9.2, 'Poor', 4, 'Master', 1, 'Yes', 26.8, 'Good'),
('S1004', 19, 'Female', 5, 4.4, 0.5, 'No', 90.9, 4.9, 'Fair', 3, 'Master', 1, 'No', 66.4, 'Good'),
('S1005', 24, 'Male', 7.2, 1.3, 0, 'No', 82.9, 7.4, 'Fair', 1, 'Master', 4, 'No', 100, 'Average'),
('S1006', 21, 'Female', 5.6, 1.5, 1.4, 'Yes', 85.8, 6.5, 'Good', 2, 'Master', 4, 'No', 89.8, 'Poor'),
('S1007', 21, 'Female', 4.3, 1, 2, 'Yes', 77.7, 4.6, 'Fair', 0, 'Bachelor', 8, 'No', 72.6, 'Average'),
('S1008', 23, 'Female', 4.4, 2.2, 1.7, 'No', 100, 7.1, 'Good', 3, 'Bachelor', 1, 'No', 78.9, 'Good'),
('S1009', 18, 'Female', 4.8, 3.1, 1.3, 'No', 95.4, 7.5, 'Good', 5, 'Bachelor', 10, 'Yes', 100, 'Good'),
('S1010', 19, 'Female', 4.6, 3.7, 0.8, 'No', 77.6, 5.8, 'Fair', 1, 'None', 3, 'No', 63.3, 'Good'),
('S1011', 23, 'Male', 3.9, 2.4, 2.5, 'No', 71.7, 7.9, 'Fair', 2, 'Bachelor', 1, 'No', 74.4, 'Average'),
('S1012', 19, 'Female', 3.7, 2.1, 0.4, 'Yes', 81.1, 4.5, 'Fair', 1, 'Bachelor', 9, 'No', 76.9, 'Good'),
('S1013', 19, 'Female', 3.4, 2.7, 2.7, 'No', 89.3, 4.7, 'Fair', 4, 'Bachelor', 10, 'No', 75.8, 'Good'),
('S1014', 24, 'Male', 2.4, 1.5, 0.7, 'No', 87.4, 6.7, 'Poor', 6, 'Bachelor', 9, 'No', 78.9, 'Average'),
('S1015', 21, 'Male', 3.1, 5, 1, 'No', 97.5, 6.5, 'Good', 6, 'High School', 7, 'No', 74, 'Average'),
('S1016', 20, 'Male', 1, 0.6, 0.2, 'No', 92.9, 5.6, 'Poor', 3, 'High School', 8, 'Yes', 55.2, 'Poor'),
('S1017', 24, 'Female', 3.4, 2.7, 1.2, 'No', 94.7, 7.5, 'Poor', 0, 'High School', 1, 'Yes', 70.8, 'Average'),
('S1018', 22, 'Male', 2,  4.9, 2.9, 'Yes', 88.3, 7.1, 'Good', 2, 'High School', 5, 'No', 43.9, 'Good'),
('S1019', 23, 'Male', 1.8, 2.5, 2.4, 'No', 71.1, 7.5, 'Fair', 1, 'High School', 2, 'No', 45.3, 'Average'),
('S1020', 22, 'Female', 3.8, 2.3, 2.9, 'No', 83, 6.4, 'Good', 3, 'Master', 1, 'No', 58.5, 'Good'),
('S1021', 21, 'Male', 5.6, 2.1, 2.4, 'No', 95.6, 7.2, 'Fair', 1, 'High School', 3, 'No', 82.5, 'Good'),
('S1022', 18, 'Female', 4.9, 2.3, 0.6, 'No', 84.5, 6, 'Fair', 3, 'High School', 7, 'No', 98.7, 'Average'),
('S1023', 24, 'Female', 1.1, 4.1, 1.4, 'Yes', 90, 9, 'Fair', 6, 'Bachelor', 1, 'No', 43.7, 'Good'),
('S1024', 20, 'Female', 2, 0, 0.9, 'Yes', 81.8, 5.5, 'Fair', 4, 'Bachelor', 2, 'No', 54.9, 'Average'),
('S1025', 22, 'Male', 4.9, 4.3, 3.3, 'No', 74.7, 9, 'Fair', 1, 'High School', 2, 'Yes', 69.9, 'Average'),
('S1026', 22, 'Male', 2, 0.8, 0.5, 'No', 83.8, 6.5, 'Good', 4, 'Bachelor', 4, 'No', 73.5, 'Poor'),
('S1027', 18, 'Male', 3.2, 2.2, 2.8, 'Yes', 88.1, 4.8, 'Fair', 5, 'Bachelor', 3, 'No', 71.1, 'Average'),
('S1028', 24, 'Male', 4.3, 2, 2.8, 'Yes', 78.4, 8.1, 'Good', 5, 'High School', 3, 'Yes', 82.8, 'Poor'),
('S1029', 20, 'Female', 2, 3.2, 3.8, 'Yes', 82.6, 6.7, 'Poor', 6, 'High School', 10, 'Yes', 75.7, 'Poor'),
('S1030', 21, 'Female', 3.7, 0.6, 1.3, 'No', 75.6, 7.5, 'Fair', 2, 'Master', 5, 'No', 70.6, 'Average');
select * from habit_and_performance;

 
-- Data management and Data cleaning:

-- step 1 : identify Data Issues
/**
1. check for missing values: 
this identity row with missing values  
 **/
select * from habit_and_performance where 
student_id and age  is null;

/**
2. check for duplicate:
using Group by  and having clause to identity duplicate rows
count(*) : means it counting the numbers of 
 rows in your table have the same value with age column
**/
select age, count(*) as count from habit_and_performance
group by age having count(*) > 1;

/**
3. check for data type inconsistencies 
  to identity row with incorrect data types 
  not like %[0-9]% for sql server
  not like operator is use to exclude rows that match a specific 
  pattern
**/
select * From habit_and_performance where parental_education_level  regexp '^[a-zA-Z]+$';

-- Step 2 : Handling  Missing Values 
/**
1. replace missing values with a value
**/
update habit_and_performance set part_time_job = 'Yes' where part_time_job is null;

/** 
2. delete row with missing values 
**/
delete from habit_and_performance where part_time_job is null;

-- Step 3 : Remove Duplicates
/**
1. using the Distinct keyword
**/
select distinct age from habit_and_performance;
/** 
2.  use Row_Number() function to assign a unique row number
    to each row and delete duplicates
**/

