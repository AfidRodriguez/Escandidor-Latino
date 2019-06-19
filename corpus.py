
# Estas funciones trabajan con lo que bota el lematizador
def metrica(string):
	inicio = 0
	fin = string.find(',') 
	return(string[inicio:fin])

def lemma(string):
	inicio = string.find(',')+1
	fin = string.find('\t') 
	return(string[inicio:fin])

def significado(string):
	inicio = string.find('\t')+1
	fin = string.rfind('\t') 
	return(string[inicio:fin])

def morfologia(string):
	inicio = string.rfind('\t')+1  
	return(string[inicio:])

def todo(word):
	print("De pista métrica tenemos: '", metrica(word),"'")
	print( "Es de la palabra '", lemma(word),"'")
	print("El significado común es: '", significado(word),"'")
	print("y su morfología es '",morfologia(word),"'")





#malviajes del análisis
Sa["bstrok"],niom