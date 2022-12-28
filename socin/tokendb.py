import psycopg2
from socin import usuarios as socin

def conecta_db():

  con = psycopg2.connect(host='10.0.200.200', 
                         port='5442',
                         database='tokenbag',
                         user='postgres', 
                         password='qaz123#@!')
  return con

def listar(nome):
        
    con = conecta_db()
    
    sql = con.cursor()

    sql.execute(
    #"SELECT A.nome,A.codigo,B.funcionario_id,B.valor FROM funcionario as A INNER JOIN token_do_funcionario as B ON A.id = B.funcionario_id where A.nome = '"+nome+"' and B.data_do_envio >= current_date"
    "SELECT B.valor,B.data_do_envio::date FROM funcionario as A INNER JOIN token_do_funcionario as B ON A.id = B.funcionario_id where A.nome = '"+nome+"' and B.data_do_envio::date >= (current_date-2)"
    )

    result = sql.fetchall()

    usuario = socin.UsuarioSocin

    usuario.senhahoje = result[2][0]
    usuario.ontem =result[1][1]
    usuario.senhaontem = result[1][0]
    usuario.anteontem = result[0][1]
    usuario.senhaanteontem= result[0][0]

    return usuario

#nome="JANAINA CARVALHO DA SILVA"

#listar(nome)