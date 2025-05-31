/*
 granting all privileges to database and table isn't what i want,
 i would prefer having a new database on the user and not granting all access
 to mysql_70 with mysql80
 
*/

Create user 'Dipsy_D_Analyst'@'localhost' identified by 'Rocky@123';
Grant all privileges on *.* to 'Dipsy_D_Analyst'@'localhost' with Grant Option;
flush privileges;


REVOKE GRANT OPTION ON *.* FROM 'Dipsy_D_Analyst'@'localhost';

-- error in statement
grant select , insert on real_lifedb.* to 'Dipsy_D_Analyst'@'localhost';
create database Real_lifedb;
use Real_lifedb;
