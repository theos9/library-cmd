import sqlite3
import os


class connect_db:
    def connect():
        connection = sqlite3.connect("./library_database.db")
        cursor = connection.cursor()
        sql = """
            CREATE TABLE IF NOT EXISTS books(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME VARCHAR(150),
            AUTHOR VARCHAR(60),
            YEAR INTEGER,
            PRICE INTEGER,
            CAPTION VARCHAR(200),
            ADDRESS VARCHAR(60)
            );
        """
        cursor.execute(sql)
        connection.commit()
        connection.close()


class order:
    def input_order():
        list_of_orders = ["insert", "show",
                          "update", "open", "search", "delete", "help"]
        while True:
            user_order = input("what do you want? : ").lower()
            if user_order == "q" or user_order == "exit":
                break
            elif user_order not in list_of_orders:
                print("that order does not in my list pls check 'help'!")
            elif user_order in list_of_orders:
                order.processing_user_order(user_order)

    def processing_user_order(user_order):

        if user_order == "insert":
            name_of_book = input("enter name of book : ")
            author_of_book = input("enter author of book : ")
            year_of_book = input("enter year of book : ")
            price_of_book = input("enter price of book : ")
            caption_of_book = input("enter caption of book : ")
            address_of_book = input("enter address of book : ")
            call_insert_func = insert(name_of_book, author_of_book, year_of_book,
                                      price_of_book, caption_of_book, address_of_book)
            call_insert_func.insert_user_data()

        elif user_order == "show":
            show.show_all()

        elif user_order == "update":
            list_column_can_changing = [
                "NAME", "AUTHOR", "YEAR", "PRICE", "CAPTION", "ADDRESS"]
            id_of_changing = int(input("Which ID do you want to change? : "))
            while True:
                column_of_changing = input(
                    "Which COLUMN do you want to change? : ").upper()
                if column_of_changing in list_column_can_changing:
                    if column_of_changing == "year" or column_of_changing == "price":
                        column_of_changing = int(column_of_changing)
                        break
                    else:
                        break
                else:
                    print("i cant change this column pls choose another...")
            change = input("enter your new details : ")
            call_update_func = update(
                id_of_changing, column_of_changing, change)
            call_update_func.update_book()

        elif user_order == "search":
            name_of_book = input("enter name of book : ")
            author_of_book = input("enter author of book : ")
            year_of_book = input("enter year of book : ")
            price_of_book = input("enter price of book : ")
            caption_of_book = input("enter caption of book : ")
            address_of_book = input("enter address of book : ")
            call_search_func = search(
                name_of_book, author_of_book, year_of_book, price_of_book, caption_of_book, address_of_book)
            call_search_func.search_book()
        elif user_order == "delete":
            list_of_confirmation = ["y", "n"]
            id_of_book = input(
                "Enter the ID of the book you want to delete : ")
            while True:
                confirmation_delete = input(
                    f"are you sure about delete ID={id_of_book} [y = yes ,n = no] :").lower()
                if confirmation_delete in list_of_confirmation:
                    if confirmation_delete == "y":
                        call_delete_func = delete(id_of_book)
                        call_delete_func.delete_book()
                        break
                    elif confirmation_delete == "n":
                        print("delete canceled !")
                        break
                else:
                    print("pls just choose y or n ")

        elif user_order == "open":
            id_of_book = input(
                "Enter the ID of the book you want to open : ")
            call_open_func = open(id_of_book)
            call_open_func.open_book()
        elif user_order == "help":
            help.help_of_library()


class insert:
    def __init__(self, name: str, author: str, year: int, price: int, caption: str, address: str):
        self.name = name
        self.author = author
        self.year = year
        self.price = price
        self.caption = caption
        self.address = address

    def insert_user_data(self):
        try:
            conn = sqlite3.connect("./library_database.db")
            cursor = conn.cursor()
            sql = f"""
                insert into books (NAME,AUTHOR,YEAR,PRICE,CAPTION,ADDRESS)values ('{self.name}','{self.author}','{self.year}','{self.price}','{self.caption}','{self.address}')
            """
            cursor.execute(sql)
            conn.commit()
            conn.close()
            print("The insert order is finished...")
        except:
            print("i cant import data in database! ")


class show:
    def show_all():
        conn = sqlite3.connect("./library_database.db")
        cursor = conn.cursor()
        sql = """
            SELECT * FROM books
        """
        cursor.execute(sql)
        print("\nID | NAME | AUTHOR | YEAR | PRICE | CAPTION | ADDRESS")
        for x in list(cursor):
            print("\n", x)
        conn.commit()
        conn.close()


class update:
    def __init__(self, id_of_changing, column_of_changing, change):
        self.id_of_changing = id_of_changing
        self.column_of_changing = column_of_changing
        self.change = change

    def update_book(self):
        try:
            conn = sqlite3.connect("./library_database.db")
            cursor = conn.cursor()
            sql = f"""
                update books set '{self.column_of_changing}'='{self.change}' where ID={self.id_of_changing}
            """
            cursor.execute(sql)
            conn.commit()
            conn.close()
            print("The update order is finished...")
        except:
            print("i cant update data in database! ")


class search:
    def __init__(self, name: str, author: str, year: int, price: int, caption: str, address: str):
        self.name = name
        self.author = author
        self.year = year
        self.price = price
        self.caption = caption
        self.address = address

    def search_book(self):
        try:
            conn = sqlite3.connect("./library_database.db")
            cursor = conn.cursor()
            sql = f"""
            SELECT * FROM books WHERE NAME='{self.name}' or AUTHOR='{self.author}' or YEAR='{self.year}' or PRICE='{self.price}' or CAPTION='{self.caption}' or ADDRESS='{self.address}'
            """
            cursor.execute(sql)
            print("\nID | NAME | AUTHOR | YEAR | PRICE | CAPTION | ADDRESS")
            for x in list(cursor):
                print(x)
            conn.commit()
            conn.close()
            print("The search order is finished...")
        except:
            print("i cant search data in database! ")


class delete:
    def __init__(self, id):
        self.id = id

    def delete_book(self):
        try:
            conn = sqlite3.connect("./library_database.db")
            cursor = conn.cursor()
            sql = f"""
                DELETE FROM books WHERE ID='{self.id}'
            """
            cursor.execute(sql)
            conn.commit()
            conn.close()
            print("book was deleted! ")
        except:
            print("i cant delete data in database")


class open:
    def __init__(self, id):
        self.id = id

    def open_book(self):
        try:
            conn = sqlite3.connect("./library_database.db")
            cursor = conn.cursor()
            sql = f"""
                SELECT ADDRESS FROM books WHERE ID='{self.id}'
            """
            cursor.execute(sql)
            for y in cursor:
                for x in y:
                    os.system(x)
            conn.commit()
            conn.close()
        except:
            print("i cant open book")


class help:
    def help_of_library():
        sys_help = {
            "insert": "you can add a new book in database",
            "delete": "delete 1 book from database",
            "show": "you can see all books",
            "search": "With any information you have from a book, you can find it with this command",
            "update": "You can use this command to change the information of a book , except ID",
            "open": "If the address of the book is correct, you can open and read it with this command and with the help of books ID , attention: The address must be Local",
            "q": "close program",
            "exit": "close program",
            "help": "with this command you can watch all another commands...",
        }
        for key, value in sys_help.items():
            print(f"\n{key} : {value}")


connect_db.connect()
order.input_order()
