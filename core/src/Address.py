
class Address():

    def __init__(self, street, number, district):

        self._street = street
        self._number = number
        self._district = district

    def __str__(self):
        return self._street + ' ' + self._number + ' ' + self._district

    """ Set and Get functions """

    def getStreet(self):
        return self._street

    def setStreet(self, street):
        self._street = street

    def getNumber(self):
        return self._number

    def setNumber(self, number):
        self._number = number

    def getDistrict(self):
        return self._district

    def setDistrict(self, district):
        self._district = district

