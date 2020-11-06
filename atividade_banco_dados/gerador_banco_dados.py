import json
import os

def gerar_BD():
   #samsung
   celular1 = {'marca' : 'SAMSUNG', 'modelo' : 'NOTE 10 LITE', 'tela' : '5', 'valor' : '1999'}
   celular2 = {'marca' : 'SAMSUNG', 'modelo' : 'NOTE 20', 'tela' : '7', 'valor' : '2999'}
   celular3 = {'marca' : 'SAMSUNG', 'modelo' : 'NOTE 20 5G', 'tela' : '7', 'valor' : '3999'}
   celular4 = {'marca' : 'SAMSUNG', 'modelo' : 'NOTE 20 ULTRA', 'tela' : '7', 'valor' : '4999'}
   celular5 = {'marca' : 'SAMSUNG', 'modelo' : 'NOTE 20 ULTRA 5G', 'tela' : '7', 'valor' : '3999'}
   celular6 = {'marca' : 'SAMSUNG', 'modelo' : 'S10 LITE', 'tela' : '6', 'valor' : '2999'}

   #apple
   celular7 = {'marca':'APPLE', 'modelo':'IPHONE 12','tela':'6', 'valor' : '3999'}
   celular8 = {'marca':'APPLE', 'modelo':'IPHONE 12 MINI ','tela':'5', 'valor' : '2999'}
   celular9 = {'marca':'APPLE', 'modelo':'IPHONE 12 PRO ','tela':'6', 'valor' : '4999'}
   celular10 = {'marca':'APPLE', 'modelo':'IPHONE 12 PRO MAX ','tela':'7', 'valor' : '5999'}
   celular11= {'marca':'APPLE', 'modelo':'IPHONE SE ','tela':'5', 'valor' : '2999'}
   celular12 = {'marca':'APPLE', 'modelo':'IPHONE 11','tela':'5', 'valor' : '2999'}
   celular13 = {'marca':'APPLE', 'modelo':'IPHONE 11 PRO ','tela':'6', 'valor' : '3999'}
   celular14 = {'marca':'APPLE', 'modelo':'IPHONE 11 PRO MAX ','tela':'7', 'valor' : '5999'}

   #motorola
   celular15 = {'marca':'MOTOROLA', 'modelo':'MOTO E6 PLAY','tela':'5', 'valor':'999', }
   celular16 = {'marca':'MOTOROLA', 'modelo':'MOTO E6 PLUS','tela':'6', 'valor':'999', }
   celular17 = {'marca':'MOTOROLA', 'modelo':'MOTO G7','tela':'5', 'valor':'1999', }
   celular18 = {'marca':'MOTOROLA', 'modelo':'MOTO G7 PLAY','tela':'5', 'valor':'1200', }
   celular19 = {'marca':'MOTOROLA', 'modelo':'MOTO G7 PLUS','tela':'6', 'valor':'1700', }
   celular20 = {'marca':'MOTOROLA', 'modelo':'MOTO G7 POWER','tela':'6', 'valor':'1999', }
   celular21 = {'marca':'MOTOROLA', 'modelo':'MOTO G8 PLAY','tela':'5', 'valor':'999', }
   celular22 = {'marca':'MOTOROLA', 'modelo':'MOTO G8 PLUS','tela':'6', 'valor':'1800', }
   celular23 = {'marca':'MOTOROLA', 'modelo':'MOTO Z4','tela':'6', 'valor':'2999'}

   estoque_celulares = [celular1, celular2, celular3, celular4, celular5, celular6, 
      celular7, celular8, celular9, celular10, celular11, celular12, celular13, 
      celular14, celular15, celular16, celular17, celular18, celular19, celular20, 
      celular21, celular22, celular23]


   arquivo = open ('BD_celulares.json', 'w') #Se o arquivo não existir, será criado 'W'

   transformar_json = json.dumps(estoque_celulares) #transforma para a estrtura do json
   arquivo.write(transformar_json)
   arquivo.close()
   os.system('clear')
   print('-----------------------------------------------')
   print('Banco de dados gerado !')
   print('-----------------------------------------------\n')