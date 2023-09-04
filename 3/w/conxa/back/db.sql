create database conxa;
use conxa;
create table Users(
	id int primary key auto_increment not null,
    name varchar(250) unique not null,
    email varchar(250) unique not null,
    password varchar(250) not null,
    description varchar(2000) default "",
    avatar boolean default false,
    created_at datetime default current_timestamp,
    updated_at datetime default current_timestamp on update current_timestamp
);
