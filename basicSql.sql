create database evening;
use evening;
create table info(id int,name varchar(25),course varchar(25),
fees float,join_date date);
insert into info value(12,"Naveen","Testing",18900,"2026-06-06");
select * from info;
insert into info value(13,"Mohan","Testing",18900,"2026-06-10");
insert into info value(14,"kokila","Java",15900,"2023-04-01"),
(78,"Jana","Python",16900,"2026-07-07"),
(96,"Kalai","C",10900,"2026-08-08");
select * from info where course="Testing";
select name,fees from info;

set sql_safe_updates=0;
delete from info where name="kalai";
update info set course="Java Fs" where name="kokila";
alter table info drop column id;
alter table info add column phone int;
alter table info modify column phone bigint;

update info set phone=9442207972 where name="kokila";

select now();
select date_format(now(),"%Y-%M-%D");
select date_format(now(),"%y-%m-%d");
select extract(day from join_date) from info;
select extract(month from join_date) from info;
select extract(year from join_date) from info;

select datediff(curdate(),"2006-07-03");
select * from info;
select * from info order by join_date;
select * from info order by join_date desc;

select * from info where name like "M%";
select * from info where name like "_o%";
select * from info where name like "%a";
