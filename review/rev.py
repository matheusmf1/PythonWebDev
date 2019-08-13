
lista = [1,2,3,4]
lista = [ x*2 for x in range(5) ]

#tupla é imutavel
tup = ( 1,2,"tripla",560 )

#dicionario - chave:valor
dict = { "oi":560,2:"tchau" }

#nao ordenavel e nao repete valor
#manipulacao de indices
conjunto = {1,2,3,4,4}


def func( nome="Rola", idade=18, end = "SCS" ):
    print( "nome {}, idade {}, mora {} ".format(nome,idade,end) )

def someTudo( *args ):
    res = sum( args )
    print( "A soma é: ".format(res))
    print( args )
    print( type(args))


#__something__ é uma convencao para variaveis internas do python

# print( "rev" )
# print(__name__)
# main é o arquivo do seu namespace

def do():
    # print("rev")
    # print(__name__)


    # func("Matheus", 22, "SCS")
    # func()
    # func( idade = 24)

    someTudo(1,15,2,4)


if __name__ == "__main__":
    do()