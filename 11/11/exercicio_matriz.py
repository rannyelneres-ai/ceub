matriz = [[0.0 for _ in range(5)] for _ in range(2)]
parar = False
contador = 0

for l in range(2):
    for c in range(5):
        valor = float(input(f"Digite o valor [{l}][{c}] (ou 0 para sair): "))
        if valor == 0:
            parar = True
            break
        matriz[l][c] = valor
        contador += 1
    if parar:
        break

soma = 0.0
maiores_que_vinte = 0

for l in range(2):
    for c in range(5):
        soma += matriz[l][c]
        if matriz[l][c] > 20:
            maiores_que_vinte += 1

if contador > 0:
    media = soma / contador
else:
    media = 0.0

print("\n" + "="*35)
print("      VALORES DA MATRIZ      ")
print("="*35)

for l in range(2):
    for c in range(5):
        print(f"{matriz[l][c]:.2f}", end="\t")
    print()

print("="*35)
print(f"Soma total dos elementos: {soma:.2f}")
print(f"Média aritmética: {media:.2f}")
print(f"Valores maiores que 20: {maiores_que_vinte}")
print("="*35)

matriz[1][3] = 13.0

print("\n" + "="*35)
print("   MATRIZ APÓS ALTERAÇÃO [1][3]=13   ")
print("="*35)

for l in range(2):
    for c in range(5):
        print(f"{matriz[l][c]:.2f}", end="\t")
    print()
print("="*35)
