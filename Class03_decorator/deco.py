import functools

def my_decorator( f ):
  @functools.wraps( f )
  def processa_f( *args, **kwargs ):
    print("Decorator: Antes de executar f")
    f( *args, **kwargs )
    print("Decorator: Depois de executar f")

  return processa_f


@my_decorator
def minha_funcao():
  print("Minha funcao")


def soma( x,y ):
  print("soma: ".format( x + y ))


if __name__ == '__main__':
  minha_funcao()
  soma(2,3)