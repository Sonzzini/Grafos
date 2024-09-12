Para cada atividade a ser feita, criar um arquivo novo com o nome da atividade.
Cada código implementado para aquela atividade deve ser feito neste arquivo, e caso seja requisitado estar em outro, importá-lo neste outro arquivo.

Exemplo:
Atividade 1 - faça a função `Marina()` que retorna um `int` para a classe `Grafo`

```
ARQUIVO: Atividade 1

def Marina() -> int:
  print("Olá! Eu sou a Marina.")
  return 1

```

Incluir o prefixo "atv" na função a ser importada (para diferenciação da função própria da classe)

```
ARQUIVO: Grafo

from Atividade 1 import Marina as atvMarina

class Grafo:
  ...

  def Marina() -> int:
      return atvMarina()
```

