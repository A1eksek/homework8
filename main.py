# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.sides = (a, b, c)
#
#     def is_triangle(self):
#         if not all(isinstance(side, (int, float)) for side in self.sides):
#             return "Нужно вводить только числа!"
#
#         if any(side <= 0 for side in self.sides):
#             return "С отрицательными числами ничего не выйдет!"
#
#         a, b, c = self.sides
#
#         if a + b > c and a + c > b and b + c > a:
#             return "Ура, можно построить треугольник!"
#         else:
#             return "Жаль, но из этого треугольник не сделать."
#
#
# triangle = TriangleChecker(3, 4, 5)
# print(triangle.is_triangle())
#
# triangle_invalid = TriangleChecker(1, -1, 3)
# print(triangle_invalid.is_triangle())
#
# triangle_not_numbers = TriangleChecker(3, '4', 5)
# print(triangle_not_numbers.is_triangle())
#
# triangle_not_possible = TriangleChecker(1, 1, 3)
# print(triangle_not_possible.is_triangle())

class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')


weight = KgToPounds(18)
print(weight.to_pounds())
print(weight.kg)
weight.kg = 42