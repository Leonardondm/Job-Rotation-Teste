# definindo a string a ser invertida
string = "exemplo de string"

# criando uma lista vazia para armazenar os caracteres invertidos
string_invertida = []

# percorrendo a string de trás para frente e adicionando cada caractere à lista
for i in range(len(string)-1, -1, -1):
    string_invertida.append(string[i])

# unindo os caracteres invertidos em uma nova string
nova_string = "".join(string_invertida)

# imprimindo a nova string invertida
print(nova_string)
