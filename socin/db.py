import mysql.connector

dbsocin = mysql.connector.connect(

        host="10.0.2.15",  
        user="econect",  
        password="123456",
        database="concentrador")              
        
def listar(codigo):

        sql = dbsocin.cursor()

        sql.execute("select login,senha,nome from usuario_security where login="+codigo)

        result = sql.fetchall()

        return result