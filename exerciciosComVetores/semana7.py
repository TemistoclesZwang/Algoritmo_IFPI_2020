from  menu_semana7 import opcoes_menu
def main():

   menu = '*** Brincando com Listas ***'
   menu += '\n 1 - Inserir Valores (caso não escolha essa opção valores padrões seram usados)'
   menu += '\n 2 - Mostrar Valor posição'
   menu += '\n 3 - Remover do Final'
   menu += '\n 4 - Remover do Início'
   menu += '\n 5 - Remover de Posição Específica'
   menu += '\n 6 - Mostrar todos os valores '
   menu += '\n 7 - Inserir valores em Posição Específica'
   menu += '\n 8 - Contagem (número de pares,ímpares,primos,positivos,negativos) '
   menu += '\n 9 - Média valores '
   menu += '\n 10 - Ocorrências de um determinado valor '
   menu += '\n 11 - Dobrar '
   menu += '\n 12 - Apagar todos os valores '
   menu += '\n 13 - Inverter valores da lista '
   menu += '\n 14 - Ordenar a lista '
   menu += '\n 0 - Sair '
   menu += '\n\n Opção >>> '


   lista = [10,35,65,52,20] #valores padrão
   opcoes_menu(lista,menu)

main()

in_