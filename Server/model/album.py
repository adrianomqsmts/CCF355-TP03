import connect as conn


def show(id_user):

    mydb = conn.connect()
    mycursor = mydb.cursor(dictionary=True)

    sql = "SELECT * FROM album INNER JOIN figure ON idUser = %s AND album.idFigure = figure.idFigure;"
    var = (id_user, )

    mycursor.execute(sql, var)
    result = mycursor.fetchall()

    return result

