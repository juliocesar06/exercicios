'''
CRIANDO  JOGO DA VELHA 

-CRIAR O GRAFICO
-CRIAR 0S ICONES
-CRIAR A TELA DE VITORIA

-JOGADOR

-BOT INTELIGENCIA SIMPLES
-BOT INTELIGENCIA AVANÇADA



'''
import random
from colorama import init
from colorama.ansi import Fore

init()


class JogoDaVelha:
    # lista dos espaços para jogar
    lista = [
                 ' ',' ',' ',
                 ' ',' ',' ',
                 ' ',' ',' '
            ]
    # lista da teclas para jogar
    lista_poss = [1,2,3,4,5,6,7,8,9]

    # lista com as posiçoes jogadas
    lista_off = []

    def __init__(self,jogador,dificuldade):
        self.jogador = jogador
        self.dificuldade = 0
        pass


    #-CRIAR O GRAFICO   
    def draw_table(self):
        # denhar a tela padrao com as teclas de jogo
        '''
            __|__|__ desenho padrao da tela
            __|__|__
              |  |
              1| 2| 3 gabarito das teclas
              4| 5| 6
              7| 8| 9
        '''
        
        print(f' {self.lista[0]}| {self.lista[1]}| {self.lista[2]}          {self.lista_poss[0]}|{self.lista_poss[1]}|{self.lista_poss[2]}')
        print(f' {self.lista[3]}| {self.lista[4]}| {self.lista[5]}          {self.lista_poss[3]}|{self.lista_poss[4]}|{self.lista_poss[5]}')
        print(f' {self.lista[6]}| {self.lista[7]}| {self.lista[8]}          {self.lista_poss[6]}|{self.lista_poss[7]}|{self.lista_poss[8]}')

        # -jogador
    
    # JOGANDO COM JOGADOR
    def player(self):

        # pede pra player jogar
        print('Jogue com as teclas....')
        jogar = int(input('1 a 9'))

        # criar uma condiçao para se escolher um numero menor ou maior q nove escolha denovo
        # criar uma condiçao onde se escolher um numero que ja esta marcado escolha de novo

        if jogar > 9 or jogar < 1:
            print('numero escolhido fora do possível...')
            pos_pos = []
            c=1
            for i in self.lista:
                
                if  i == ' ':
                    pos_pos.append[c]

                c += 1 
            
            # pergubta um numero ate que ele seja valido e nao esteja na pos_pos(POsição já jogada)
            while jogar > 9 or jogar <1 and jogar != int and jogar != pos_pos:
                # pede pra player jogar
                print('Jogue com as teclas....')
                jogar = int(input('1 a 9'))
                
        # confirir se o numero jogado esta disponivel
        lugares_vagos =[]
        marcado = []
        c = 1
        # mostra os lugares disponíveis para jogar
        for i in self.lista:
            if i == ' ':
                lugares_vagos.append(c)
            else:
                marcado.append(c)

            c+=1
        if len(marcado) > 8:
            JogoDaVelha.velha()
        print(f'os lugares que pode jogar ainda é: {lugares_vagos}')
 
        # marcando
        if self.lista[jogar-1] == ' ':
            self.lista[jogar-1] = 'X'


        
    # -BOT INTELIGENCIA SIMPLES
    def bot_low(self):

        
        bot ='O'
        pos = []
        marcado = []
        c=1   
        for i in self.lista:
            
                
            # Olha os espaços em branco na tabela
            if  i == ' ':
                pos.append(c)
            else:
                marcado.append(c)
            c+=1
            if len(marcado) > 8:
                JogoDaVelha.velha()
            # olhar onde esta vazio para jogar e nao perder
        # olhando primeira fileira horizontal
        if self.lista[0] and self.lista[1] == 'X':
            if self.lista[2] == ' ':
                self.lista[2] = 'O'
            else:
                self.bot_jogando(self,pos,bot)
        elif self.lista[0] and self.lista[2] == 'X':
            if self.lista[1] == ' ':
                self.lista[1] = 'O'
            else:
                self.bot_jogando(self,pos,bot)
        elif self.lista[1] and self.lista[2] == 'X':
            if self.lista[0] == ' ':
                self.lista[0] = 'O'
            else:
                self.bot_jogando(self,pos,bot)
      # olhando segunda fileira horizontal
        elif self.lista[3] and self.lista[4] == 'X':
            if self.lista[2] == ' ':
                self.lista[2] = 'O'
            else:
                self.bot_jogando(self,pos,bot)
        elif self.lista[3] and self.lista[5] == 'X':
            if self.lista[4] == ' ':
                self.lista[4] = 'O'
            else:
                self.bot_jogando(self,pos,bot)
        elif self.lista[4] and self.lista[5] == 'X':
            if self.lista[3] == ' ':
                self.lista[3] = 'O'
            else:
                self.bot_jogando(self,pos,bot)
            
    # olhando terceira  fileira orizontalmente
        elif self.lista[6] and self.lista[8] == 'X':
            if self.lista[7] == ' ':
                self.lista[7] = 'O'
            else:
                self.bot_jogando(self,pos,bot)
        elif self.lista[6] and self.lista[7] == 'X':
            if self.lista[8] == ' ':
                self.lista[8] = 'O'
            else:
                self.bot_jogando(self,pos,bot)
        elif self.lista[7] and self.lista[8] == 'X':
            if self.lista[7] == ' ':
                self.lista[7] = 'O'
            else:
                self.bot_jogando(self,pos,bot)
            
        # olhando trasversalmente
        elif self.lista[7] and self.lista[5] == 'X':
            self.lista[3] = 'O'
        elif self.lista[3] and self.lista[7] == 'X':
            self.lista[5] = 'O'
            
            # jogar esse se nao entrar na lista
        else:
           self.bot_jogando(self,pos,bot)
    
    # FUNÇÃO DE TESTAR ONDE JOGAR
    def bot_jogando(self,pos,bot):
        # olho os espaços vazios
        local = random.choice(pos)
        # testando se ja esta marcado o lugar
            
        if self.lista[local-1] == 'X' or self.lista[local-1] == 'O':
            local = random.choice(pos)
            print(local)
        else:
            self.lista[local-1] = bot
    
    #FUNÇÂO DE VITORIA
    def winner(self):


        # vencer horizontal fieira 1
        if self.lista[0]  == 'X' and self.lista[1] == 'X' and self.lista[2] == 'X':
            print('Voçe venceu.....')
            print('Fim...')
            jog= False
            return jog
        elif self.lista[0]  == 'O' and self.lista[1] == 'O' and self.lista[2] == 'O':
            print('BOT venceu.....')
            print('Fim...')
            jog = False
            return jog
        
        # vencer horizontal fieira 2
        if self.lista[3]  == 'X' and self.lista[4] == 'X' and self.lista[5] == 'X':
            print('Voçe venceu.....')
            print('Fim...')
            jog = False
            return jog
        elif self.lista[3]  == 'O' and self.lista[4] == 'O' and self.lista[5] == 'O':
            print('BOT venceu.....')
            print('Fim...')
            jog = False
            return jog
        
        # vencer horizontal fieira 3
        if self.lista[6]  == 'X' and self.lista[7] == 'X' and self.lista[8] == 'X':
            print('Voçe venceu.....')
            print('Fim...')
            jog = False
            return jog
        elif self.lista[6]  == 'O' and self.lista[7] == 'O' and self.lista[8] == 'O':
            print('BOT venceu.....')
            print('Fim...')
            jog = False
            return jog
            return jog
        
        # vencer verticalmente fieira 1
        if self.lista[0]  == 'X' and self.lista[3] == 'X' and self.lista[6] == 'X':
            print('Voçe venceu.....')
            print('Fim...')
            jog = False
        elif self.lista[0]  == 'O' and self.lista[3] == 'O' and self.lista[6] == 'O':
            print('BOT venceu.....')
            print('Fim...')
            jog = False
            return jog
            return jog

        # vencer verticalmente fieira 2
        if self.lista[1]  == 'X' and self.lista[4] == 'X' and self.lista[7] == 'X':
            print('Voçe venceu.....')
            print('Fim...')
            jog = False
            return jog
            return jog
        elif self.lista[1]  == 'O' and self.lista[4] == 'O' and self.lista[7] == 'O':
            print('BOT venceu.....')
            print('Fim...')
            jog = False
            return jog

        # vencer verticalmente fieira 1
        if self.lista[2]  == 'X' and self.lista[5] == 'X' and self.lista[8] == 'X':
            print('Voçe venceu.....')
            print('Fim...')
            jog = False
            return jog
        elif self.lista[2]  == 'O' and self.lista[5] == 'O' and self.lista[8] == 'O':
            print('BOT venceu.....')
            print('Fim...')
            jog = False
            return jog
        else:
            jog = True
            return jog
    
    # roda essa funçao quando der velha
    def velha():
        print('====================================')
        print('===============FIM==================')
        print('Deu Velha niguem GANHOU')





        


        
j1 = JogoDaVelha
jog = True
while jog:

    j1.draw_table(j1)
    j1.player(j1)
    j1.bot_low(j1)
    jog = j1.winner(j1)
    if jog == False:
        j1.draw_table(j1)
        break

    print(Fore.YELLOW + '===========================================================================')
