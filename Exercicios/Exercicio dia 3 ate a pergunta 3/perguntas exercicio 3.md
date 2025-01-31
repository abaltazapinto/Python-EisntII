Sobre manipulação de entradas e erros:

Quais são as melhores práticas para tratar entradas de usuários em programas interativos? Por exemplo, como lidar com separadores diferentes (vírgulas, espaços, etc.)?

Como o Python trata entradas inválidas durante a conversão de tipos (como float) e quais outras estratégias poderiam ser usadas além do try/except?

Existe alguma forma de validar entradas automaticamente antes de processá-las? Ferramentas ou bibliotecas ajudam nesse caso?

Sobre operações matemáticas e funções:

Quando usar a função reduce em vez de um loop simples para processar uma lista de números?

Qual seria a melhor forma de lidar com operações matemáticas personalizadas (por exemplo, potências, raízes) se quisermos expandir o programa?

Em linguagens como Java ou C, como poderíamos implementar um programa semelhante ao que foi feito em Python?

Sobre tratamento de divisão por zero:

Qual é a maneira mais robusta de lidar com a divisão por zero? Retornar infinito é sempre apropriado, ou seria melhor gerar um erro personalizado?

Existe alguma abordagem matemática que permita lidar com divisões por zero em cenários específicos, como estatísticas ou álgebra linear?

Sobre extensibilidade do programa:

Como podemos permitir que o programa aceite mais operadores, como potenciação (^) ou módulo (%)?
Existe uma maneira de permitir que o usuário insira fórmulas complexas (por exemplo, 1+2*3) e o programa as resolva dinamicamente?

Como adaptar o programa para aceitar entradas em diferentes formatos, como números separados por espaços ou ponto e vírgula?

Sobre desempenho e otimização:

Qual é a diferença de desempenho entre o uso de reduce e loops convencionais em listas muito grandes?

Como o Python lida internamente com a divisão por zero ao usar float('inf')? Isso tem algum impacto em cálculos de larga escala?

Sobre boas práticas de programação:

Quais são os melhores métodos para garantir que o programa seja escalável e fácil de manter?
Como documentar o código de forma clara para que outro programador entenda rapidamente as intenções do programa?

É melhor organizar funções como soma, subtração etc. separadamente em vez de usar lambdas no dicionário? Por quê?

Sobre segurança e entradas do usuário:

Quais problemas de segurança podem surgir se não tratarmos adequadamente a entrada do usuário? (Por exemplo, injeção de código em linguagens como JavaScript).

O que poderia ser feito para evitar que entradas muito grandes (ou malformadas) causem travamentos no programa?

Para a Pergunta 1:
Sobre dicionários e correspondências:

Como lidar com entradas duplicadas de forma eficiente em dicionários? Por exemplo, se houver cores ou marcas repetidas, como apresentar todas as correspondências corretamente?
É possível criar dicionários que aceitem múltiplas chaves para o mesmo valor? Como seria a estrutura ideal nesse caso?

Sobre estrutura de dados:

Quando usar dicionários em vez de listas ou conjuntos para armazenar pares de valores? Quais são as vantagens e desvantagens?
Existem alternativas aos dicionários que facilitam a busca e manipulação de dados pareados, como cores e marcas?
Sobre lógica e validação:

Como validar automaticamente que o número de marcas e cores inseridas pelo usuário é igual? Há métodos mais robustos além de contar manualmente?
Para a Pergunta 2:
Sobre variáveis globais e locais:

Quando o uso de variáveis globais é justificado? Quais são os principais problemas que podem surgir ao usá-las em programas maiores?
Como evitar conflitos entre variáveis globais e locais, especialmente em projetos mais complexos?
Sobre argumentos arbitrários por palavra-chave:

Qual é a diferença prática entre *args e **kwargs? Em que cenários cada um deles é mais adequado?
Existem limitações no uso de argumentos arbitrários por palavra-chave em programas que precisam de grande desempenho?
Sobre organização do código:

Em um programa real, é melhor usar funções que retornem dicionários ou trabalhar diretamente com variáveis globais? Por quê?
Como podemos documentar melhor funções que usam **kwargs para torná-las mais compreensíveis?
Para a Pergunta 3:
Sobre funções lambda:

Quais são as principais limitações do uso de funções lambda em Python? Há algo que elas não possam fazer em comparação com funções regulares?
Por que as funções lambda são preferidas para cálculos rápidos em programas menores? Existem desvantagens em usá-las em projetos maiores?
Sobre operações matemáticas:

Como seria possível adaptar o programa para aceitar fórmulas completas (ex.: 1+2*3) ao invés de operadores fixos? É necessário usar bibliotecas externas, como eval?
Qual é a melhor forma de lidar com exceções matemáticas além da divisão por zero? Por exemplo, operações inválidas como 0 ** -1.
Sobre extensibilidade:

Como permitir que o programa execute operações mais complexas, como módulo (%) ou potenciação (^), mantendo a simplicidade?
É possível criar uma interface gráfica simples para este programa, usando bibliotecas como Tkinter ou PyQt?
