class CalcularNotas:

    @staticmethod
    def calcular_media(n1, n2, n3, n4):
        return (n1 * 0.2) + (n2 * 0.2) + (n3 * 0.3) + (n4 * 0.3)

    @staticmethod
    def verificar_situacao(media):
        if media >= 7.0:
            return "Aprovado"
        elif media >= 6.0 and media < 7.0:
            return "Recuperação"
        elif media > 5.0 and media < 6.0:
            return "Final"
        else:
            return "Reprovado"

    @staticmethod
    def calcular_turma(alunos, notas):
        resultados = []

        for i in range(len(alunos)):
            media = CalcularNotas.calcular_media(
                notas[i][0], notas[i][1], notas[i][2], notas[i][3]
            )
            situacao = CalcularNotas.verificar_situacao(media)
            resultados.append(f"{alunos[i]}: {situacao}")

        return resultados