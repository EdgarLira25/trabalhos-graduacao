from unidecode import unidecode
import re
def parse(file_name):
	
	# abre o arquivo para leitura
	with open(file_name, 'r') as arquivo_entrada:
	    # lê o conteúdo do arquivo
		conteudo = arquivo_entrada.read()

	# transforma as letras em minúsculas
	conteudo = conteudo.lower()

	# remove os acentos das vogais
	conteudo = unidecode(conteudo)

	# remove todos os caracteres que não são letras
	conteudo = re.sub(r'[^a-z\s]', '', conteudo)
	conteudo = conteudo.replace('\n', ' ')
	#print(conteudo)

	conteudo = conteudo.split()
	lista = []
	for string in conteudo:
		if string not in lista:
			if len(string) > 4:
				lista.append(string)
		else:
			pass
	dic = open("dicionario.txt", "w")
	for item in lista:
		dic.write(item+"\n")

parse("policarpo_quaresma.txt")