public class SistemaNotas {

    public static double calcularMedia(double n1, double n2, double n3, double n4) {
        return (n1 * 0.2) + (n2 * 0.2) + (n3 * 0.3) + (n4 * 0.3);
    }

    public static String verificarSituacao(double media) {
        if (media >= 7) {
            return "Aprovado";
        } 
        else if (media >= 6) {
            return "Recuperação";
        } 
        else if (media > 5) {
            return "Final";
        } 
        else {
            return "Reprovado";
        }
    }

    public static String[] calcularTurma(String[] alunos, double[][] notas) {

        String[] resultados = new String[alunos.length];

        for (int i = 0; i < alunos.length; i++) {
            double media = calcularMedia(notas[i][0], notas[i][1], notas[i][2], notas[i][3]);
            String situacao = verificarSituacao(media);
            resultados[i] = alunos[i] + ": " + situacao;
        }

        return resultados;
    }
}
