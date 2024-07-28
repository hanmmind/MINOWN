from mysql import *
from sql_configue import *
database = "sakila"
sql = MYSQL(hostname,password,user,port,database)
select_list = []
option = {
    "country_id":"'1'",
    "country IN":"('Afghanistan')"
}
data = sql.select_sql(select_list,option,"country")
print(data)

sql = MYSQL(hostname,password,user,port,database)
insert_option = {
    "country_id":"'110'",
    "country":"'minhan'",
    "last_update":"'2024-07-28 22:08:59'"
}
sql.insert_sql(insert_option,"country")