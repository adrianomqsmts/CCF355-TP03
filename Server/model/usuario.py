import controller.connect as conn


def login(name, password):

    mydb = conn.connect()
    mycursor = mydb.cursor(dictionary=True)

    sql = "SELECT * FROM Usuario WHERE name = %s and password = %s"
    var = (name, password, )

    mycursor.execute(sql, var)
    result = mycursor.fetchone()

    return result


def create(name, password):
    mydb = conn.connect()
    mycursor = mydb.cursor(dictionary=True)

    try:
        sql = "INSERT INTO usuario (name, password) VALUES (%s, %s)"
        val = [(name, password)]
        mycursor.executemany(sql, val)
        mydb.commit()
        return 1
    except Exception as e:
        return 0


def update(name, password):
    return 0
