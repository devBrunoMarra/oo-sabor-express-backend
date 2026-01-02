from modelos.restaurantes import Restaurante
from modelos.avaliacao import Avaliacao

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Bruno', 10)
restaurante_praca.receber_avaliacao('Bruna', 8)
restaurante_praca.receber_avaliacao('Emy', 2)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()