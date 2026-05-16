import pytest
from calcular_notas import CalcularNotas


@pytest.mark.parametrize(
    "nome, n1, n2, n3, n4, situacao_esperada",
    [
        ("Ana", 8, 7, 9, 10, "Aprovado"),
        ("Bruno", 6, 6, 6, 6, "Recuperação"),
        ("Carlos", 5.5, 5.5, 5.5, 5.5, "Final"),
        ("Daniel", 3, 4, 5, 4, "Reprovado"),
        ("Eduarda", 9, 9, 8, 10, "Aprovado"),
        ("Fernando", 7, 6, 7, 6, "Recuperação"),
        ("Gabriela", 6, 5.8, 6.2, 6, "Recuperação"),
        ("Henrique", 5, 5, 5, 6, "Final"),
        ("Isabela", 10, 10, 9, 9, "Aprovado"),
        ("João", 6.5, 6.5, 6.5, 6.5, "Recuperação"),
        ("Karla", 5.9, 5.9, 5.9, 5.9, "Final"),
        ("Lucas", 4, 4, 5, 4, "Reprovado"),
        ("Mariana", 7, 7, 7, 7, "Aprovado"),
        ("Nicolas", 6, 6, 5.5, 6, "Final"),
        ("Olivia", 5, 5, 4.5, 5, "Reprovado"),
    ]
)
def test_calcular_turma(nome, n1, n2, n3, n4, situacao_esperada):
    alunos = [nome]
    notas = [[n1, n2, n3, n4]]

    resultado = CalcularNotas.calcular_turma(alunos, notas)

    esperado = f"{nome}: {situacao_esperada}"

    assert resultado[0] == esperado