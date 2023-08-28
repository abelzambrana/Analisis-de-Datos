import psycopg2

#-----------------------------------------------------------------------------#
def conectar(usuario,clave,servidor,puerto,baseDeDato):
    conexion=None
    try:
        # Connecto a una base de datos existente
        conexion = psycopg2.connect(user=usuario,password=clave,host=servidor,port=puerto,database=baseDeDato)
        # Creo un cursor para hacer operaciones sobre la base de datos conectada
        cursor = conexion.cursor()
        # Ejecuto una consulta SQL
        cursor.execute("SELECT version();")
        # Obtengo el resultado de la consulta SQL
        record = cursor.fetchone()
        print("ligpg.conectar(): Ud esta conectado a: ", record, "\n")
        cursor.close()
        return conexion

    except Exception as error:
        print("libpg.conectar(): Error conectando con PostgreSQL:",error)
        return conexion

    finally:
        return conexion
#-----------------------------------------------------------------------------#
def consultar(conexion,sql):
    tuplas = None
    columnas = None
    dic_cols={} #diccionario columnas:  nombre columna -> posicion
    try:
        if conexion:
            # Creo un cursor para hacer operaciones sobre la base de datos conectada
            cursor = conexion.cursor()
            # Ejecuto una consulta SQL
            cursor.execute(sql)
            #print("libpg.consultar(): Ejecute consulta!")
            tuplas = cursor.fetchall()
            cursor.close()
            columnas = [desc[0] for desc in cursor.description] #devuelve arreglo con nombres de columnas
            i=0
            for col in columnas:
                dic_cols[col]=i
                i=i+1
        return tuplas,dic_cols
    except Exception as error:
        print("libpg.consultar(): Error :",error," en consulta:",sql)
        return tuplas,dic_cols

#-----------------------------------------------------------------------------#
def ejecutar(conexion,sql):
    try:
        if conexion:
            # Creo un cursor para hacer operaciones sobre la base de datos conectada
            cursor = conexion.cursor()
            # Ejecuto una consulta SQL
            cursor.execute(sql)
            conexion.commit()
            cursor.close()
            #print("libpg.ejecutar(): Ejecute consulta!")
            return True
        return False
    except Exception as error:
        print("libpg.ejecutar(): Error :",error," en consulta:",sql)
        return False

#-----------------------------------------------------------------------------#

def desconectar(conexion):
    try:
        if conexion:
            conexion.close()
        print("ligpg.desconectar(): Se desconecto de la base de datos!")
    except Exception as error:
        print("libpg.desconectar(): Error :",error," desconectando base de datos!")

