primeiro = 0
segundo = 1

seq = int(input("Digite quantas sequências deseja ver: "))

print(primeiro)
print(segundo)
for i in range(0,(seq-2)):
    soma = primeiro + segundo
    print(soma)
    primeiro = segundo
    segundo = soma

# testando 123