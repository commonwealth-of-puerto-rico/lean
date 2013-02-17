class AgencyElement(object):
    _registry = []

    def __init__(self, link):
        self.link = link
        self.__class__._registry.append(self)

    @classmethod
    def get_all(cls):
        return cls._registry
