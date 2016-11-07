# coding=UTF-8
# python/app.py
import re

def cadastrar(nomes):
  print 'Digite o nome:'
  nome = raw_input()
  nomes.append(nome)

def remover(nomes):
  print 'Qual nome você gostaria de remover?'
  nome = raw_input()
  nomes.remove(nome)

def alterar(nomes):
  print 'Qual nome vc gostaria de alterar?'
  nome = raw_input()
  
  if(nome in nomes): 
    print 'Digite o Novo Nome:'
    novo_nome = raw_input()
    index = nomes.index(nome)
    nomes[index] = novo_nome

def procurar(nomes):
    print 'Digite nome a procurar:'
    nome_a_procurar = raw_input()
    if(nome_a_procurar in nomes):
      print 'Nome encontrado'
    else:
      print 'Nome não encontrado'  
    
def listar(nomes):
  print 'Listando nomes'
  for nome in nomes:
    print nome
 
def procurar_regex(nomes):
  print('Digite a expressão regular')
  regex = raw_input()
  nomes_concatenados = ' '.join(nomes)
  resultado = re.findall(regex,nomes_concatenados)
  print resultado
    
def menu():
  nomes = []
  escolha = ''
  while(escolha != '0'):    
    print 'Digite: 1 para cadastrar, 2 para remover, 3 para alterar, 4 para procurar, 5 para listar, 6 para procurar by regex, 0 para terminar'
    escolha = raw_input()
    if(escolha == '1'):
      cadastrar(nomes)
    if(escolha == '2'):
      remover(nomes)
    if(escolha == '3'):
      alterar(nomes)
    if(escolha == '4'):
      procurar(nomes)
    if(escolha == '5'):
      listar(nomes)
    if(escolha == '6'):
      procurar_regex(nomes)
      
menu()
