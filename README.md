# Software-Engineering-Crud-System-Demo
Enviroment: python3.10
Framework: Flask
Database: MySql

Initial launch of the web is a list of content. e.g.create a new items, list all items etc
In each content, redirection will lead to a new page related to specific operations.

Be sure to create some items before doing other operations, otherwise, the page is empty. 
Meanwhile, please MySql should be set up in advance in order to make the crud system work properly. 
Specific info on MySql configuration is in mysql_database.py.

1. main page
![1](https://user-images.githubusercontent.com/45372265/181102970-4a7b624e-5ab3-4c06-94c6-0e58dc5abe96.png)

2. create new item
![2](https://user-images.githubusercontent.com/45372265/181103001-559d63e3-5db9-4821-bcc6-e45068d5a530.png)

3.list all items
![3](https://user-images.githubusercontent.com/45372265/181103018-8ecb0424-6f91-4ef1-916b-fe71aaf4c06b.png)

4.update an item
![4](https://user-images.githubusercontent.com/45372265/181103030-735bce4c-0fb1-4705-8e85-80a49c4cb0e2.png)

5. result of updating an item
![5](https://user-images.githubusercontent.com/45372265/181103041-830ba9aa-1df6-4628-bc08-675a2e7e218e.png)

For deletion, the result will be a list of all items except the one deleted. 
