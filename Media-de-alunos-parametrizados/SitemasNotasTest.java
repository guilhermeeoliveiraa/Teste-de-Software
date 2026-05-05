import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

public class SitemasNotasTest {

    @ParameterizedTest
    @CsvSource({
        "Ana, 8, 7, 9, 10, Aprovado",
        "Bruno, 6, 6, 6, 6, Recuperação",
        "Carlos, 5.5, 5.5, 5.5, 5.5, Final",
        "Daniel, 3, 4, 5, 4, Reprovado"
    })
    void testeCalcularTurma(String nome, double n1, double n2, double n3, double n4, String situacaoEsperada) {

        String[] alunos = { nome };

        double[][] notas = {
            { n1, n2, n3, n4 }
        };

        String[] resultado = CalcularNotas.calcularTurma(alunos, notas);

        String esperado = nome + ": " + situacaoEsperada;

        assertEquals(esperado, resultado[0]);
    }
}