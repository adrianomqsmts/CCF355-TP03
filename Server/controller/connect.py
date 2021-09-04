def connect():
    import mysql.connector

    mydb = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="xxZxx280400.",
        database="oneFigure"
    )

    return mydb
