from .funcs import square


class SomeClass(object):
    """
    This is some class
    """
    def __init__(self, a: str, b: float):
        self.a = a
        self.b = b

    def do_smth(self, c: int):
        """
        Multiplies b property and c

        Parameters
        ----------
        c: int
            Some parameter

        Returns
        -------
        float
            multiplication
        """
        return self.b * c

class AnotherClass(object):
    """
    Another class
    """

    def __init__(self, d: int):
        self.d = d

    def sqrt(self):
        """
        Returns squared d property

        Returns
        -------
        int
            Squared d property
        """
        return square(self.d)
