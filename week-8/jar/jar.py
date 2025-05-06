class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return '🍪' * self._size

    def deposit(self, n):
        if self._size > self._capacity:
            raise ValueError
        self.size += n


    def withdraw(self, n):
        if n > self._size:
            raise ValueError
        self.size -= n


    @property
    def capacity(self):
         return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not 0 <= value <= self.capacity:
            raise ValueError
        self._size = value
