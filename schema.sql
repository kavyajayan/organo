drop table if exists users;
    create table users (
    id integer primary key autoincrement,
    email text not null,
    username text not null,
    password text not null,
    phone text not null,
    district text 
);

drop table if exists prices;
	create table prices(
	itemid integer primay key,
	price float not null
);

drop table if exists items;
	create table items(
	itemid integer primary key,
	category text not null,
	item text not null
);

drop table if exists availproducts;
	create table availproducts(
	sellerid integer not null,
	itemid integer not null,
	qty float not null,
	unit integer not null
);


 
