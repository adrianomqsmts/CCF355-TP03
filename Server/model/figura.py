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
    if value >= 25:
        cards = buyAction(id_user, value)
        addCard(id_user, cards)
        result = []
        show(cards, result)
        result.append(str(value - 25))

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
    var = (value - 25, id_user)
    mycursor.execute(sql, var)
    mydb.commit()
    summon(cards)
    return cards


def summon(cards):
    for i in range(3):
        x = randint(1, 51)
        cards.append(x)


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


def sell(id_user, id_figure):
    mydb = conn.connect()
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM album WHERE idFigure = %s and idUser = %s"
    var = (id_figure, id_user)
    mycursor.execute(sql, var)
    data = mycursor.fetchone()
    quantity = data['quantity']
    if data and quantity > 1:
        result = sellAction(id_user, id_figure, quantity)
    else:
        result = {
            'response': False,
        }
    return result


def sellAction(id_user, id_figure, quantity):
    mydb = conn.connect()
    mycursor = mydb.cursor(dictionary=True)
    sql = "UPDATE album SET quantity = %s WHERE idUser = %s and idFigure = %s"
    var = (quantity - 1, id_user, id_figure)
    mycursor.execute(sql, var)
    mydb.commit()
    data = addBalance(id_user, id_figure)
    return data


def addBalance(id_user, id_figure):
    mydb = conn.connect()
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM usuario WHERE idUser = %s"
    var = (id_user,)
    mycursor.execute(sql, var)
    data1 = mycursor.fetchone()
    balance = data1['balance']
    sql = "SELECT * FROM figure WHERE idFigure = %s"
    var = (id_figure,)
    mycursor.execute(sql, var)
    data2 = mycursor.fetchone()
    rarity = data2['rarity']
    price = getPrice(rarity)
    sql = "UPDATE usuario SET balance = %s WHERE idUser = %s"
    var = (balance + price, id_user,)
    mycursor.execute(sql, var)
    mydb.commit()
    result = {'name': data2['name'],
              'price': price,
              'balance': data1['balance'] + price
              }
    return result


def getPrice(rarity):
    if rarity == "comum":
        return 5
    elif rarity == "rare":
        return 15
    elif rarity == "epic":
        return 25
