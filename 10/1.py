# Счет с нуля до бесконечности.

class count_iterator:
    n = 0

    def __iter__(self):
        return self

    def __next__(self):
        y = self.n
        self.n += 1
        return y