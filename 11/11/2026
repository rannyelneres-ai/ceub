# ceub
11/11/2026
matriz = [[0.0 for _ in range(5)] for _ in range(2)]
parar = False

for l in range(2):
    for c in range(5):
        valor = float(input(f"Digite o valor [{l}][{c}] (ou 0 para sair): "))
        if valor == 0:
            parar = True
            break
        matriz[l][c] = valor
    if parar:
        break

soma = 0.0
for l in range(2):
    for c in range(5):
        soma += matriz[l][c]

print("\n" + "="*30)
print("      VALORES DA MATRIZ      ")
print("="*30)

for l in range(2):
    for c in range(5):
        print(f"{matriz[l][c]:.2f}", end="\t")
    print()

print("="*30)
print(f"Soma total dos elementos: {soma:.2f}")
print("="*30)
