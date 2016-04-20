
class Address(object):

    def __init__(self, district, complement):
        self._district = district
        self._complement = complement

    def __str__(self):
        return '%s %s' % (self._complement, self._district)

    """ Set and Get functions """

    def getDistrict(self):
        return self._district

    def setDistrict(self, district):
        self._district = district

    def getComplement(self):
        return self._complement

    def setComplement(self, complement):
        self._complement = complement
