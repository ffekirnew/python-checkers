from checkers.enums import CheckerType


class Checker:
    def __init__(self, type: CheckerType = CheckerType.NONE):
        self.__type = type

    @property
    def type(self):
        return self.__type

    def change_type(self, type: CheckerType):
        """Change the type of the checker."""
        self.__type = type
