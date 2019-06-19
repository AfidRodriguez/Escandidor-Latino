


pass
#archivo=open("greek2.txt","r")
#Corpus = archivo.read()
#lema=open("Greek_Dic.py","w")
#lema.write(Corpus.replace('a','a'))

from Misintentos import latina
from corpus import todo

# busca la palabra en el diccionario y bota los significados
def lematizador(word):
	return latina.get(word)


sisas=['  alba_,alba#1\ta white precious stone\tfem abl sg', '  alba#1\ta white precious stone\tfem nom/voc sg', '  album\t \tneut nom/voc/acc pl', '  albus\twhite\tneut nom/voc/acc pl', '  alba_,albus\twhite\tfem abl sg', '  albus\twhite\tfem nom/voc sg']	
#a cada elemento de la lista lo vuelve string. por qué uno solo me bota?
def distribuidor(lista):
	if len(lista) > 1:
		for i in lista:
			print("Opción")
			print(todo(i))
			
	elif len(lista)<2:
		for i in lista:
			print('Sólo puedo ser :')
			print(todo(i))
	
	

	


#Da la lista de opciones que tiene una palabra
def concatenador(word):
	return distribuidor(lematizador(word))

#coje todo el texto y a acada una lematiza
def oradero(texto):
	for word in texto.split(' '):
		print("-------------------")
		print('para', word,'tenemos')
		concatenador(word)
		print("-------------------")


cosa=input('Ponga una oración o palabra para analizar: ')
cosita= str(cosa)
oradero(cosita)


