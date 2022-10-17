<h2>What is this?  :neckbeard:  </h2>
    <dt>A simple web-form (username/email), that uses POST and GET methods to write or get data to/from MySQL database and its all ran under Flask.</dt>
now dive! 
<h2>How can i run this?  :leftwards_arrow_with_hook:  </h2>  

There are couple of things you need to do in order to run this simple project.<br>
1. Its utter important to check  `requirements.txt`  first and add your missing packages/modules.
Ofcourse, if you want to install all the packages/modules from `requirements.txt` , you can use:<br> 

>$ pip install -r requirements.txt --no-index --find-links file:///tmp/packages

[this is the explanation](https://stackoverflow.com/a/10429168/3114307) of what the above line does.

2. You should make a database with two columns.<br>
I used XAMPP's integrated MySQL MariaDB 10.1.34. You can check `sidenote.txt` for detailed explanation of how to do this! And ofcourse you can skip the sidenote if you can access MySQL through cmd or phpMyAdmin.

Creating a database in MySQL's prompt:

`CREATE DATABASE flaskapp;`

now we need to use the created database:

`USE flaskapp;`

this is to create a table, we're going to use:

`CREATE TABLE users(name varchar(20), email varchar(40));`

and now lets make a query to the database and make sure its empty:

`SELECT * FROM users;`

    
The second thing you need to do is simply open `cmd`, go to the directory where you cloned/downloaded  `flaskwithMySQL.py`  and simply type
`python flaskwithMySQL.py`
to run it.
The command prompt should give you a link to the page, where the form is. If you haven't touched anything, it should be  `localhost:5000`.

<h2>What is this project written on? What packages/modules were used?  :package:  </h2>

Well the packages you need are written in  `requirements.txt`  , but here we go anyway:

Installation is made with `pip install <package name>`
<br>

 * <b>Python 2.7.15</b> - If you don't have this, you can download it from [python.org/downloads](https://www.python.org/downloads/) 
 * <b>pip=18.0</b> - This should be already installed if you're using Python 2 >=2.7.9 or Python 3 >=3.4, but anyway, use  `python -m pip install -U pip`  to upgrade it.
 * <b>Flask=1.0.2</b>
 * <b>Flask-MySQLdb=0.2.0</b>
 * <b>mysqlclient=1.3.13</b>
 * <b>request=1.0.2</b>
 
Ofcourse there are couple of side tools you'll need, if you don't have them yet:
<br>
* <b>wheel=0.32.0</b> - A built-package format for Python. To work with wheel (.whl) file formats.
* <b>setuptools=39.0.1</b> - to easily download, build, install, upgrade, and uninstall Python packages

<h2>Is this free to use/clone?  :free:  </h2>  
    <dt>Yes, its absolutely free!</dt>

<br>

***

I think this is uploaded correctly through GitKraken.
All rights are not reserved, so clone as much as you want.

Adler Ademov


