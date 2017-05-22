#!/usr/bin/python
# -*- encoding: utf-8 -*-


#import
import os, sys, math


#funcoes

def limpar():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

def binario(num):
	if num == 0:
		return ""
	return binario(num//2) + str(num%2)
	
def zeros(val, nstring):
	while len(val) < nstring:
		val = "0" + val
	return val

def res(nstring):
	pos = 1
	for i in range(nstring):
		pos = pos * 2
	return pos

def swap(result, l, r):
	t = result[l]
	result[l] = result[r]
	result[r] = t
	return result
	
def toString(List):
	return ''.join(List)

def magica(result, l, r):
	if l==r:
		wordlist.write(toString(result) + "\n")
	else:
		#embaralha as palavras chaves criandos todas as tentativas possiveis
		for i in range(l, r + 1):
			result = swap(result, l, i)
			magica(result, l + 1, r) 
			result = swap(result, l, i)
			
def wcount(nstrings):
	words = 0 
    total = 0 
    for i in range(1, nstrings + 1): 
        words = (math.factorial(nstrings) / math.factorial(nstrings - i)) 
        total = total + words 
    return int(total)  #Retorna o numero de senhas a serem gravados
	
def checanum(): # checa se o valor inserido é numerico ou nao
	while True:
		nkeywords = raw_input("Numero de palavras chaves: ")
		try:
			nkeywords = int(nkeywords)
		except ValueError:
			print ("[!] Valor invalido")
		if type(nkeywords) == int:
			return nkeywords
			
def banner():
	print """
	           ______________
      ,===:'.,            `-._
           `:.`---.__         `-._
             `:.     `--.         `.
               \.        `.         `.
       (,,(,    \.         `.   ____,-`.,
    (,'     `/   \.   ,--.___`.'
,  ,'  ,--.  `,   \.;'         `
 `{D, {    \  :    \;
   V,,'    /  /    //
   j;;    /  ,' ,-//.    ,---.      ,
   \;'   /  ,' /  _  \  /  _  \   ,'/
         \   `'  / \  `'  / \  `.' /
          `.___,'   `.__,'   `.__,'
	
	
[+] Autor: Pablo Santhus
[+] Data: 22/05/2017
[+] Name: Gerador Wordlist Keywords
[+] GitHub: /pablosanthus
[+] Facebook: /pablosanthus
[+] Youtube: /0xsec

		
	"""

	
while True:
	
	limpar()
	banner()
	
	strings = []
	parlist = []
	result = []
	
	name = raw_input("Wordlist Ex:(NAME.txt)>> ")
	ext = name.split(".")
	if ext[1] == "txt":
		wordlist = open(name, "w")
	else:
		print ("[!] Extensao Invalida")
		
	nkeywords = checanum()
	for i in range(nkeywords):
		strings.append(raw_input("Palavra Chave %s: " % (i + 1)))
		
	nstring = len(strings)
	pos = res(nstring)
	
	cont = wcount(nstring)
	break
	
print ("\n")
print ("[+] Iniciando...")
print ("[+] Analisando Palavras Chaves")
print ("[+] Escrevendo Palavras na wordlist")
print ("[+] %s Combinacões Possiveis" % (cont))
print ("\n")
	
	
for i in range(pos):
	par = zeros((binario(i)), nstring)
	for letras in par:
		parlist.append(letras)
	for i in range(len(parlist)):
		if parlist[i] != "0":
			result.append(strings[i])
	if (len(result) - 1 != -1):
		magica(result, 0, len(result) - 1)
		
		
	parlist = []
	result = []

print ("[+] Finalizado com sucesso, salvo em %s" % (name))
