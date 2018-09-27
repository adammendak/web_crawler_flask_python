from model import AbstractTimestampableEntity


class Domain(AbstractTimestampableEntity):
    """
    Encja opisująca stronę internetową
    """

    def __init__(self, name):
        #  co z id ? ogarnac
        self.name = name
        self.count = 0  # ile razy crawler pobierał dane z tej strony

    def increment_count(self):
        self.count = self.count + 1
