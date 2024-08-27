def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()



test_function()

inner_function()
# ЗДЕСЬ НЕ РАБОТАЕТ! (ошибка)
# Вызов функци inner_function() вне функции test_function приводит к появлению ошбики -
# NameError: name 'inner_function' is not defined
# вследствие различия пространства имён, т.к.  мы не можем доставать значения внутри функции (извне)
