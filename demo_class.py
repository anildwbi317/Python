class MyClass:
    """
    Nothing
    """
    def __init__(self, a_x, b_y):
        """
            Nothing
        """
        self.a_x = a_x
        self.b_y = b_y

    def tasks(self):
        """
                Returns sum of the arguments only if both types are int else return -99
        """
        try:
            return self.a_x + self.b_y
        except TypeError:
            return -99


if __name__ == "__main__":
    """
    Nothing
    """
    obj = MyClass(10, 20)
    print(obj.tasks())
    obj1 = MyClass(10, 'a')
    print(obj1.tasks())
