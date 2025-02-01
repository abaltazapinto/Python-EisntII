


# class Pessoa:
#     PrimeiroNome = 'Andre'
#     UltimoNome = 'Baltazar'
#     idade = 32
#     profissao = 'Engenheiro de software'

# PrimeiroNome = Pessoa()
# UltimoNome = Pessoa()
# idade = Pessoa()
# profissao = Pessoa()


class Pessoa:
    def __init__(self, primeiroNome:str, ultimoNome:str, idade:int, profissao: str):
        self.primeiroNomeInit = primeiroNome
        self.ultimoNomeInit = ultimoNome
        self.idadeInit = idade
        self.profissaoInit = profissao
        
    def obterDadosPessoa(self):
        return self.primeiroNomeInit, self.ultimoNomeInit, self.idadeInit, self.profissaoInit
    
    


pessoas = []

for i in range(int(input('Introduza o numero de pessoas que pretende inserir'))):
    pessoas.append(Pessoa(input(f'{i + 1}ª Pessoa: Introduza o seu primeiro Nome:'),
                         str(input(f'{i + 1}ª Pessoa: Introduza o seu ultimo Nome:')),
                         int(input(f'{i +1}ª Pessoa: Introduza a sua idade:')),
                         str(input(f'{i+1}º Pessoa: Introduza a sua profissão:'))
                         
                         ))
    

print('Dados pessoais das pessoas')
for i in pessoas:
    print(i.obterDadosPessoa())