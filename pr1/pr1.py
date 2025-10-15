import math

TOLERANCE = 1e-4
MAX_ITERATIONS = 50
INITIAL_GUESS = 1.0 


def f(x):
    return x ** 2 - 20 * math.sin(x + 2) + 1


def f_prime(x):
    return 2 * x - 20 * math.cos(x + 2)

def phi(x):
    return x - 0.05 * f(x)


def simple_iteration_solver(x0, tol, max_iter):
    x_prev = x0

    for i in range(1, max_iter + 1):
        x_next = phi(x_prev)
        error = abs(x_next - x_prev)

        if error < tol:
            return x_next, i, error

        x_prev = x_next

    return x_prev, max_iter, error


def newton_solver(x0, tol, max_iter):
    x_prev = x0

    for i in range(1, max_iter + 1):
        f_x = f(x_prev)
        f_prime_x = f_prime(x_prev)

        if abs(f_prime_x) < 1e-6:
            return "Помилка (f'(x) = 0)", i, "N/A"

        x_next = x_prev - (f_x / f_prime_x)
        error = abs(x_next - x_prev)

        if error < tol:
            return x_next, i, error

        x_prev = x_next

    return x_prev, max_iter, error

print(f"Задана точність: {TOLERANCE}")
print(f"Початкове наближення (x0): {INITIAL_GUESS}\n")
print("-" * 50)

root_si, iterations_si, error_si = simple_iteration_solver(INITIAL_GUESS, TOLERANCE, MAX_ITERATIONS)

print("\nРЕЗУЛЬТАТИ МЕТОДУ ПРОСТОЇ ІТЕРАЦІЇ")
print(f"1. Корінь (відповідь):   {root_si:.6f}")
print(f"2. Кількість ітерацій:  {iterations_si}")
print(f"3. Фінальна похибка:    {error_si:.6e}")
print(f"4. Досягнута точність:  {error_si < TOLERANCE}")

print("-" * 50)

root_newton, iterations_newton, error_newton = newton_solver(INITIAL_GUESS, TOLERANCE, MAX_ITERATIONS)

print("\nРЕЗУЛЬТАТИ МЕТОДУ НЬЮТОНА")
print(f"1. Корінь (відповідь):   {root_newton:.6f}")
print(f"2. Кількість ітерацій:  {iterations_newton}")
print(f"3. Фінальна похибка:    {error_newton:.6e}")
print(f"4. Досягнута точність:  {error_newton < TOLERANCE}")