import pymysql


class MYSQL():
    def __init__(self, host, password, user, port):
        self.host = host
        self.password = password
        self.port = port
        self.user = user

    def connect_sql(self):
        sql = pymysql.connect(host=self.host, password=self.password, port=self.port, charset="utf8mb4")
        cur = sql.cursor(pymysql.cursors.DictCursor)
        print("数据库连接成功")
        return cur

    def select_sql(self, select_list, select_option, database):
        cursor = self.connect_sql()
        sql_cmd = self.get_select_cmd(select_list, select_option, database)
        print("[SQL_CMD]{}".format(sql_cmd))
        cursor.execute(sql_cmd)
        sql_data = cursor.fetchall()
        return sql_data

    def get_select_cmd(self, select_list, select_option, database):
        select_str = ",".join(select_list)
        option_list = []
        for key, value in select_option.item():
            option_list.append("{}={}".format(key, value))
        option = "AND".join(option_list)
        sql_cmd = "SELECT {} FROM {} WHERE {}".format(select_str, database, option)
        return sql_cmd
