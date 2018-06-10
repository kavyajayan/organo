drop table if exists availproducts;
create table availproducts ( sellerid int, item varchar(20),category varchar(20), qty float, unit varchar(20));

drop table if exists orders;
create table orders(buyerid int, sellerid int, item varchar(20), qty float);
