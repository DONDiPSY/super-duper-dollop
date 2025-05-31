CREATE TABLE ADDRESS(
   ZIP           VARCHAR(12),
   STREET        VARCHAR(200),
   CITY          VARCHAR(100),
   STATE         VARCHAR(100),
   PRIMARY KEY (ZIP)
);
CREATE TABLE CUSTOMERS(
   CUST_ID       INT              NOT NULL,
   CUST_NAME     VARCHAR (20)      NOT NULL,
   DOB           DATE,
   ZIP           VARCHAR(12),
   EMAIL_ID      VARCHAR(256),
   PRIMARY KEY (CUST_ID)
);
insert into address values
('12w4', 'Adiyan', 'ijaye', 'Ogun-State'),
('1e24', 'Agbado', 'alaye', 'Osun-State'),
('13t4', 'toki', 'Abule-egba', 'Lagos-State')
;
insert into customers values
(1, 'precious', '1995-4-25','12w4','preciousoge@gmail.com'),
(2, 'james', '1992-4-25','1e24','jameswillams@gmail.com'),
(3, 'peter', '1996-4-25','13t4','petermark@gmail.com')
;
select ad.*, cus.cust_id, cus.cust_name, cus.DOB, cus.EMAIL_ID 
from  address  as ad join customers as cus on ad.zip = cus.zip;
alter table customers Add  constraint fk_zip foreign key (ZIP) references address(zip);
desc address;
Drop database if exists tutor;