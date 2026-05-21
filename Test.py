import unittest
from Bicicletta import Bicicletta, BiciclettaClassica, BiciclettaElettrica
from FlottaBici import FlottaBici
from Utility import calcola_durata_minuti, classifica_corsa, riepilogo_corse

# Realizza una piccola dimostrazione di polimorfismo:

# def stampa_flotta(biciclette: list) -> None:
#     ...

#     Crea una lista con oggetti di almeno 2 classi diverse del dominio
#     Applica la stessa operazione a tutti gli elementi senza fare controlli espliciti sul tipo
#     Inserisci un commento breve (2-3 righe) in cui spieghi l'idea di interfaccia comune e dispatch dinamico
#     Mostra anche una chiamata di esempio della funzione

b1 = Bicicletta("A1", "classica", "Duomo", 10, True)
b2 = BiciclettaClassica("A2", "classica", "Centrale", 20, True, "M")
b3 = BiciclettaElettrica("A3", "elettrica", "Porta Nuova", 15, True, 80)

flotta = [b1, b2, b3]

def stampa_flotta(biciclette: list):
    for bici in biciclette:
        print(bici)

stampa_flotta(flotta)