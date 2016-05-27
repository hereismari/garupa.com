
class Address(object):

    def __init__(self, district, complement):
        self._district = district
        self._complement = complement

    def get_district(self):
        return self._district

    def get_complement(self):
        return self._complement
