import controller.connect as conn


def login(name, password):

    mydb = conn.connect()
    mycursor = mydb.cursor(dictionary=True)

    sql = "SELECT * FROM Usuario WHERE name = %s and password = %s"
    var = (name, password, )

    mycursor.execute(sql, var)
    result = mycursor.fetchone()

    return result
