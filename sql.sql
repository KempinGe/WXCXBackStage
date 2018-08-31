drop database WXSCDATABASE;
create database WXSCDATABASE default character set utf8;
use WXSCDATABASE;
create table xh_user_info(
    userId bigint unsigned auto_increment comment '用户索引',
    userNikeName varchar(30) not null comment '用户昵称',
    userGender tinyint not null default 0 comment '性别',
    userAge tinyint unsigned null comment '年龄',
    userPhone char(11)  null comment '手机号码',
    userAvatar varchar(128) null  comment '头像',
    userOpenid char(128) null  comment '用户唯一标示',
    userUnionid char(128) null  comment '用户公共平台标识' ,
    craeteTime datetime not null  default current_timestamp comment '注册时间',
    updateTime datetime not null  default current_timestamp on update current_timestamp comment '更新user的时间',
    primary key (userId),
    unique (userOpenid)
) engine=InnoDB default charset=utf8 comment '用户信息表';


create table xh_goods(
    goodsId bigint unsigned auto_increment comment '商品id',
    goodsImgs varchar(60)  not null comment '商品名称',
    goodsSmallImg varchar(128)  comment '缩略图',
    goodsMinPrice float(6,1)  default 1.0 comment '最低价格',
    goodsOriginPrice float(6,1)  default 1.0 comment '元价格',
    goodsCount int not null default 0 comment '数量',
    goodsInStore tinyint(1) default 1 comment '是否上架',
    craeteTime datetime not null  default current_timestamp comment '时间',
    primary key (goodsId)
)engine=InnoDB default charset=utf8 comment '商品列表';

create table xh_goods_detail(
    goodsDetailId bigint unsigned auto_increment comment '详情id',
    goodsDetailImages TEXT  comment  '详情图片',
    goodsIntroduction TINYTEXT  comment '简介',
    goodsContent   TEXT  comment '介绍',
    goodsComments  int default 0 '评论数',
    goodsComments  TEXT comment '评论',
    goodsId bigint unsigned comment '商品ID',
    primary key (goodsDetailId),
    constraint foreign key (goodsId) references xh_goods(goodsId)
) engine = InnoDB default charset = utf8 comment '评分列表';


#unique 有保证字段唯一性 及 可为这个字段建立索引
#可以用show create table  ***** 来显示创建某张表时候的sql语句