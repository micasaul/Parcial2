# 1. Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada
# de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir
# tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:





from Arbol import BinaryTree

pokemons = [
    {
        "nombre": "Bulbasaur",
        "tipo": "Planta/Veneno",
        "numero_de_pokemon": 1,
        "nivel": 5
    },
    {
        "nombre": "Charmander",
        "tipo": "Fuego",
        "numero_de_pokemon": 4,
        "nivel": 5
    },
    {
        "nombre": "Squirtle",
        "tipo": "Agua",
        "numero_de_pokemon": 7,
        "nivel": 5
    },
    {
        "nombre": "Pikachu",
        "tipo": "Eléctrico",
        "numero_de_pokemon": 25,
        "nivel": 7
    },
    {
        "nombre": "Jigglypuff",
        "tipo": "Normal/Hada",
        "numero_de_pokemon": 39,
        "nivel": 3
    },
    {
        "nombre": "Meowth",
        "tipo": "Normal",
        "numero_de_pokemon": 52,
        "nivel": 4
    },
    {
        "nombre": "Psyduck",
        "tipo": "Agua",
        "numero_de_pokemon": 54,
        "nivel": 6
    },
    {
        "nombre": "Machop",
        "tipo": "Lucha",
        "numero_de_pokemon": 66,
        "nivel": 5
    },
    {
        "nombre": "Geodude",
        "tipo": "Roca/Tierra",
        "numero_de_pokemon": 74,
        "nivel": 4
    },
    {
        "nombre": "Gastly",
        "tipo": "Fantasma/Veneno",
        "numero_de_pokemon": 92,
        "nivel": 6
    },
    {
        "nombre": "Eevee",
        "tipo": "Normal",
        "numero_de_pokemon": 133,
        "nivel": 5
    },
    {
        "nombre": "Snorlax",
        "tipo": "Normal",
        "numero_de_pokemon": 143,
        "nivel": 8
    },
    {
        "nombre": "Jolteon",
        "tipo": "Eléctrico",
        "numero_de_pokemon": 135,
        "nivel": 10
    },
    {
        "nombre": "Lycanroc",
        "tipo": "Roca",
        "numero_de_pokemon": 744,
        "nivel": 15
    },
    {
        "nombre": "Tyrantrum",
        "tipo": "Roca",
        "numero_de_pokemon": 697,
        "nivel": 20
    }
]


nombre=BinaryTree()
numero=BinaryTree()
tipo=BinaryTree()

# a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
for pokemon in pokemons:
    nombre.insert_node(pokemon["nombre"], {"numero_de_pokemon": pokemon["numero_de_pokemon"], "tipo": pokemon["tipo"], "nivel": pokemon['nivel']})
    numero.insert_node(pokemon["numero_de_pokemon"], {"nombre": pokemon["nombre"], "tipo": pokemon["tipo"], "nivel": pokemon['nivel']})
    tipo.insert_node(pokemon["tipo"], {"nombre": pokemon["nombre"], "numero_de_pokemon": pokemon["numero_de_pokemon"], "nivel": pokemon['nivel']})

# b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
# último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
# mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos
# caracteres–;
num= int(input("Ingrese el numero de pokemon que desea buscar: "))
pos=numero.search(num)
print(pos.value, pos.other_value) if pos is not None else print("No se encontro pokemon con ese numero")
print("")

name= input("Ingrese el nombre que desea buscar: ")
print(nombre.search_coincidente(name))
print("")

# c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
agua= tipo.search_lista("Agua")
fuego = tipo.search_lista("Fuego")
planta = tipo.search_lista("Planta")
electrico = tipo.search_lista("Electrico")
print(f"Los pokemon de tipo agua son: {agua}")
print(f"Los pokemon de tipo fuego son: {fuego}")
print(f"Los pokemon de tipo planta son: {planta}")
print(f"Los pokemon de tipo electrico son: {electrico}")
print("")

# d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
# además un listado por nivel por nombre;
print("Listado en orden ascendente por numero: ")
numero.inorden_values()
print("")
nivel=nombre.inorden_nivel()
print(f"Listado en orden ascendente por nivel: {nivel}")
print("")

# e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
jolteon=nombre.search("Jolteon")
print(jolteon.value, jolteon.other_value) if jolteon is not None else print("No se encontro pokemon con ese numero")
lycanroc=nombre.search("Lycanroc")
print(lycanroc.value, lycanroc.other_value) if lycanroc is not None else print("No se encontro pokemon con ese numero")
tyrantrum=nombre.search("Tyrantrum")
print(tyrantrum.value, tyrantrum.other_value) if tyrantrum is not None else print("No se encontro pokemon con ese numero")
print("")

# f) Determina cuantos Pokémons hay de tipo eléctrico y acero. 
acero = tipo.search_lista("Acero")
print(f"Hay {len(acero)} pokemons de tipo acero y {len(electrico)} pokemons de tipo electrico")