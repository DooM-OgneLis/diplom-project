import pytest
from support_test.mock_emul import MocksBurger as smock
from burger import Burger

class TestBurger:
    #Проверка инициализации бургера
    def test_burger_initial_state(self):
         burger = Burger()

         assert burger.bun is None #проверка что булдочка не выбрана
         assert burger.ingredients == [] #проверка что наполнение отсутствует

    #Проверка выбора булочки
    def test_set_buns_set_buns(self):
        burger = Burger()

        #имитируем моком создания булочки
        mock_bun = smock.bun("crrot bun")

        burger.set_buns(mock_bun) #назначаем булочку

        assert burger.bun is mock_bun #проверяем что булочка назначилась
    
    #Проверка замены булочки
    def test_set_buns_replace_buns(self):
        burger = Burger()

        #имитируем моком создания первой булочки
        mock_bun_one = smock.bun("crrot bun")
        mock_bun_two = smock.bun("glass Bun")

        burger.set_buns(mock_bun_one) #назначаем булочку
        assert burger.bun is mock_bun_one, (f"проверь: {burger.bun}, булочка не была назначена или назначена неправильно")  #проверяем что булочка назначилась

        burger.set_buns(mock_bun_two) #изменяем булочку
        assert burger.bun is not mock_bun_one, (f"проверь: {burger.bun}, булочка не поменялась на {mock_bun_two}") #проверяем что булочка не содержит значение первой выбранной булочки
        assert burger.bun is mock_bun_two #проверяем что булочка поменялась

    #проверка добавления ингредиентов в бургер
    def test_add_ingredient_add_ingredients(self):
        burger = Burger()

        #имитируем булочку
        mock_bun = smock.bun("crrot bun")

        #имитируем ингредиент
        mock_ingredient = smock.ingredient()

        #добавляем булочку
        burger.set_buns(mock_bun)

        #добавляем ингредиент
        burger.add_ingredient(mock_ingredient)

        assert mock_ingredient in burger.ingredients

    #проверка добавления нескольких ингредиентов в бургер
    def test_add_ingredient_add_other_ingredients(self):
        burger = Burger()

        count = 4 #для удобства контроля счета ингредиентов
        ing_list = [] #вспомогательный лист для учета изменений в составе

        #имитируем булочку
        mock_bun = smock.bun("crrot bun")

        #добавляем булочку
        burger.set_buns(mock_bun)

        #имитируем ингредиенты
        for i in range (count):
            mock_ingredient = smock.ingredient()

            #добавляем в лист базовой проверки
            ing_list.append(mock_ingredient) #добавляем в лист для сравнения
            #добавляем ингредиент
            burger.add_ingredient(mock_ingredient)
            
        assert len(burger.ingredients) == count, (f"Кол-во присутствующих ингредиентов({len(burger.ingredients)}) не соответствует добавленному ({count})")
        assert ing_list == burger.ingredients, (F"Списки ингредиентов не совпали, проверь /n{ing_list} /n{burger.ingredients}")

    def test_remove_ingredient_delete_ingredient(self):
        burger = Burger()

        #для удобства контроля добавляем переменные настроек:
        count = 4
        index = 2 

        ing_list = [] #вспомогательный лист для учета изменений в составе

        #имитируем булочку
        mock_bun = smock.bun("crrot bun")

        #добавляем булочку
        burger.set_buns(mock_bun)

        #имитируем ингредиенты
        for i in range (count):
            mock_ingredient = smock.ingredient()

            #добавляем в лист базовой проверки
            ing_list.append(mock_ingredient) #добавляем в лист для сравнения
            #добавляем ингредиент
            burger.add_ingredient(mock_ingredient)

        #промежуточная проверка
        assert len(burger.ingredients) == count, (f"что-то пошло не так, Кол-во присутствующих ингредиентов({len(burger.ingredients)}) не соответствует добавленному ({count})")

        #удаляем ингредиент
        burger.remove_ingredient(index)

        assert len(burger.ingredients) == count-1, ("кол-во не уменьшилось или изначально больше добавленного") #проверяем что кол-во уменьшилось на 1
        assert ing_list[index] not in burger.ingredients, ("Продукт обнаружен в списке!") #проверяем что убранный ингридиент полностью отсутствует в списке
        #использование подмены через mock создает уникальные объекты для каждой операции что позволяет проверять наличие даже при полной индетичности объектов

    def test_move_ingredient_drag_ingredient_down(self):
        burger = Burger()
                
         #для удобства контроля добавляем переменные настроек:
        count = 4
        index_start = 2 
        index_finish = 0

        ing_list = [] #вспомогательный лист для учета изменений в составе

        #имитируем булочку
        mock_bun = smock.bun("crrot bun")

        #добавляем булочку
        burger.set_buns(mock_bun)

        #имитируем ингредиенты
        for i in range (count):
            mock_ingredient = smock.ingredient()

            #добавляем в лист базовой проверки
            ing_list.append(mock_ingredient) #добавляем в лист для сравнения
            #добавляем ингредиент
            burger.add_ingredient(mock_ingredient)

        #промежуточная проверка
        assert len(burger.ingredients) == count, (f"что-то пошло не так, Кол-во присутствующих ингредиентов({len(burger.ingredients)}) не соответствует добавленному ({count})")

        burger.move_ingredient(index_start, index_finish)

        assert ing_list[index_start] == burger.ingredients[index_finish]

    @pytest.mark.parametrize("counts", [1, 2, 4, 10, 0])
    def test_get_price_get_value(self, counts):
        burger = Burger()

        count = counts #для удобства контроля счета ингредиентов
        ing_price = 0 #вспомогательный лист для учета изменений в составе

        #имитируем булочку
        mock_bun = smock.bun("crrot bun")

        #добавляем булочку
        burger.set_buns(mock_bun)

        ing_price += mock_bun.get_price() * 2

        #имитируем ингредиенты
        for i in range (count):
            mock_ingredient = smock.ingredient()

            #добавляем в лист базовой проверки
            ing_price += mock_ingredient.get_price() #добавляем в лист для сравнения
            #добавляем ингредиент
            burger.add_ingredient(mock_ingredient)

        #промежуточная проверка
        assert len(burger.ingredients) == count, (f"Кол-во присутствующих ингредиентов({len(burger.ingredients)}) не соответствует добавленному ({count})")
        
        assert burger.get_price() == ing_price #проверяем что ключевая сумма совпадает с набранной в основном бургере

    @pytest.mark.parametrize("counts", [1, 2, 4, 10, 0])
    def test_get_receipt_get_list_receipt(self, counts):
        burger = Burger()
        
        count = counts #для удобства контроля счета ингредиентов
        ing_receipt = '' #вспомогательный лист для учета изменений в составе
        ing_price = 0

        #имитируем булочку
        mock_bun = smock.bun("crrot bun")

        #добавляем булочку
        burger.set_buns(mock_bun)

        ing_receipt += (f'(==== {mock_bun.get_name()} ====)\n')
        ing_price += mock_bun.get_price() * 2

        #имитируем ингредиенты
        for i in range (count):
            mock_ingredient = smock.ingredient()

            #добавляем в лист базовой проверки
            ing_receipt += (f'= {str(mock_ingredient.get_type()).lower()} {mock_ingredient.get_name()} =\n') #добавляем в лист для сравнения
            ing_price += mock_ingredient.get_price()
            #добавляем ингредиент
            burger.add_ingredient(mock_ingredient)

        #промежуточная проверка
        assert len(burger.ingredients) == count, (f"Кол-во присутствующих ингредиентов({len(burger.ingredients)}) не соответствует добавленному ({count})")
        
        ing_receipt += (f'(==== {mock_bun.get_name()} ====)\n\nPrice: {ing_price}')
        
        assert burger.get_receipt() == ing_receipt, (f'рецепт {burger.get_receipt()} не совпал с {ing_receipt} при кол-ве ингредиентов {count}')
