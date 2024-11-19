from enum import Enum

class AccessibilityType(Enum):
    NIL = "Sem acessibilidade"
    ELEVADOR = "Elevador"
    RAMPA = "Rampa"
    EM_NIVEL = "Em nível"
    ELEVACAO_INCLINADA = "Elevação inclinada"
    ESTEIRA = "Esteira rolante"
