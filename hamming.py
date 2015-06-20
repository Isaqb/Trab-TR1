def paridade (mensagem) : #recebe uma mensagem converte para uma lista e nas posições de bits de paridade insere *
	mensagem = list(mensagem)
	for i in range(0, len(mensagem)):
		posicao = 2** i
		if posicao < len(mensagem):
			mensagem.insert(posicao-1, "*")
		else:
			break
	mensagem = "".join(mensagem)		
	return mensagem	
def calcularparidade(cadeia):
	aux = cadeia
	x = cadeia.count("*")
	i=0
	while x > i :
		salto = 2**i

		while len(cadeia)>0:
			
		i+=1

	return 		
def erros(cadeia):
	for contendo in cadeia.items():
		soma=0
		for elemento in contendo:
			for caracter in elemento:
				if caracter != "*":
					soma += int(caracter)
	return cadeia				
def main():
	mensagem = raw_input()
	cadeia1=paridade(mensagem)
	cadeia2=calcularparidade(cadeia1)	
	cadeia = erros(cadeia2)
	print "Erros:\n", cadeia
main()
