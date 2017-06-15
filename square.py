class Square:
    """Class has method to create single square.

    Attributes:
        row : int
            Indicates on which row square lies.
        column : int
            Indicates on which column square lies.
        is_marked : bool
            True if Square is marked, False otherwise.
    """
    def __init__(self, column, row):
        """Constructs a Square object."""
        self.row = row
        self.column = column
        self.is_marked = False
