'''
JOGO BINGO

-CRIAR  CARTELA 0,100

-PLAYER ESCOLHE A CERTELA

-MOSTRA CARTELA ESCOLHIDA

-BOT SORTEIA UMA PEDRA

-SE TEM A PEDRA NA CARTELA  MARCA ELE

-GANHA SE MARCA A CARTELA HORIZONTAL E VERTICAL

'''
import random
import time
import colorama
from colorama.initialise import init


init()

class Bingo:
    tela = []
    pedra = list(range(1,100))
    jogar = True

    
    def __init__(self):
        pass
#==============================================================================
    #-CRIAR  CARTELA 1,99
    def gerar_cartela(self):
        
        while len(self.tela)< 25:
            num = random.randint(1,99)
            if num not in self.tela:
                if num <10:
                    num = str(f' {num}')
                else:
                    num = str(num)

                
                self.tela.append(num)
        self.tela[12] = ':)'

    
#   -MOSTRA CARTELA ESCOLHIDA
    def draw_tela(self):

        '''
        TELA =>
        ---------------
             BINGO
        ---------------
          |  |  |  |  |
        ---------------
          |  |  |  |  |
        ---------------
          |  |  |  |  |
        ---------------
          |  |  |  |  |
        ---------------
          |  |  |  |  |
        


        '''
      
        print('-'*10)
        print('  BINGO  ')
        print('-'*10)
        print(f'{self.tela[0]} |{self.tela[1]} |{self.tela[2]} |{self.tela[3]} |{self.tela[4]}')
        print(f'{self.tela[5]} |{self.tela[6]} |{self.tela[7]} |{self.tela[8]} |{self.tela[9]}')
        print(f'{self.tela[10]} |{self.tela[11]} |{self.tela[12]} |{self.tela[13]} |{self.tela[14]}')
        print(f'{self.tela[15]} |{self.tela[16]} |{self.tela[17]} |{self.tela[18]} |{self.tela[19]}')
        print(f'{self.tela[20]} |{self.tela[21]} |{self.tela[22]} |{self.tela[23]} |{self.tela[24]}')

    def bot_sortear(self):
        self.pedra_escolhida  = random.choice(self.pedra)
        self.pedra.remove(self.pedra_escolhida)
        self.pedra_escolhida = str(self.pedra_escolhida)

        print('-'*10)
        print(f'A pedra sorteada foi... %" {self.pedra_escolhida} "% ')
        print('-'*10)
            
    def marcar(self):
            if self.pedra_escolhida in self.tela:
                local = self.tela.index(self.pedra_escolhida)
                self.tela[local] = 'X '
    
    def testar_vitoria(self):
        '''
        ganha horizontalmete e verticalmente
        pos 01234 
        '''
        # HORIZONTAL
        # VENCER FILEIRA 1 HORIZONTAL
        if self.tela[0] == 'X ' and self.tela[1] == 'X ' and self.tela[2] == 'X ' and self.tela[3] == 'X ' and self.tela[4] == 'X ':
            self.winner(b1)
        # VENCER FILEIRA 2 HORIZONTAL
        elif self.tela[5] == 'X ' and self.tela[6] == 'X ' and self.tela[7] == 'X ' and self.tela[8] == 'X ' and self.tela[9] == 'X ':
            self.winner(b1)
        # VENCER FILEIRA 3 HORIZONTAL
        elif self.tela[10] == 'X ' and self.tela[11] == 'X ' and self.tela[13] == 'X ' and self.tela[14] == 'X ':
            self.winner(b1)
        # VENCER FILEIRA 4 HORIZONTAL
        elif self.tela[15] == 'X ' and self.tela[16] == 'X ' and self.tela[17] == 'X ' and self.tela[18] == 'X ' and self.tela[19] == 'X ':
            self.winner(b1)
        # VENCER FILEIRA 5 HORIZONTAL
        elif self.tela[20] == 'X ' and self.tela[21] == 'X ' and self.tela[22] == 'X ' and self.tela[23] == 'X ' and self.tela[24] == 'X ':
            self.winner(b1)
        else:
            self.testar_derrota(self)
    
    # VITÓRIA
    def winner(self):
        c = 0
        for i in self.tela:
            if i == 'X ':
                i = colorama.Back.LIGHTGREEN_EX +colorama.Fore.WHITE+ 'X '+ colorama.Back.RESET + colorama.Fore.RESET
                self.tela[c-1]=i
                c+=1
            else: 
                c+=1

        for i in range(3):
            print('01'*77)
        print('#'*154)
        print(colorama.Fore.GREEN + ' PARABÉNS         '*9 + colorama.Fore.RESET)
        self.jogar = False
        self.draw_tela(self)
        


    def testar_derrota(self):
        if len(self.pedra) < 1:
            print('==========================')
            print('Voçe não ganhou')
            for i in self.tela:
                if i == 'X ':
                    i = colorama.Back.LIGHTGREEN_EX +colorama.Fore.WHITE+ 'X '+ colorama.Back.RESET + colorama.Fore.RESET
                    self.tela[c-1]=i
                    c+=1
                else: 
                    c+=1
            self.jogar = False
        else:
            self.jogar = True
        


                


b1= Bingo

while b1.jogar:
    b1.gerar_cartela(b1)
    b1.draw_tela(b1)
    #time.sleep(1)
    b1.bot_sortear(b1)
    b1.marcar(b1)
    #time.sleep(3)
    b1.draw_tela(b1)
    b1.testar_vitoria(b1)

    
    
