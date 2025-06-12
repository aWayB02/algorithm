class PrefixSum:
    """
    Класс для создания префиксных сумм. Принимает массив в качестве параметров
    и создает префиксный массив на его основе.
    """

    def __init__(self, nums: list, one_based=False):

        self.prefix_arr = [0]
        for num in nums:
            self.prefix_arr.append(self.prefix_arr[-1] + num)

    def sum(self, l, r):
        return self.prefix_arr[r] - self.prefix_arr[l - 1]
