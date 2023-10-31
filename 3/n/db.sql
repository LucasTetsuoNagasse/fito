create database laranja;
use laranja
create table `customers`(
  `_id` int primary key auto_increment,
  `created_at` datetime default current_timestamp,
  `updated_at` datetime default current_timestamp on update current_timestamp,
  `name` varchar(255) not null,
  `address` varchar(255) not null
);
create table `products`(
  `_id` int primary key auto_increment,
  `created_at` datetime default current_timestamp,
  `updated_at` datetime default current_timestamp on update current_timestamp,
  `name` varchar(255) not null unique,
  `price` decimal(10, 2) not null default 0.00,
  `category` varchar(255),
  `description` varchar(255) default ""
);
create table `orders`(
  `_id` int primary key auto_increment,
  `created_at` datetime default current_timestamp,
  `updated_at` datetime default current_timestamp on update current_timestamp,
  `customer` int not null,
  `shipper` int not null unique,
  `status` enum("toReceive", "received") not null default "toReceive",
  `receive_date` datetime not null default (current_date),
  foreign key (`customer`) references `customers`(`_id`),
  foreign key (`shipper`) references `shippers`(`_id`)
);
create table `items`(
  `_id` int primary key auto_increment,
  `created_at` datetime default current_timestamp,
  `updated_at` datetime default current_timestamp on update current_timestamp,
  `order` int not null,
  `product` int not null,
  `price` decimal(10, 2) not null default 0.00,
  `quantity` int not null default 1,
  foreign key (`product`) references `products`(`_id`),
  foreign key (`order`) references `orders`(`_id`)
);
create unique index idx_items on `items` (`order`, `product`);
create table `stock`(
  `_id` int primary key auto_increment,
  `created_at` datetime default current_timestamp,
  `updated_at` datetime default current_timestamp on update current_timestamp,
  `product` int not null,
  `quantity` int not null default 1,
  foreign key (`product`) references `products`(`_id`)
);
create table `shipper`(
  `_id` int primary key auto_increment,
  `created_at` datetime default current_timestamp,
  `updated_at` datetime default current_timestamp on update current_timestamp,
  `name` varchar(255) not null,
  `address` varchar(255) not null
);
create table `supplier`(
  `_id` int primary key auto_increment,
  `created_at` datetime default current_timestamp,
  `updated_at` datetime default current_timestamp on update current_timestamp,
  `name` varchar(255) not null,
  `address` varchar(255) not null
);
create table `payment`(
  `_id` int primary key auto_increment,
  `created_at` datetime default current_timestamp,
  `updated_at` datetime default current_timestamp on update current_timestamp,
  `name` varchar(255) not null,
  `address` varchar(255) not null
);
