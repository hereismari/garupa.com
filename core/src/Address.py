
class Address(object):

    def __init__(self, district, complement):
        self._district = district
        self._complement = complement

    def __str__(self):
        return '%s %s' % (self._complement, self._district)

    """ Set and Get functions """

    def get_district(self):
        return self._district

    def set_district(self, district):
        self._district = district

    def get_complement(self):
        return self._complement

    def set_complement(self, complement):
        self._complement = complement
