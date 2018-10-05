
class Database(object):
    """测试"""
    def __init__(self, g_db):
        self.g_db = g_db

    def sql_select_total(self):
        sql = 'SELECT * FROM users'
        cur = self.g_db.execute(sql)
        return cur.fetchall()

    def sql_select(self, user_name):
        sql = 'SELECT * FROM users WHERE name=?'
        cur = self.g_db.execute(sql, [user_name])
        cur = cur.fetchone()
        return cur

    def sql_insert(self, user_name, user_password):
        sql = 'INSERT INTO users (name, password) VALUES (?, ?)'
        self.g_db.execute(sql, (user_name, user_password))
        self.g_db.commit()

    def sql_update(self, user_name, new_pwd):
        sql = 'UPDATE users SET password=? where name=?'
        self.g_db.execute(sql, (new_pwd, user_name))
        self.g_db.commit()

