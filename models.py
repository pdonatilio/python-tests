# -*- coding: utf-8 -*-

class Perfil(object):
  'Classse para moldar perfis de usuarios'

  def __init__(self, nome, telefone, empresa):
    self.nome = nome
    self.telefone = telefone
    self.empresa = empresa
    self.__curtidas = 0  

  def imprimir(self):
    print 'Nome %s, Telefone %s, Empresa %s, Curtidas %s' % (self.nome, self.telefone, self.empresa, self.obter_curtidas())

  def curtir(self):
    self.__curtidas+=1

  def obter_curtidas(self):
    return self.__curtidas
  
  
#Exercícios do Módulo 8  
class Data(object):
  'Classe para exibir uma data no sistema no padrão dia/mês/ano'

  def __init__(self,dia,mes,ano):
    self.dia = dia
    self.mes = mes
    self.ano = ano

  def imprime(self):
    print '%s/%s/%s' % (self.dia,self.mes,self.ano)

class Pessoa(object):
  'Classe para apresentar o IMC do indivíduo'

  def __init__(self, nome, peso, altura):
    self.nome = nome
    self.peso = peso
    self.altura = altura

  def __calcula_imc(self):
    self.imc = (self.peso / (self.altura**2))

  def imprime_imc(self):
    self.__calcula_imc()
    print 'O IMC de %s é %s' %(self.nome, self.imc)
