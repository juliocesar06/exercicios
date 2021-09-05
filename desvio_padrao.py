'''
Trabalho da faculdade de analíse e desenvolvimento de sistemas

- criar um programa que faz media,moda e mediana, variância e desvio_padrao


processos

--> criar uma classe estatisticas 

--> metodos de media

--> metodos de moda

--> metodos de mediana

--> metodos de variância

--> metodos de desvio_padrao
'''
import math



class Estatística:

    def __init__(self,grupo) :
        self.grupo = grupo

    def media(self):
        '''
         No metódo meédia:
         soma todos o svalores da lista grupo
         divide pela sua quantidade total
        '''
        soma = sum(self.grupo)
        media =  soma / len(self.grupo)
        return media

    def moda(self):
        # organizando a minha lista
        grupo = sorted(self.grupo)
        c = 0
        loop = True
        moda = []

        # loop ate terminar a lista
        while loop:
            # testar iten na lista grupo
            for i in grupo:
                # recebe qtd de vezes item (i) na lista
                v = grupo.count(i)
                # condicional q testa se o item é maior q seu antecessor
                if v >= c:
                    if i in moda:
                        pass
                    else:    
                        moda.append(i)
                    if v > grupo.count(moda[0]):
                        moda.clear()
                        moda.append(i)
                    elif v < grupo.count(moda[0]):
                        moda.remove(i)
                    elif v == grupo.count(moda[0]):
                        pass
                c =grupo.count(i)
            if len(moda) > 0:
                for valor in moda:
                    if grupo.count(valor) == 1:
                        moda.clear()
            if len(moda) == 0:
                moda.append('AMODAL')
                loop = False
            
            loop = False
       
        return moda


    def mediana(self):
        grupo = sorted(self.grupo)
        
        if len(grupo) % 2 == 0:
            x = int(len(grupo)/2)
            mediana = (grupo[x-1] + grupo[x])/2
        else:
            x = int(len(grupo)/2)
            mediana =  grupo[x]

        return mediana
    def variancia(self):
        '''
        s =  s2 = (i=1 , n)sigma (x1+m)² * f/n-1
        s = varaincia
        sigma = somatorio
        x1 = primeiro item
        m = media
        f = quantidade de vezes que aparece o item
        n = numero totol de termos

        '''
        media = Estatística.media(self)
        sigma = []
        for i in self.grupo:
            x1 = i
            f = self.grupo.count(x1)
            termo = ((x1 - media) ** 2)
            sigma.append(termo)
        variancia = sum(sigma) / (len(self.grupo)-1)
        return variancia


    def desvio_padrao(self):
        x =  Estatística.variancia(self)
        desvio_padrao = float(math.pow(x,1/2))
        math.ceil(desvio_padrao)
        return desvio_padrao
    

print('Digite sua lista usando uma virgula(,) para separar')
lista = input('Digite a lista: ')
lista = lista.split(',')
lista_num = []
for i in lista:
    if type(i) == str:
        try:
            i = int(i)
            lista_num.append(i)

        except:
            lista.remove(i)


grupo1 = Estatística(lista_num)
print(f'Analisando a lista {lista_num}')
print(f' A média é :{grupo1.media():.2f}')
print(f' A moda é : {grupo1.moda()}')
print(f' A mediana é : {grupo1.mediana()}')
print(f' A variância é : {grupo1.variancia():.2f}')
print(f' O desvio padrão é : {grupo1.desvio_padrao():.3f}')
