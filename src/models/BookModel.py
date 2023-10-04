import mysql.connector


class BookModel:
    def __init__(self):
        self.db = mysql.connector.connect(
            database="do_an",
            host="127.0.0.1",
            user="root",
            password="bitnami"
        )

        self.c = self.db.cursor()

    """
        Lấy danh sách
    """

    def get_all(self):
        self.c.execute("select * from books")
        return self.c.fetchall()

    """
        Lấy thông tin 1 quyền sách theo id
    """

    def get(self, book_id):
        self.c.execute("select * from books where id=%s", (book_id,))
        return self.c.fetchone()

    """
        Thêm 1 quyển sách
    """

    def add(self, fields):
        response = 0
        print(fields)
        try:
            self.c.execute("INSERT INTO books (title, author, published_date, quality) VALUES (%s, %s, %s, %s)",
                           (fields[0].get(), fields[1].get(), fields[2].get(), fields[3].get()))
            response = self.c.rowcount
            self.db.commit()

        except:
            pass
        return response

    """
        Update 1 quyển sách
    """

    def update(self, fields):
        self.c.execute(
            "UPDATE books SET title = %s, author = %s, published_date = %s, quality = %s WHERE id = %s",
            (
                fields[1].get(),
                fields[2].get(),
                fields[3].get(),
                fields[4].get(),
                fields[0].get()
            ))
        self.db.commit()

        return self.c.rowcount

    """
        Xoá 1 quyển sách
    """

    def delete(self, book_id):
        self.c.execute("DELETE FROM books WHERE id = %s", (book_id,))
        self.db.commit()
        return self.c.rowcount
