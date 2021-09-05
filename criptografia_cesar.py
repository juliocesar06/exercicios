
MAX_VALOR_CHAVE = 26

# funçao que procura saber se o usuário quer criptografar ou descriptografar a msg
def getMode():
    
    while True:
        
        print('Voçe quer criptografar ou descriptgrafar mensagem ?')
        mode = input().lower()
        if mode in 'criptografar c descriptografar d'.split():
            return mode
        else:
            print('Entre com: criptografar  ou c descriptografar ou d')

# recebe a mesnagem que irá criptografar ou descriptografar
def getMensagem():
    print('Entre com sua mensagem !!!')
    return input()

# gerando a chave 
def getKey():
    key = 0
    while True:
        print(f'Entre com sua chave (1-{MAX_VALOR_CHAVE})')
        key = int(input())
        if key >=1  and key <= MAX_VALOR_CHAVE:
            return key

def getTaduzirMsg(mode,mensagem, key):
    if mode[0] == 'd':
        key = -key
    translated =  ''

    # testa ca da um dos numeros para tabela asc2
    for symbol in mensagem:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
        
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif  num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num  < ord('a'):
                    num +=26
            translated +=chr(num)
        else:
            translated += symbol
    return translated

mode = getMode()
mensagem = getMensagem()
key = getKey()

print(' Digite seu texto')
print(getTaduzirMsg(mode,mensagem,key))


