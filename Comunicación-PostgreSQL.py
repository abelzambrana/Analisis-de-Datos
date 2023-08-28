import psycopg2
import funPostgreSQL

#----------------------------------------------------------------------------#
def ingresoNum(prompt):#funcion para ingresar la opcion de menu
    while True:
        try:
            opcion = int(input(prompt))
            return opcion
        except Exception as error:
            pass


def menu(titulo,opciones):  #funcion para mostrar el menu
    print("------------------")
    print(titulo)
    n=1
    for opcion in opciones:
        print(f"{n:3} {opcion}")
        n=n+1
    print("  0 Salir!")
    opcion=-1
    while opcion < 0 or opcion >= n:
        opcion = ingresoNum("Ingrese su Opcion:")
    return opcion


#--------------------------------------#
def main():
  conn = None
  opcion = -1
  while opcion != 0:
    opcion=menu("MENU PRINCIPAL",["Conectar","Consultar","Ejecutar","Desconectar"])
    if opcion == 1:
        conn = funPostgreSQL.conectar("postgres","XXXXX","localhost","5432","database")
    elif opcion == 2:
        sql = "SELECT * from localidad"
        tuplas,cols = funPostgreSQL.consultar(conn,sql)
        if (tuplas):
            print("Resultado Consulta:",len(tuplas)," tuplas!")
            columnas = [desc for desc in cols]
            for tupla in tuplas:
                print(f"Codigo Postal: {tupla[0]} Localidad: {tupla[1]}")
                #uso los nombres de columnas de la base de datos
                #print(f"{columnas[0]}:{tupla[0]} {columnas[1]}:{tupla[1]}")
        else:
            print(f"La Consulta: {sql} no dio ningun resultado!")
    elif opcion == 3:
        postal = ingresoNum("Codigo Postal:")
        localidad = input("Localidad:")
        sql = f"insert into localidad(cpostal,nombre) values({postal},'{localidad}')"
        funPostgreSQL.ejecutar(conn,sql)
    else:
        funPostgreSQL.desconectar(conn)

  exit(0)


if __name__=="__main__":
   main()   
#-------------------------------------------------------------------#


