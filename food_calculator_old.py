# declaracao de controle de execucao
executa_progama = True
executa_distribuicao = True

# declaracao de contadores de alinmento para cada tipo de familia
alimentos = 0
contador_familia_1_pessoa = 0
contador_familia_2_3_pessoas = 0
contador_familia_4_5_pessoas = 0
contador_familia_6_pessoas = 0



def balanceador(familia):
	if familia == "familia_6_pessoas":
		global contador_familia_6_pessoas
		global alimentos

		if familia_4_5_pessoas is not 0:
			resto = contador_familia_6_pessoas - contador_familia_4_5_pessoas
			while resto > 2:
				contador_familia_6_pessoas = contador_familia_6_pessoas -1 
		 		alimentos = alimentos + familia_6_pessoas
		 		resto = resto - 1

		elif familia_2_3_pessoas is not 0:
			resto = contador_familia_6_pessoas - contador_familia_2_3_pessoas
			while resto > 2:
				contador_familia_6_pessoas = contador_familia_6_pessoas -1 
		 		alimentos = alimentos + familia_6_pessoas
		 		resto = resto - 1

		elif familia_1_pessoa is not 0:
			resto = contador_familia_6_pessoas - contador_familia_1_pessoa
			while resto > 2:
				contador_familia_6_pessoas = contador_familia_6_pessoas -1 
		 		alimentos = alimentos + familia_6_pessoas
		 		resto = resto - 1

	elif familia == "familia_5_pessoas":
		global contador_familia_4_5_pessoas
		global alimentos 

		if familia_2_3_pessoas is not 0:
			resto = contador_familia_4_5_pessoas - contador_familia_2_3_pessoas
			while resto > 2:
				contador_familia_4_5_pessoas = contador_familia_4_5_pessoas -1 
		 		alimentos = alimentos + familia_2_3_pessoas
		 		resto = resto - 1
		 		
		elif familia_1_pessoa is not 0:
			resto = contador_familia_4_5_pessoas - contador_familia_1_pessoa
			while resto > 2:
				contador_familia_4_5_pessoas = contador_familia_4_5_pessoas -1 
		 		alimentos = alimentos + familia_2_3_pessoas
		 		resto = resto - 1 		 		
	else:
		global contador_familia_2_3_pessoas
		global alimentos
		if familia_1_pessoa is not 0:
			resto = contador_familia_2_3_pessoas - contador_familia_1_pessoa
			while resto > 2:
				contador_familia_2_3_pessoas = contador_familia_2_3_pessoas -1 
		 		alimentos = alimentos + familia_1_pessoa
		 		resto = resto - 1 		 			 		

def reset_contadores():
	global contador_familia_1_pessoa
	global contador_familia_2_3_pessoas
	global contador_familia_4_5_pessoas
	global contador_familia_6_pessoas
	global alimentos

	contador_familia_1_pessoa = 0
	contador_familia_2_3_pessoas = 0
	contador_familia_4_5_pessoas = 0
	contador_familia_6_pessoas = 0
	alimentos = 0


def imprime_contadores():
	print "\n"
	print "Quantidade de alimentos para distribuir para a familia de 1 pessoa: " + str(contador_familia_1_pessoa) 
	print "Quantidade de alimentos para distribuir para a familia de 2 a 3 pessoas: " + str(contador_familia_2_3_pessoas) 
	print "Quantidade de alimentos para distribuir para a familia de 4 a 5 pessoas: " + str(contador_familia_4_5_pessoas) 
	print "Quantidade de alimentos para distribuir para a familia de 6 ou mais pessoas: " + str(contador_familia_6_pessoas)

def imprime_alimento_restantes(alimentos):
	print "Sobraram " + str(alimentos) + " que nao serao distribuidos"
	print "\n"
	
try:
	print "\n"
	# Recebe input do usuario no teclado e armazena nas variaveis 
	familia_1_pessoa    = input("Numero de familias de 1 pessoa: ")
	familia_2_3_pessoas = input("Numero de familias de 2-3 pessoas: ") 
	familia_4_5_pessoas = input("Numero de familias de 4-5 pessoas: ")
	familia_6_pessoas   = input("Numero de familias +6 pessoas: ")

	# Pula uma linha no console
	# print "\n"

	while executa_progama:
		
		reset_contadores()

		# Recebe input de alimentos para a divisao 
		
		global alimentos 
		alimentos = input("Quantidade de alimentos para ser dividido: ")

		while True:
			# Checagem da familia com mais de 6 pessoas
			if familia_6_pessoas is not 0:
				if alimentos >= familia_6_pessoas :
					alimentos = alimentos - familia_6_pessoas
					contador_familia_6_pessoas = contador_familia_6_pessoas + 1

				else:
					balanceador("familia_6_pessoas")	
					imprime_contadores()
					imprime_alimento_restantes(alimentos)	
					break

			# Checagem da familia com 4 a 5 pessoas
			if familia_4_5_pessoas is not 0:
				if alimentos >= familia_4_5_pessoas:
					alimentos = alimentos - familia_4_5_pessoas
					contador_familia_4_5_pessoas = contador_familia_4_5_pessoas + 1
				
				elif familia_6_pessoas is 0:
					balanceador("familia_5_pessoas")	
					imprime_contadores()
					imprime_alimento_restantes(alimentos)
					break	

			# Checagem  da familia de 2 a 3 pessoas
			if familia_2_3_pessoas is not 0:
				if alimentos >= familia_2_3_pessoas:
					alimentos = alimentos - familia_2_3_pessoas
					contador_familia_2_3_pessoas = contador_familia_2_3_pessoas + 1
				
				elif familia_6_pessoas is 0 and familia_4_5_pessoas is 0:
					balanceador("familia_3_pessoas")	
					imprime_contadores()
					imprime_alimento_restantes(alimentos)	
					break
			
			# Checagem  da familia de 1 pessoa
			if familia_1_pessoa is not 0:
				if alimentos >= familia_1_pessoa:
					alimentos = alimentos - familia_1_pessoa
					contador_familia_1_pessoa = contador_familia_1_pessoa + 1
				
				elif familia_6_pessoas is 0 and familia_4_5_pessoas is 0 and familia_2_3_pessoas is 0:
				 	imprime_contadores()
					imprime_alimento_restantes(alimentos)	
					break

		controle = raw_input("Deseja calcular a distribuicao de outro alimento?[y/n]")
		print "\n"			
		if controle != "y":
			executa_progama = False


except Exception, e:
	raise e