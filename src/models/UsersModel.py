import mysql.connector


class UsersModel:
    def __int__(self):
        self.db = mysql.connector.connect(
            database="do_an",
            host="127.0.0.1",
            user="root",
            password="bitnami"
        )

        self.c = self.db.cursor()

    """
        Check user tồn tại
    """

    def get_username(self, username):
        self.c.execute("select * from users where username=%s", (username,))
        return self.c.fetchone()

    """
        Lấy danh sách users
    """

    def get_all(self):
        self.c.execute("select * from users")
        return self.c.fetchall()

    """
        Thêm 1 user 
    """

    def add(self, fields):
        response = 0
        print(fields)
        try:
            self.c.execute("INSERT INTO users (username, isAdmin) VALUES (%s, %s)",
                           (fields[0].get(), fields[1].get()))
            response = self.c.rowcount
            self.db.commit()

        except:
            pass
        return response

    """
        Update 1 Users
    """

    def update(self, fields):
        self.c.execute(
            "UPDATE users SET isAdmin = %s WHERE id = %s",
            (
                fields[1].get(),
                fields[0].get()
            ))
        self.db.commit()

        return self.c.rowcount

    """
        Xoá 1 user 
    """

    def delete(self, user_id):
        self.c.execute("DELETE FROM users WHERE id = %s", (user_id,))
        self.db.commit()
        return self.c.rowcount
