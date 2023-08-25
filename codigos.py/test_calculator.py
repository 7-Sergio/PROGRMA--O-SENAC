# TESTE SOMA

# from calculator import add
# import unittest
# from calculator import add

# class testCalculator(unittest.TestCase):
#     def test_add(self):
#          self.assertEqual(add(2, 3), 6)
   
    
#     if __name__ == '__main__':
#         unittest.main()
        

# TESTE SOMA E SUBTRAÇÃO

# import unittest
# from calculator import soma

# class TestSoma(unittest.TestCase):
    
#     def test_soma_positivos(self):
#         self.assertEqual(soma(3, 5), 8)
        
#     def test_soma_negativo(self):
#         self.assertEqual(soma(-2, 8), 6)
        
# if __name__ == '__main__':
#     unittest.main()


#TESTE NUMERO PRIMO

# import unittest
# from calculator import soma

# class TestSoma(unittest.TestCase):
    
#    def eh_primo(num):
#        if num <= 1:
#            return False
#        for i in range(2,num):
#             if num % i == 0:
#                 return False
        
# if __name__ == '__main__':
#     unittest.main()
    
    
# import  unittest
# class TesTprimo(unittest.TestCase):
#     def Test_numero_primo(self):
#         self.assertTrue(eh_primo(7))
        
#         def test_numero_nao_primo(self):
#             self.assert.False(eh_primo(10))


# Criar uma função para validar se uma string é um formato de e-mail válido.

# import unittest 

# class TestValidacaoEmail(unittest.TestCase):
#     def test_email_valido(self):
#         self.assertTrue(validar_email("usuario@example.com"))
        
        
#     def tesst_email_invalido(self):
#         self.assertFalse(TestValidacaoEmail("nao_e_um_email"))


import unittest

from calculator import calcular_media

class TestCalculoMedia(unittest.TestCase):
    def test_media_lista_vazia(self):
        self.assertEqual(calcular_media([]), 0)
        
    def test_media_lista_numeros(self):
        self.assertEqual(calcular_media([2, 4, 6, 8]), 5)