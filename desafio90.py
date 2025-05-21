lista = {
    "alunos": [],
    "notas": [],
    "estado": []
}


lista["alunos"] = str(input("Digite o nome do Aluno "))

lista["notas"] = int(input(f"Digite a nota do {lista["alunos"]} "))

print(f"nome igual a {lista["alunos"]}")
print(f"media igual a {lista["notas"]}")

if lista["notas"] >= 6:
    print("Aprovado")
    lista["estado"].append("aprovado")
else:
    print("Reprovado")
    lista["estado"].append("reprovado")