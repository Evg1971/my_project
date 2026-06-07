def sum_numbers(a: int, b: int) -> int:
    second_number = int(
        input(
            "В это поле необходимо ввести второе число, "
            "с которым в последующем будет складываться "
            "первое число. Введите число:\n"
        )
    )

    result = a + second_number

    print(f"Результат сложения: {result}")

    return result


first_number = int(
    input(
        "В это поле необходимо ввести первое число. "
        "Введите число:\n"
    )
)

sum_numbers(first_number, 0)

print("Завершение программы...")