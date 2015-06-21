def paridade (mensagem) :
	mensagem = list(mensagem)
	for i in range(0, len(mensagem)):
		posicao = 2** i				#encontra os bits de paridade e substitui por *
		if posicao < len(mensagem):
			mensagem.insert(posicao-1, "*")
		else:
			break
	mensagem = "".join(mensagem)
	print mensagem
	return mensagem	
	
def calcularsalto(cadeia): #calcula o proximo bit a ser analisado
	aux = dict()
	x = cadeia.count("*")
	i=0
	while x > i :
		salto = 2**i
		i+=1
		aux[salto] = calcularpar(cadeia, salto) 
	return aux

def calcularpar(cadeia1,salto, aux=""): #checa o bit, função auxiliar de calcularsalto 
	original = cadeia1
	cadeia1 = cadeia1[salto-1:]
	n = "N"*(salto-1)		#insere N para presevar posição
	aux += n 
	n = "N"*salto
	nsalto = salto * 2
	while len(cadeia1) > 0:
		aux += cadeia1[:salto]
		cadeia1 = cadeia1[nsalto:]
		aux += n
	aux = aux[:len(original)]
 
	return aux	

def erros(cadeia2):
	errada = list()
	for indice, valor in cadeia2.items():
		soma = 0
		for elemento in valor:
			for x in elemento:
				if x != "*" and x != "N":
					soma += int(x)
		if soma % 2 != 0: 
			errada.append(indice)
	
	return errada	
def main():
	mensagem = raw_input()
	mensagem = list ()
	cadeia1=paridade(mensagem)
	cadeia2 = calcularsalto(cadeia1)
	cadeia = erros(cadeia2)
	print "Erros:\n", cadeia
main()
