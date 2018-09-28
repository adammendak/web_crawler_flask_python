from datetime import datetime


class AbstractTimestampableEntity(object):
    """
    abstrakcyjna encja ktora zapisuje czase kiedy obiekt zostal persistowany lub updatowany
    """

    def __init__(self):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def updated(self):
        self.updated_at = datetime.now()