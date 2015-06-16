# Trab-TR1
1 Descrição do Projeto
Este trabalho tem como objetivo simular a comunicação entre dois ou mais clientes, utilizando um canal
de comunicação não confiavel como meio compartilhado. Para a implementaçãao desta abstraçao,
devera ser utilizado a arquitetura Cliente  Servidor. O canal nao confiavel sera implementado
como servidor e a conexao entre os clientes devera, obrigatoriamente, passar pelo Canal de Comunicaçao. Ou seja, apos o estabelecimento da comunicaçao entre os clientes e o servidor (canal de comunicaçao), toda a mensagem encaminhada por um cliente origem devera ser recebida, tratada e encaminhadas aos clientes de destino pelo servidor.É importante destacar que o canal de comunicaçao tambem desempenha o papel de encaminhador de mensagens entre os clientes de origem e os de destinos. Para isso, devera ser implementado, na camada aplicaçao, um cabeçalho para a identificaçao dos endereços de origem e destino. Com base nestes identificadores é que o canal de comunicaçao tera condiçoes de fazer o encaminhamento entre
os sockets de comunicaçao abertos.
A figura abaixo apresenta uma representac~ao da arquitetura descrita.
Todas as configuraçoes do Canal e dos clientes deverao ser fornecidas mediante arquivo de configuraçao. Desta forma, espera-se ser possivel obter uma maior exibilizaçao nos parametros fornecidos ao sistema durante a execuçao de diversos experimentos.
1.1 Aplicaçao
A aplicaçao a ser implementada devera gerar, de forma sequencial, numeros inteiros positivos. Este
numeros serao apresentados tanto no cliente origem quanto no cliente destino. O payload das mensagens
geradas pela Camada de Aplicaçao e formado pelos numeros gerados de forma sequencial.
1.2 Cliente
Os clientes dever~ao conectar-se ao servidor (canal) mediante ao estabelecimento de conex~ao socket
utilizando os protocolos TCP e IP. O socket estabelecido e que sera utilizado para encaminhar as
mensagens ao Servidor. Devera ser implementado um cabecalho para as mensagens geradas pela
Camada de Aplicac~ao. Este cabecalho sera utilizado para registrar as seguintes informac~oes:
 Endereco da aplicac~ao de origem;
 Endereco da aplicac~ao de destino;
 Algoritmo de correc~ao aplicado ao payload.
Com base nos cabecalhos das mensagens, o Servidor tera condic~oes de realizar o encaminhamento
das mensagens recebidas para o socket de sada correto. E importante deixar registrado que durante
o processo de estabelecimento do socket, o cliente devera fazer o registro do seu endereco junto
ao Servidor. Somente com este registro e que o servidor tera condic~oes de fazer o mapeamento:
socketn ! clienten;
O cliente origem utilizara o socket da conex~ao estabelecida com o servidor para o encaminhamento
de suas mensagens. Contudo, antes do encaminhamento, e necessario a aplicac~ao do algoritmo de
correc~ao denido no arquivo de congurac~ao. A mensagem recebida pela Camada de Aplicac~ao
(numero inteiro positivo) tera o seu valor convertido para um binario de 32 bits e somente este valor
sera utilizado como entrada em um dos algoritmos denidos (CRC-8, Hamming, MD5 ou SHA1). A
sada resultante sera anexada ao cabecalho da mensagem de aplicac~ao, devidamente preenchido, e
encaminhado pelo socket.
O cliente destino recebera do socket estabelecido com o servidor a mensagem encaminhada pelo
cliente origem. O cabecalho da mensagem fornecera a informac~ao de qual algoritmo de correc~ao foi
aplicado. O cliente destino devera vericar se a mensagem foi recebida de maneira correta. Caso
contrario, devera tentar recuperar a informac~ao original.
1.3 Servidor
O servidor de comunicac~ao emula o comportamento de um canal de comunicac~ao n~ao conavel.
Sendo assim, desempenha dois papeis: a propagac~ao das mensagens e a simulac~ao de erros de comunica
c~ao.
Para realizar a propagac~ao das mensagens, o servidor devera estar apto a estabelecer conex~oes
TCP/IP e fazer o registro dos clientes conectados. Com base no cabecalho das mensagens recebidas,
o servidor fara o encaminhamento das mensagens para o socket que representam a conex~ao
com o clientes destino apropriado.
Page 2
Contudo, antes de fazer o encaminhamento, o servidor devera simular os erros de comunicac~ao. Os
erros possveis est~ao denidos no arquivo de congurac~ao de entrada. S~ao eles: 
ipar bits pares,

ipar bits impares, 
ipar de forma aleatoria de 1 a todos os bits do payload da mensagem, n~ao 
ipar
nenhum bit; Somente os bits do payload da mensagem e que poder~ao ser 
ipados.
2 Algoritmos de Detecc~ao
Para este trabalho, dever~ao ser utilizados os seguintes algoritmos: CRC-8, Hamming, MD5 e SHA1.
Os algoritmos CRC-8 e Hamming dever~ao, obrigatoriamente, ser implementados. Para os algoritmos
MD5 e SHA1 podem ser utilizadas bibliotecas quem possuam a sua implementac~ao.
