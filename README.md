
# Xây dựng ứng dụng quản lý contact bằng flask

## Về cơ sở dữ liệu

Sử dụng cơ sở dữ liệu SQLite3.

Tạo cơ sở dữ liệu SQLite3 có tên contact.db

Dùng script sau để tạo bảng dữ liệu Contacts

```SQL
CREATE TABLE `Contacts` (
	`ContactId`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`Name`	TEXT NOT NULL,
	`Phone`	TEXT,
	`Address`	TEXT
);
```


## Về form mẫu:

Trang home sẽ hiển thị danh sách các contact đang có trên hệ thống:


![home.png](https://quangvinh86.github.io/img/2018-03-16-Flask/home.png)

###  Trang thêm mới một contact

![Add_phone.png](https://quangvinh86.github.io/img/2018-03-16-Flask/Add_phone.png)

### Cập nhật một contact

![MODIFIES.png](https://quangvinh86.github.io/img/2018-03-16-Flask/Add_phone.png)

### Xoá một contact

![Delete.png](https://quangvinh86.github.io/img/2018-03-16-Flask/delete.png)

### Chuyển trang nếu có truy nhập không hợp lệ
![Error.png](https://quangvinh86.github.io/img/2018-03-16-Flask/404.png)

