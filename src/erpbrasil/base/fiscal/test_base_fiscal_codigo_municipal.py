import unittest

import codigo_municipal


class Tests(unittest.TestCase):

    def testCodigoValido(self):
        self.assertTrue(codigo_municipal.validar_codigo_municipal(1200013))

    def testCodigoInvalido(self):
        self.assertFalse(codigo_municipal.validar_codigo_municipal(5200013))

if __name__ == '__main__':
    unittest.main()