from typing import List
from accessibilityEnum import AccessibilityType
from __future__ import annotations

class Node:

    def __init__(self, name):
        self.name: str = name
        self.connections: List[Node] = []
        self.accessibility: AccessibilityType = AccessibilityType.NIL


    def addConnection(self, node: Node) -> bool:
        # Limita o número de conexões a 2
        if len(self.connections) >= 2:
            return False
        
        # Verifica se o nó já está conectado
        if node in self.connections:
            return True  # Conexão já existe
        
        # Adiciona o nó na lista de conexões de self
        self.connections.append(node)
        
        # Tenta adicionar self na lista de conexões de node
        if len(node.connections) < 2 and self not in node.connections:
            node.connections.append(self)
        else:
            # Remove a conexão se não puder ser feita em ambas as direções
            self.connections.remove(node)
            return False
        
        return True

    def removeConnection(self, node: Node) -> bool:
        # Remove a conexão de self para node, se existir
        if node in self.connections:
            self.connections.remove(node)
            
            # Também remove a conexão de node para self, se existir
            if self in node.connections:
                node.connections.remove(self)
            
            return True  # Conexão removida com sucesso
        return False  # Conexão não existia
    
    