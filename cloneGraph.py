"""
# Definiția pentru un nod.
class Node:
    def __init__(self, val = 0, neighbors = None):
        # Fiecare nod are o valoare (val) și o listă de vecini (neighbors).
        self.val = val
        # Dacă nu există vecini, inițializăm cu o listă goală.
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Dicționarul oldToNew va mapa nodurile originale la copii lor.
        oldToNew = {}

        # Definim funcția DFS care va clona nodul și vecinii săi.
        def dfs(node):
            # Dacă nodul a fost deja clonat, îl returnăm direct din dicționar.
            if node in oldToNew:
                return oldToNew[node]
            
            # Creăm o copie a nodului curent, dar fără vecini pentru moment.
            copy = Node(node.val)
            # Mapa nodul original la copia sa.
            oldToNew[node] = copy
            
            # Parcurgem vecinii nodului și îi clonăm recursiv.
            for nei in node.neighbors:
                # Adăugăm vecinii clonați la lista de vecini a copiei.
                copy.neighbors.append(dfs(nei))
            
            # Returnăm copia nodului curent.
            return copy

        # Dacă graful este gol (nodul de start este None), returnăm None.
        return dfs(node) if node else None
