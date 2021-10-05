# Análise e Projeto de Algoritmos
# AC3: Ciência da Computação
#
# Email Impacta: carolina.vieira@aluno.faculdadeimpacta.com.br


def seleciona_aulas(horarios_inicio, horarios_fim):
	"""
	Implemente a função seleciona_aulas(horarios_inicio, horarios_fim) que possui dois parâmetros:
		- horarios_inicio: uma lista de inteiros que representa os horários de início de algumas aulas.
		- horarios_fim: uma lista de inteiros que representa os horários de finalização de algumas aulas.
		Considere que os valores da lista horarios_fim sempre estarão ordenados!
		Considere que as duas listas sempre possuem o mesmo tamanho.
	
	A função deve usar a estratégia gulosa para retornar uma lista com o máximo de aulas
	que podem ser realizadas por uma pessoa, assumindo que a pessoa só pode frequentar uma aula
	de cada vez.
	
	Retorno da função:
		- uma lista de inteiros representando cada uma das aulas que podem ser realizadas
		por uma pessoa, sem que os horários das aulas se sobreponham.
		DICA: crie uma lista vazia dentro da função para isso. Não altere as duas listas
		passadas por parâmetro!

	Como o algoritmo funciona? Suponha o seguinte exemplo:
	Aulas          :  0, 1, 2, 3, 4, 5, ou seja, o "nome" da aula é representado pelo seu índice nas listas.
	horarios_inicio: [1, 3, 0, 5, 8, 5]
	horarios_fim:    [2, 4, 6, 7, 9, 9]
	
	Isto é:
		A aula 0 começa à 1h e termina às 2h.
		A aula 1 começa às 3h e termina às 4h.
		A aula 2 começa à 0h e termina às 6h.
		A aula 3 começa às 5h e termina às 7h.
		A aula 4 começa às 8h e termina às 9h.
		A aula 5 começa às 5h e termina às 9h.
	
	O algoritmo consiste basicamente no seguinte:
		- Passo 1: Selecione (inclua na lista que será retornada pela função) a primeira aula (a "aula 0").
		- Passo 2: Começando da "aula 1", selecione (inclua na lista que será retornada) uma nova aula,
		se seu horário de início é maior ou igual ao horário de finalização da aula previamente selecionada.
		- Passo 3: Repita o Passo 2 até que todas as aulas tenham sido checadas.
	
	Aplicando os passos descritos acima (suponha a variável lista_retorno que contém as aulas selecionadas):
		- lista_retorno = [0], isto é, começando pelo Passo 1, incluimos a "aula 0".
		- A "aula 1" possui horário de início maior ou igual ao horário de fim da "aula 0"?
			Sim, então inclua a "aula 1". Portanto, lista_retorno = [0, 1]
		- A "aula 2" possui horário de início maior ou igual ao horário de fim da "aula 1"?
			Não, então não fazemos nada.
		- A "aula 3" possui horário de início maior ou igual ao horário de fim da "aula 1"?
			Sim, então inclua a "aula 3". Portanto, lista_retorno = [0, 1, 3]
		- A "aula 4" possui horário de início maior ou igual ao horário de fim da "aula 3"?
			Sim, então inclua a "aula 4". Portanto, lista_retorno = [0, 1, 3, 4]
		- A "aula 5" possui horário de início maior ou igual ao horário de fim da "aula 4"?
			Não, então não fazemos nada.
	Ou seja, considerando o exemplo acima, a função deve retornar a lista: [0, 1, 3, 4],
	representando as aulas 0, 1, 3 e 4.
	"""
	lista_retorno = []
	for i in range(len(horarios_fim)):
		if i == 0:
			lista_retorno.append(i)
		if horarios_inicio[i] >= horarios_fim[lista_retorno[-1]]:
			lista_retorno.append(i)
	return lista_retorno

def troco_menores_moedas(carteira, valor_troco):
	"""
	Implemente a função troco_menores_moedas(carteira, valor_troco) que possui dois parâmetros:
		- carteira: uma lista de inteiros que representa as moedas disponíveis em uma carteira.
		Considere que os valores dessa lista sempre estarão ordenados!
		- valor_troco: um inteiro, que representa o valor de um troco a ser pago;
	
	A função deve usar a estratégia gulosa para retornar uma lista de moedas disponíveis
	na carteira que serão utilizadas para pagar esse troco. O seu algoritmo deve utilizar
	as moedas de menor valor que completam o valor do troco.

	Retorno da função:
		- uma lista de inteiros representando cada uma das moedas que serão utilizadas
		para pagar o troco.	DICA: crie uma lista vazia dentro da função para isso. Não altere
		a lista "carteira" passada por parâmetro!
	==============================================
	Exemplo 1:
		Suponha:
			carteira = [1, 1, 1, 1, 2, 2, 10, 25]
			valor_troco = 12
		A função deve retornar uma lista com: [1, 1, 10]

		Como aplicar a estratégia gulosa no caso acima?
		Crie uma lista vazia para poder adicionar as moedas escolhidas.
		Passo 1: percorra a lista (carteira) enquanto o valor do troco não for alcançado ou superado:
			Adicione a moeda de 1; por enquanto a soma é 1, que é menor que 12. Continue!
			Adicione a moeda de 1; por enquanto a soma é 2, que é menor que 12. Continue!
			Adicione a moeda de 1; por enquanto a soma é 3, que é menor que 12. Continue!
			Adicione a moeda de 1; por enquanto a soma é 4, que é menor que 12. Continue!
			Adicione a moeda de 2; por enquanto a soma é 6, que é menor que 12. Continue!
			Adicione a moeda de 2; por enquanto a soma é 8, que é menor que 12. Continue!
			Adicione a moeda de 10; agora a soma é 18. PARE!
		Perceba que escolhemos as seguintes moedas para o troco: [1, 1, 1, 1, 2, 2, 10]
		Mas temos um problema: a soma desses valores é 18.

		Passo 2: agora vamos remover as maiores moedas possíveis, mas que após a remoção a soma ainda
		continue maior ou igual ao valor do troco, isto é, a soma deve continuar maior ou igual a 12.
			Podemos remover a moeda de 10? Não, pois se ela for removida a soma será 8, que é menor que 12.
			Podemos remover a moeda de 2? Sim, se ela for removida a soma será 16, que é maior que 12.
			Podemos remover a moeda de 2? Sim, se ela for removida a soma será 14, que é maior que 12.
			Podemos remover a moeda de 1? Sim, se ela for removida a soma será 13, que é maior que 12.
			Podemos remover a moeda de 1? Sim, se ela for removida a soma será 12, que é maior ou igual a 12.
			Podemos remover a moeda de 1? Não, pois se ela for removida a soma será 11, que é menor que 12.
			Podemos remover a moeda de 1? Não, pois se ela for removida a soma será 11, que é menor que 12.
		Note que no passo 2 tivemos que percorrer a lista de moedas escolhidas de trás para frente.
		Tivemos que remover quatro moedas, nessa ordem: 2, 2, 1, 1.
		Assim, sobraram as moedas de: [1, 1, 10], que será o resultado da função.

		DICA: para remover um índice específico da lista, utilize o método pop(indice) no objeto que representa a lista.
		Por exemplo: se lista = [10, 20, 30, 40, 50], lista.pop(3) remove o elemento 40, e a lista ficaria: [10, 20, 30, 50].
	==============================================
	Exemplo 2:
		Suponha:
			carteira = [5, 5, 5, 5, 10, 10, 10, 25]
			valor_troco = 60
		A função deve retornar uma lista com: [5, 5, 5, 10, 10, 25]

		Como aplicar a estratégia gulosa no caso acima?
		Crie uma lista vazia para poder adicionar as moedas escolhidas.
		Passo 1: percorra a lista (carteira) enquanto o valor do troco não for alcançado ou superado:
			Adicione a moeda de 5; por enquanto a soma é 5, que é menor que 60. Continue!
			Adicione a moeda de 5; por enquanto a soma é 10, que é menor que 60. Continue!
			Adicione a moeda de 5; por enquanto a soma é 15, que é menor que 60. Continue!
			Adicione a moeda de 5; por enquanto a soma é 20, que é menor que 60. Continue!
			Adicione a moeda de 10; por enquanto a soma é 30, que é menor que 60. Continue!
			Adicione a moeda de 10; por enquanto a soma é 40, que é menor que 60. Continue!
			Adicione a moeda de 10; por enquanto a soma é 50, que é menor que 60. Continue!
			Adicione a moeda de 25; agora a soma é 75. PARE!
		Perceba que escolhemos as seguintes moedas para o troco: [5, 5, 5, 5, 10, 10, 10, 25]
		Mas temos um problema: a soma desses valores é 75.

		Passo 2: agora vamos remover as maiores moedas possíveis, mas que após a remoção a soma ainda
		continue maior ou igual ao valor do troco, isto é, a soma deve continuar maior ou igual a 60.
			Podemos remover a moeda de 25? Não, pois se ela for removida a soma será 50, que é menor que 60.
			Podemos remover a moeda de 10? Sim, se ela for removida a soma será 65, que é maior que 60.
			Podemos remover a moeda de 10? Não, pois se ela for removida a soma será 55, que é menor que 60.
			Podemos remover a moeda de 10? Não, pois se ela for removida a soma será 55, que é menor que 60.
			Podemos remover a moeda de 5? Sim, pois se ela for removida a soma será 60, que é maior ou igual a 60.
			Podemos remover a moeda de 5? Não, pois se ela for removida a soma será 55, que é menor que 60.
			Podemos remover a moeda de 5? Não, pois se ela for removida a soma será 55, que é menor que 60.
			Podemos remover a moeda de 5? Não, pois se ela for removida a soma será 55, que é menor que 60.
		Note que no passo 2 tivemos que percorrer a lista de moedas escolhidas de trás para frente.
		Tivemos que remover duas moedas, nessa ordem: 10, 5.
		Assim, sobraram as moedas de: [5, 5, 5, 10, 10, 25], que será o resultado da função.
	"""
	pass


