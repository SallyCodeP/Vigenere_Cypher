from string import ascii_lowercase
from random import randint, choice, triangular


alfabeto = list(ascii_lowercase)


# Gera chave pseudo aleatoria para criptografia
def __gerar_chave(num=int()):
    tamanho = randint(num, num + 100)
    chave = [choice(alfabeto) for _ in range(0, tamanho)]
    return "".join(chave)


# Criptografa a frase em questão gerando o alfabeto de vigenere
def __transformador(palavra, indexkey):
    cripto = list()
    indexx = 0
    for numero, local in enumerate(palavra):
        if type(local) != int:
            cripto.append(local)
        else:
            gerador = alfabeto[local:]
            total = 26 - len(gerador)
            for num in range(0, total):
                gerador.append(alfabeto[num])
            cripto.append(gerador[indexkey[indexx]])
            indexx += 1
    chave = [f"{str(a)}-" for a in indexkey]
    return "".join(cripto), "".join(chave)


# Criptografa usando uma chave pseudo aleatoria a frase colocada no parametro.
# Retorna a frase criptografada com a chave em questão
def criptografar(word=str(), la_chave="None"):
    if la_chave != "None":
        
        # Calibrando tamanho da chave para tamanho da frase
        if len(la_chave) == len(word) or len(la_chave) > len(word):
            key = la_chave
        
        # Chave menor que a palavra a ser criptografada
        elif len(la_chave) < len(word):
            key = [a for a in la_chave]
            contagem = 0
            compensa = len(word) - len(la_chave)
            for _ in range(0, compensa):
                key.append(la_chave[contagem])
                contagem += 1
                if contagem == len(la_chave):
                    contagem = 0
            key = ''.join(key)
        
    else:
        key = __gerar_chave(len(word))
    
    cripto_array = list()
    key_array = list()
    for letter in range(0, len(word)):
        if not word[letter] in alfabeto:
            cripto_array.append(str(word[letter]))
        else:
            cripto_array.append(alfabeto.index(word[letter]))
            key_array.append(alfabeto.index(key[letter]))
    return __transformador(cripto_array, key_array)





# Descriptografa a cifra de vigenere e retorna a frase descriptografada
def descripto(word=str(), passw=str()):
    final = list()
    tamanho = 0
    password = passw.split("-")
    password.pop()
    for letra in word:
        if not letra in alfabeto:
            final.append(letra)
        else:
            equivale = alfabeto.index(letra) - int(password[tamanho])
            if equivale < 0:
                equivale = 26 + equivale
                final.append(alfabeto[equivale])
            else:
                final.append(alfabeto[equivale])
            tamanho += 1
    return "".join(final)
