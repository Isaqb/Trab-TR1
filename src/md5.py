import hashlib
class Checamd5():
	def msgenviada(msg):
		m = hashlib.md5()
		m.update(msg)
		return m

	def msgrecebida(msg):
		recebida = hashlib.md5()
		recebida.update(msg)	
		return recebida
