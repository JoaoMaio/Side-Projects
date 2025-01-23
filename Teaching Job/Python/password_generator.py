import random
import string 

# guardar todos os caracteres que são usados para as passwords
letras_minusculas = list(string.ascii_lowercase)
letras_maiusculas = list(string.ascii_uppercase) 
digitos = list(string.digits)
sinais = list(string.punctuation)

tamanho = input("Quantos caracteres quer que a sua password tenha? ")

# vai estar sempre a executar até sairmos
while True:
    try:
        tamanho_numero = int(tamanho)

        # verificar se o numero é menor que 8
        if tamanho_numero < 8:
            print("Insira um numero maior que 8!!")
            tamanho = input("Quantos caracteres quer que a sua password tenha? ")
        else:
            break
    except:
        print("O número que inseriu não é válido")
        tamanho = input("Quantos caracteres quer que a sua password tenha? ")
    

# misturar todas as listas de caracteres
# evita que a password tenha qualquer padrão quando estes caracteres forem usados
random.shuffle(letras_minusculas)
random.shuffle(letras_maiusculas)
random.shuffle(digitos)
random.shuffle(sinais)


# vamos dividr a password em 2 partes
# a primeira parte vai ser composta por letras_minusculas e letras_maiusculas (60% da password)
# a segunda parte vai ser composta por numeros e sinais (40%)
part1 = round(tamanho_numero * 0.3)
part2 = round(tamanho_numero * 0.2)

# nossa password
result = []

for x in range(part1):
    result.append(letras_minusculas[x]) # 30% da password
    result.append(letras_maiusculas[x]) # outros 30% da password

for x in range(part2):
    result.append(digitos[x]) # 20% da password
    result.append(sinais[x])  # os outros 20% da password

# voltar a misturar a nossa password para termos a certeza que não tem nenhum padrão
random.shuffle(result)

# vamos transformar a lista de caracteres numa string
password = "".join(result)

print("A sua password gerada por nós foi: ", password)