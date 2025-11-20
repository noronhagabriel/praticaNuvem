print("=== Média da Turma ===")

quantidade = int(input("Quantos alunos? "))
soma = 0

for i in range(quantidade):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    soma += nota

media = soma / quantidade

print(f"Média da turma: {media:.2f}")
