import connect as conn
from random import randint




def buy(id_user):
    mydb = conn.connect()
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM usuario WHERE idUser = %s"
    var = (id_user,)
    mycursor.execute(sql, var)
    result = mycursor.fetchone()
    value = result['balance']
    if value >= 20:
        cards = buyAction(id_user, value)
        addCard(id_user, cards)
        result = []
        show(cards, result)
        result.append(str(value-20))

    else:
        result = {
            'response': False,
        }
    return result


def buyAction(id_user, value):
    cards = []
    mydb = conn.connect()
    mycursor = mydb.cursor(dictionary=True)
    sql = "UPDATE usuario SET balance = %s WHERE idUser = %s"
    var = (value - 20,id_user)
    mycursor.execute(sql, var)
    mydb.commit()
    summon(cards, id_user)
    return cards


def summon(cards, id_user):
    for i in range(3):
        x = randint(1, 101)
        if 1 <= x <= 70:
            cards.append(7)
        elif 70 < x <= 95:
            cards.append(8)
        else:
            cards.append(9)


def addCard(id_user, cards):
    mydb = conn.connect()
    mycursor = mydb.cursor(dictionary=True)
    for i in range(3):
        sql = "SELECT * FROM album WHERE idFigure = %s and idUser = %s"
        var = (cards[i], id_user)
        mycursor.execute(sql, var)
        ver = mycursor.fetchone()
        if ver:
            sql = "UPDATE album SET quantity = %s WHERE idUser = %s and idFigure = %s"
            var = (ver['quantity'] + 1, id_user, cards[i])
            mycursor.execute(sql, var)
        else:
            sql = "INSERT INTO album (idUser,idFigure,quantity) VALUES (%s, %s, %s)"
            var = (id_user, cards[i], 1)
            mycursor.execute(sql, var)
    mydb.commit()


def show(cards, result):
    mydb = conn.connect()
    mycursor = mydb.cursor(dictionary=True)
    for i in range(3):
        sql = "SELECT * FROM figure WHERE idFigure = %s"
        var = (cards[i],)
        mycursor.execute(sql, var)
        result.append(mycursor.fetchone())


