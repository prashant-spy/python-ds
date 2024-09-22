class singleton:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


if __name__ == '__main__':
    s1 = singleton.get_instance()
    s2 = singleton.get_instance()
    # Both pointing to same object
    print(s1 == s2)
