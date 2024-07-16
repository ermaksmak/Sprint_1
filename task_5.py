class TestCase:

    def __init__(self):
        self.steps = {} # Инициализация пустого словаря для шагов
        self.result = None # Инициализация ожидаемого результата

    def set_step(self, step_number, step_text):
        self.steps[step_number] = step_text # Добавление шага в словарь

    def delete_step(self, step_number):
        if step_number in self.steps: # Проверка наличия шага в словаре перед удалением
            del self.steps[step_number]

    def set_result(self, result):
        self.result = result # Установка ожидаемого результата

    def get_test_case(self):
        print({ # Вывод содержимого тест-кейса
            'Шаги': self.steps,
            'Ожидаемый результат': self.result
        })

def run5():
    test_case_1 = TestCase()
    test_case_1.set_step(1, 'Перейти на сайт')
    test_case_1.set_step(3, 'Перейти в раздел Товары')
    test_case_1.delete_step(3)
    test_case_1.set_step(2, 'Перейти в раздел Товары')
    test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
    test_case_1.set_result('Товар окажется в корзине')
    test_case_1.get_test_case()
    test_case_2 = TestCase()
    test_case_2.set_step(1, 'Перейти на сайт')
    test_case_2.set_step(2, 'Перейти в раздел Корзина')
    test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
    test_case_2.set_result('Товар удален из корзины')
    test_case_2.get_test_case()