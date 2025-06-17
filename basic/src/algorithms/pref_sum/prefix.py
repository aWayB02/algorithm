class PrefixSum:
    """
    Класс для работы с префиксными сумм
    Принимает список чисел и строит массив префиксных сумм
    """

    def __init__(self, nums: list):

        self.prefix_arr = [0]
        for num in nums:
            self.prefix_arr.append(self.prefix_arr[-1] + num)

    def prefix_sum(self, l, r) -> int:
        """
        Вычисляет сумму элементов от l до r (включительно)

        Args:

            l (int): Левая граница (1-индексация)
            r (int): Правая граница (1-индексация)


        Returns:
            int: Сумма элементов от l до r включительно
        """
        return self.prefix_arr[r] - self.prefix_arr[l - 1]
