from Cliente1 import Recebe
from Cliente1 import Envia
import socket
import sys




if __name__ == "__main__":
	envia = Envia(sys.argv[1])
	#recebe = Recebe(1)
	envia.start()
	#recebe.start()
