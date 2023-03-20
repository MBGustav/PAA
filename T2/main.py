from graph_lib import graph
import os
cwd = os.getcwd()
print(cwd)

Epsilon = 0.0000005 

def compare_float(float_1, float_2):
	global Epsilon
	#testing for equal numbers
	if (abs(float_1) - abs(float_2) <= Epsilon):
		return True
	if float_1 < float_2:
		return True


def Gen_graphs_input(G_game, G_impo):
# Preenche 2 grafos - Comum + Impostor
## Input inicial:
	# 0 - tamanho do Grafo
	# 1 - Total de Corredores
	# 2 - Total de "Chamines"
	# 3 - Total de consultas
	sizeG, Corr, Vent, Const  = input().split(' ')

	sizeG, Corr, Vent, total_task = [int(x) for x in next(f).split()]
	for i in range(sizeG+1): #cria grafos
		G1.add_vertice(str(i))
		G2.add_vertice(str(i))
	
	data = input().split() # entrada Grafo principal
	# data = line.split()

	for i in range(len(data)//3):
		v1, v2, w = data[3*i+0], data[3*i+1], data[3*i+2]
		v1, v2, w = str(v1), str(v2), float(w)
		# print(v1, v2, w)
		G1.add_edge(v1,v2, w)
		G2.add_edge(v1,v2, w)

	data = input().split() # entrada Grafo Impostor
	# data = line.split()
	for k in range(len(data)//2):
		v1, v2 = data[2*k+0], data[2*k+1]
		v1, v2 = str(v1), str(v2)
		G2.add_edge(v1,v2) # peso == 1 (default) 

	for task in range(total_task):
		out = open("output.txt","a")
		pos = next(f).split()[0]
		player = G1.shortest_path(pos,'0')
		impostor = G2.shortest_path(pos,'0')
		if player <= impostor:
			print(task+1,"victory")
		else:
			print(task+1,"defeat")

def Gen_graphs_file():

	G1 = graph()
	G2 = graph()
	f = open("input.txt", "r")
	sizeG, Corr, Vent, total_task = [int(x) for x in next(f).split()]
	# print(sizeG, Corr, Vent, total_task)
	for i in range(sizeG+1): #cria grafos
		G1.add_vertice(str(i))
		G2.add_vertice(str(i))

	
	line = f.readline() # entrada Grafo principal
	data = line.split(" ")

	for i in range(len(data)//3):
		v1, v2, w = data[3*i+0], data[3*i+1], data[3*i+2]
		v1, v2, w = str(v1), str(v2), float(w)
		# print(v1, v2, w)
		G1.add_edge(v1,v2,w)
		G2.add_edge(v1,v2,w)

	# G2.print_graph()

	line = f.readline() # entrada Grafo Impostor
	data = line.split()
	for k in range(len(data)//2):
		v1, v2 = data[2*k+0], data[2*k+1]
		v1, v2 = str(v1), str(v2)
		G2.add_edge(v1,v2) # peso == 1 (default) 

	for task in range(total_task):
		out = open("output.txt","a")
		pos = next(f).split()[0]
		player = G1.shortest_path(pos,'0')
		impostor = G2.shortest_path(pos,'0')
		print("Pontuacao:", player, impostor)
		if compare_float(player,impostor):
			# out.write("victory\n")
			print(task+1,"victory")
		else:
			# out.write("defeat\n")
			print(task+1,"defeat")
	out.close()

Gen_graphs_file()


# print(type(sizeG), type(Corr), type(Vent), type(Const))
# print(v1,v2,w)


# g.add_vertice("A")
# g.add_vertice("B")
# g.add_vertice("C")
# g.add_vertice("D")
# g.add_vertice("D")

# g.add_edge("A", "B", 0)
# g.add_edge("B", "A", 5.8)
# g.add_edge("B", "C", 3)
# g.add_edge("C", "D", 4)
# g.add_edge("D", "A", 5)
# # print(g.V)
# g.print_graph()
# # # print(g.get_vertices())

# print(g.shortest_path("A", "B"))


