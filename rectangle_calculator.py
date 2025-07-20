# Простой калькулятор площади и периметра прямоугольника

def calculate_rectangle_properties(length, width):
    """
    Вычисляет площадь и периметр прямоугольника.
    """
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

def main():
    print("Добро пожаловать в калькулятор прямоугольника!")

    try:
        # Введите длину прямоугольника
        length_str = input("Введите длину прямоугольника: ")
        length = float(length_str)

        # Введите ширину прямоугольника
        width_str = input("Введите ширину прямоугольника: ")
        width = float(width_str)

        if length <= 0 or width <= 0:
            print("Длина и ширина должны быть положительными числами.")
        else:
            area, perimeter = calculate_rectangle_properties(length, width)
            print(f"\nПлощадь прямоугольника: {area}")
            print(f"Периметр прямоугольника: {perimeter}")
    except ValueError:
        print("Ошибка: Введите числовое значение для длины и ширины.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()
