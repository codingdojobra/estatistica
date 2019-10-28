import unittest

def calcula_estatistica(sequencia):
    try:
        tamanho = len(sequencia)
        minimo = min(sequencia)
        maximo = max(sequencia)
        media = round(sum(sequencia) / tamanho, 2)

        return {"tamanho": tamanho,
                "minimo": minimo,
                "maximo": maximo,
                "media": media}
    except:
        raise

class Test(unittest.TestCase):

    def test_framework(self):
        return self.assertEqual(True, True)

    def test_estatistica_1(self):
        sequencia = [6, 9, 15, -2, 92, 11]
        esperado = {"minimo": -2, "maximo": 92, "tamanho": 6, "media": 21.83}
        return self.assertEqual(calcula_estatistica(sequencia), esperado)

    def test_estatistica_2(self):
        sequencia = [1,2,50,-10]
        esperado = {"minimo": -10, "maximo": 50, "tamanho": 4, "media": 10.75}
        return self.assertEqual(calcula_estatistica(sequencia), esperado)

    def test_estatistica_3(self):
        sequencia = [-10]
        esperado = {"minimo": -10, "maximo": -10, "tamanho": 1, "media": -10}
        return self.assertEqual(calcula_estatistica(sequencia), esperado)

    def test_estatistica_4(self):
        sequencia = []
        with self.assertRaises(ValueError):
            calcula_estatistica(sequencia)

    def test_estatistica_5(self):
        sequencia = 'palavra'
        with self.assertRaises(TypeError):
            calcula_estatistica(sequencia)

    def test_estatistica_6(self):
        sequencia = ['palavra']
        with self.assertRaises(TypeError):
            calcula_estatistica(sequencia)

    def test_estatistica_7(self):
        sequencia = None
        with self.assertRaises(TypeError):
            calcula_estatistica(sequencia)


if __name__ == '__main__':
    unittest.main()
