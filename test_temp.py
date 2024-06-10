# Глобальная область видимости
global_var = "I'm a global variable"

def outer_function():
    # Нелокальная область видимости
    nonlocal_var = "I'm a nonlocal variable"

    def inner_function():
        # Локальная область видимости
        local_var = "I'm a local variable"
        
        # Доступ к переменным всех трех областей видимости
        print(global_var)    # Доступ к глобальной переменной
        print(nonlocal_var)  # Доступ к нелокальной переменной
        print(local_var)     # Доступ к локальной переменной

    return inner_function

# Создание и вызов функции
inner = outer_function()
inner()
