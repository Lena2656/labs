"""
Тесты для лабораторной работы 9 - автоматизация CI/CD
Этот файл содержит примеры тестов, которые будут запускаться автоматически в GitHub Actions
"""

def test_addition():
    """Тест сложения - самый простой тест"""
    result = 2 + 2
    expected = 4
    assert result == expected, f"Ошибка: 2 + 2 должно быть {expected}, а получилось {result}"
    print(" Тест сложения пройден: 2 + 2 = 4")


def test_subtraction():
    """Тест вычитания"""
    result = 10 - 5
    expected = 5
    assert result == expected, f"Ошибка: 10 - 5 должно быть {expected}"
    print(" Тест вычитания пройден: 10 - 5 = 5")


def test_multiplication():
    """Тест умножения"""
    result = 3 * 4
    expected = 12
    assert result == expected, "Ошибка в умножении"
    print(" Тест умножения пройден: 3 × 4 = 12")


def test_division():
    """Тест деления"""
    result = 15 / 3
    expected = 5
    assert result == expected, "Ошибка в делении"
    print(" Тест деления пройден: 15 ÷ 3 = 5")


def test_string_concatenation():
    """Тест конкатенации строк"""
    result = "Hello" + " " + "World"
    expected = "Hello World"
    assert result == expected, "Ошибка в соединении строк"
    print(" Тест строк пройден: 'Hello' + ' ' + 'World' = 'Hello World'")


def test_list_length():
    """Тест работы со списками"""
    my_list = [1, 2, 3, 4, 5]
    result = len(my_list)
    expected = 5
    assert result == expected, f"Список должен содержать {expected} элементов"
    print(" Тест списка пройден: список содержит 5 элементов")


class TestCalculator:
    """Класс для группировки тестов калькулятора"""
    
    def test_power(self):
        """Тест возведения в степень"""
        result = 2 ** 3
        expected = 8
        assert result == expected, "Ошибка в возведении в степень"
        print(" Тест степени пройден: 2³ = 8")
    
    def test_modulo(self):
        """Тест остатка от деления"""
        result = 10 % 3
        expected = 1
        assert result == expected, "Ошибка в остатке от деления"
        print(" Тест остатка от деления пройден: 10 % 3 = 1")


# def test_failing_example():
#    """
 #   Пример НЕУСПЕШНОГО теста для демонстрации
  #  Этот тест намеренно падает, чтобы показать как выглядит ошибка в GitHub Actions
#    ЗАКОММЕНТИРУЙТЕ его, когда тесты должны проходить все
 #   """
#    result = 1 + 1
  #  expected = 3  # Намеренная ошибка: 1+1=2, а не 3
#    assert result == expected, f"Намеренная ошибка: 1+1 должно быть 2, а не {expected}"
#    print(" Этот тест должен падать - это нормально для демонстрации")


# Пример теста с использованием параметризации (раскомментировать если нужно)
# import pytest
# 
# @pytest.mark.parametrize("a,b,expected", [
#     (1, 2, 3),
#     (5, 5, 10),
#     (10, -3, 7),
# ])
# def test_parametrized_addition(a, b, expected):
#     """Параметризованный тест сложения"""
#     result = a + b
#     assert result == expected, f"{a} + {b} должно быть {expected}"
#     print(f" Параметризованный тест: {a} + {b} = {expected}")


def test_always_passes():
    """Этот тест всегда проходит"""
    assert True
    print(" Простой тест на истинность пройден")


if __name__ == "__main__":
    """Если запустить файл напрямую, а не через pytest"""
    print("=" * 50)
    print("Запуск тестов напрямую из файла...")
    print("=" * 50)
    
    # Запускаем тесты вручную
    test_addition()
    test_subtraction()
    test_multiplication()
    test_division()
    test_string_concatenation()
    test_list_length()
    
    calculator = TestCalculator()
    calculator.test_power()
    calculator.test_modulo()
    
    test_always_passes()
    
    print("=" * 50)
    print(" Все тесты прошли успешно!")
    print("=" * 50)