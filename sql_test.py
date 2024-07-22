from mysql import *
hostname = "127.0.0.1"
user = "root"
port = 3306
password = "123456"
database = "sakila"
sql = MYSQL(hostname,password,user,port,database)
select_list = []
option = {
    "country_id":1
}
data = sql.select_sql(select_list,option,"country")
print(data)