def anagrama(palavra:str) -> int:
    from math import factorial
    palavra_separada = list(palavra)
    contagem = len(palavra)
    num = 0
    letras_separadas = 0

    #criei 2 listas, uma para armazenagem das letras que se repetem, e a outra para a armazenagem da quantidade delas
    letra_repetida = []
    lista_repeticao = []

    #aqui basicamente fiz um sistema para que caso a letra já tenha sido inserida na lista, ela não ser contabilizada novamente
    for letra in range(contagem):
        if palavra_separada[letras_separadas] in lista_repeticao:
            num = num + 1
        else:
            repeticao = palavra.count(palavra[num])
            num = num + 1
            if repeticao >= 2:
                letra_repetida.append(repeticao)
                lista_repeticao.append(palavra_separada[letras_separadas])
            letras_separadas = letras_separadas + 1
    num_ = 0
    calculo = 1

    #neste bloco é feito o cálculo das letras repetidas da palavra, sendo executado de forma individual,
    #transformando assim a quantidade de letras repetidas em numeros fatoriais
    for intens in lista_repeticao:
        divisisores = factorial(letra_repetida[num_])
        calculo = calculo * divisisores
        num_ = num_ + 1

    #por fim é efetuada a fórmula padrão da quantidade de anagramas existentes numa palavra
    resultado = factorial(contagem) / calculo
    return int(resultado)