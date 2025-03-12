frase = input('Informe um texto para saber qual é a letra que mais aparece: \n')

i = 0
apareceu_mais_vezes = 0
letra_mais_apareceu = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    contador_letra = frase.count(letra_atual)

    if apareceu_mais_vezes < contador_letra:
        apareceu_mais_vezes = contador_letra
        letra_mais_apareceu = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_mais_apareceu}" que apareceu '
    f'{apareceu_mais_vezes} vezes'
)