
"""My module docstring"""


class MyClass:
    """This is my class"""



class MySecondClass:
    """MySeconfClass inherits from :class:`MyClass`"""

    def mymethod(self):
        """*This* **is** ``mymethod`` with `a link <https://google.com>`_"""
        pass

    def mysecondmethod(self):
        """This one has a reference to a section in the docs :ref:`header3_target`."""
        pass

    def mynapoleon(self, arg1, arg2):
        """This method has args

        Args:
            arg1 (int): This **has** to be an int
            args2 (str): And this maybe a string

        Returns:
            float: Whatever it gives

        """
