class DataLoader:
    def __init__(self):
        self._data = None

    def get_data(self):
        if self._data is None:
            print("Loading data...")
            self._data = [i for i in range(1000)]
        return self._data

loader = DataLoader()

print(loader.get_data())
print(loader.get_data())  # ikkinchi marta load bo‘lmaydi
