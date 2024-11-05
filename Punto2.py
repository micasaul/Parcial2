# 2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los
# algoritmos necesarios para resolver las siguientes tareas:

from Grafo import Graph
from random import randint

star = Graph(dirigido=False)

# d) cargue al menos los siguientes personajes: luke Skywalker, Darth Vader, Yoda,
# Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8
personajes = ["Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C-3PO", "Leia", "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2-D2", "BB-8"]

# a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la
# cantidad de episodios en los que aparecieron juntos ambos personajes que se
# relacionan;
for personaje in personajes:
    star.insert_vertice(personaje)

for i in range (len(personajes)-1):
    for j in range (i+1, len(personajes)):
        star.insert_arista(personajes[i], personajes[j], randint(0, 9))

# b) hallar el árbol de expansión minino y determinar si contiene a Yoda;
for nodo in star.kruskal("Luke Skywalker")[0].split(';'):
    if "Yoda" in nodo:
        print("El arbol de expansion minimo contiene a Yoda")
        break
print("")

# c) determinar cuál es el número máximo de episodio que comparten dos personajes,
# y quienes son
aristas = star.lista_arista()
m = aristas[0]
for arista in aristas:
    if arista['peso'] > m['peso']:
        m= arista
print(f"Los personajes que tuvieron mayor cantidad de episodios juntos son {m['origen']} y {m['destino']} con {m['peso']} episodios") 