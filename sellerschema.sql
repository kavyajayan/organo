drop table if exists orders;
create table orders(orderid int, buyerid int, sellerid int, itemid int, qty float);

drop table if exists acceptorders;
create table acceptorders(orderid int, buyerid int, sellerid int, itemid int, qty float);