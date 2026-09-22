import unittest

from main import aplicar_regla_seguridad


class TestReglaSeguridadViento(unittest.TestCase):

    def setUp(self):
        self.actividades = [
            "Caminata turística",
            "Visitar un parque",
            "Recorrido en bicicleta"
        ]

    def test_viento_menor_a_50(self):
        resultado = aplicar_regla_seguridad(
            49,
            self.actividades
        )

        self.assertFalse(resultado["alerta_seguridad"])
        self.assertEqual(
            resultado["recomendaciones"],
            self.actividades
        )

    def test_viento_igual_a_50(self):
        resultado = aplicar_regla_seguridad(
            50,
            self.actividades
        )

        self.assertFalse(resultado["alerta_seguridad"])
        self.assertEqual(
            resultado["recomendaciones"],
            self.actividades
        )

    def test_viento_superior_a_50(self):
        resultado = aplicar_regla_seguridad(
            51,
            self.actividades
        )

        self.assertTrue(resultado["alerta_seguridad"])
        self.assertEqual(
            resultado["recomendaciones"],
            []
        )


if __name__ == "__main__":
    unittest.main()