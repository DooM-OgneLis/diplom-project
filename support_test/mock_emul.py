from bun import Bun
from ingredient import Ingredient
from unittest.mock import Mock
import support_test.generator as gen

'''
в данном месте хранятся действия имитации, 
которые повторяются в модулях тестирования 
разложенные по классам
'''
class MocksBurger:
    #имитирует создание булки
    @staticmethod
    def bun(name):
        mock_bun = Mock(spec=Bun)
        
        mock_bun.get_name.return_value = name
        mock_bun.get_price.return_value = gen.generate_price()
        
        return mock_bun
    
    @staticmethod
    def ingredient():
        mock_ingredient = Mock(spec=Ingredient)

        mock_ingredient.get_type.return_value = gen.random_type_ingredient()
        mock_ingredient.get_name.return_value = gen.generate_ingredient()
        mock_ingredient.get_price.return_value = gen.generate_price()
        
        return mock_ingredient