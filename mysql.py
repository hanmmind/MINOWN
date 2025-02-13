import pymysql


class MYSQL():
    def __init__(self, host, password, user, port, database):
        self.host = host
        self.password = password
        self.port = port
        self.user = user
        self.database = database

    def connect_sql(self):
        print("host={}, user={}, password={}, port={}, database={}".format(self.host, self.user, self.password, self.port, self.database))
        sql = pymysql.connect(host=self.host, user=self.user, password=self.password, port=self.port, database=self.database, charset="utf8mb4")
        cur = sql.cursor(pymysql.cursors.DictCursor)
        print("数据库连接成功")
        return sql,cur

    def select_sql(self, select_list, select_option, table):
        db,cursor = self.connect_sql()
        sql_cmd = self.get_select_cmd(select_list, select_option, table)
        print("[SQL_CMD]{}".format(sql_cmd))
        cursor.execute(sql_cmd)
        sql_data = cursor.fetchall()
        db.close()
        return sql_data

    def get_select_cmd(self, select_list, select_option, table):
        if select_list == []:
            select_str = "*"
        else:
            select_str = ",".join(select_list)
        option_list = []
        for key, value in select_option.items():
            if "IN" == key[-2:]:
                option_list.append("{} {}".format(key, value))
            elif "!" == key[-1]:
                option_list.append("{}={}".format(key, value))
            else:
                option_list.append("{}={}".format(key, value))
        option = " AND ".join(option_list)
        sql_cmd = "SELECT {} FROM {} WHERE {}".format(select_str, table, option)
        return sql_cmd
    def insert_sql(self,insert_option,table):
        db,cursor = self.connect_sql()
        sql_cmd = self.insert_sql_cmd(insert_option,table)
        print("[SQL_CMD]{}".format(sql_cmd))
        cursor.execute(sql_cmd)
        db.commit()
        db.close()
    def insert_sql_cmd(self,insert_option,table):
        colum_name_list = []
        value_list = []
        for keys,values in insert_option.items():
            colum_name_list.append(keys)
            value_list.append(values)
        colum_name = ",".join(colum_name_list)
        value = ",".join(value_list)
        sql_cmd = "INSERT INTO {} ({}) VALUES ({})".format(table,colum_name,value)
        return sql_cmd