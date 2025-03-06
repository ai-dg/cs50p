class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.cookies = ""
        self.quantity = 0

    def __str__(self):
        return f"{self.cookies}"

    def deposit(self, n):
        if n > (self.capacity - self.quantity) or n < 0:
            raise ValueError("Invalid number of deposit")
        self.cookies += "🍪" * n
        self.quantity += n

    def withdraw(self, n):
        if n < 0 or n > self.quantity:
            raise ValueError("Invalid number of withdraw")
        self.cookies = self.cookies[:-n]
        self.quantity -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Capacity must not be non-negative number.")
        self._capacity = value

    @property
    def size(self):
        return self.quantity


def main():
    cookies = Jar(capacity=12)

    cookies.deposit(5)
    print(cookies)

    cookies.withdraw(2)
    print(cookies)


if __name__ == "__main__":
    main()
