import heapq
import numpy

class FilaDePrioridade:

	def __init__(self):
		self._fila = []
		self._indice = 0

	def inserir(self, item, prioridade):
		heapq.heappush(self._fila, (-prioridade, self._indice, item))
		self._indice += 1

	def listar(self):
		for i in range(1, 10):
			print(heapq.heappop(self._fila)[-1])

		return heapq.heappop(self._fila)[-1]

class Tarefa:
	def __init__(self, nome):
		self.nome = nome

	def __repr__(self):
		return self.nome

fila = FilaDePrioridade()
fila.inserir(Tarefa('Comparecer reuniao'), 0)
fila.inserir(Tarefa('Ligação para familia'), 5)
fila.inserir(Tarefa('Organziar agenda'), 1)
fila.inserir(Tarefa('Reuniao com cliente'), 5)
fila.inserir(Tarefa('Consulta médica'), 3)
fila.inserir(Tarefa('Passear com cachorro'), 2)
fila.inserir(Tarefa('Fazer compras'), 1)
fila.inserir(Tarefa('Fazer atividade fisica'), 5)
fila.inserir(Tarefa('Comprar comida'), 2)
fila.inserir(Tarefa('Agendar reunião com a equipe'), 5)

print(fila.listar())