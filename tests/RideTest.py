import unittest
import sys

sys.path.append('../../')
sys.path.append('../')

from core.src.User import User
from core.src.Ride import Ride
from core.src.Address import Address

import datetime

class RideTest(unittest.TestCase):

    def setUp(self):

        self.user1 = User('User1', 'user1@gmail.com', '(83)91234-56789', '114110478', '123456789')
        self.user2 = User('User2', 'user2@gmail.com', '(83)91234-56789', '114110478')

        self.address = Address('Rua da minha casa', 'Meu bairro')

        self.neighborhoods1 = ['bairro da minha amiga', 'lindo olhar', 'alarodrigo', 'pizza do paulista']
        self.neighborhoods2 = ['alto da ufcg', 'branco alto', 'catolo', 'bodocongs', 'um bairro logo ali']
        self.neighborhoods3 = ['bairro dos amigos', 'dez em si1', 'si1 eh legal']

        self.ride1 = Ride(self.user1, 2, self.neighborhoods1)
        self.ride2 = Ride(self.user2, 5, self.neighborhoods2)

    def test_constructor(self):

        ride = Ride(self.user1, 2, self.neighborhoods3)

        self.assertEqual(ride.getDriver(), self.user1)
        self.assertEqual(ride.getNumberOfVacancies(), 2)
        self.assertEqual(ride.isWeekly(), False)
        self.assertEqual(ride.getReadableDate(), datetime.datetime.now().strftime('%d-%m-%Y'))
        self.assertEqual(ride.isFull(), False)
        self.assertEqual(ride.getNumberOfPassengers(), 0)
        self.assertEqual(ride.getRoute(), self.neighborhoods3)
        self.assertEqual(ride.getToUFCG(), False)
        
        #  Test UID
        """
        self.assertEqual(self.ride1.getUid(), 4)
        self.assertEqual(self.ride2.getUid(), 5)
        self.assertEqual(ride.getUid(), 6)"""
        # OLHAR ESSE TESTE QUANDO ACABAR

    def test_addPassenger(self):

        self.assertEqual(self.ride1.isFull(), False)
        self.assertEqual(self.ride1.getNumberOfPassengers(), 0)

        self.ride1.addPassenger(self.user1, self.address)

        self.assertEqual(self.ride1.isFull(), False)
        self.assertEqual(self.ride1.getNumberOfPassengers(), 0)

        self.ride1.addPassenger(self.user2, self.address)

        self.assertEqual(self.ride1.isFull(), False)
        self.assertEqual(self.ride1.getNumberOfPassengers(), 1)

    def test_removePassenger(self):

        self.assertEqual(self.ride1.isFull(), False)
        self.assertEqual(self.ride1.getNumberOfPassengers(), 0)

        self.ride1.addPassenger(self.user1, self.address)

        self.assertEqual(self.ride1.isFull(), False)
        self.assertEqual(self.ride1.getNumberOfPassengers(), 0)

        self.ride1.addPassenger(self.user2, self.address)

        self.assertEqual(self.ride1.isFull(), False)
        self.assertEqual(self.ride1.getNumberOfPassengers(), 1)

        self.ride1.removePassenger(self.user2)

        self.assertEqual(self.ride1.isFull(), False)
        self.assertEqual(self.ride1.getNumberOfPassengers(), 0)

    def test_addNeighborhoodToRoute(self):

        self.assertEqual(len(self.ride1.getRoute()), 4)

        self.ride1.addNeighborhoodToRoute('um bairro bem legal')
        self.ride1.addNeighborhoodToRoute('um bairro nao tao legal')

        self.assertEqual(len(self.ride1.getRoute()), 6)


    def test_weeklyUpdate(self):

        self.ride3 = Ride(self.user1, 2, self.neighborhoods1, date=datetime.datetime(2016, 04, 15))
        self.ride4 = Ride(self.user2, 5, self.neighborhoods2, date=datetime.datetime(2016, 04, 05))

        self.assertEqual(self.ride3.getReadableDate(), '15-04-2016')
        self.assertEqual(self.ride4.getReadableDate(), '05-04-2016')

        self.ride3.setWeekly(True)
        self.ride4.setWeekly(True)

        self.assertEqual(self.ride3.weekly_update(), True)
        self.assertEqual(self.ride4.weekly_update(), True)

        self.assertEqual(self.ride3.getReadableDate(), '22-04-2016')
        self.assertEqual(self.ride4.getReadableDate(), '12-04-2016')

        self.ride3.setWeekly(False)
        self.assertEqual(self.ride3.weekly_update(), False)

        self.assertEqual(self.ride4.weekly_update(), True)

        self.assertEqual(self.ride4.getReadableDate(), '19-04-2016')

    def test_isInTheRoute(self):

        self.assertEqual(self.ride1.isInTheRoute('bairro da minha amiga'), True)
        self.assertEqual(self.ride1.isInTheRoute('alarodrigo'),True)
        self.assertEqual(self.ride1.isInTheRoute('bodocongs'),False)
        self.assertEqual(self.ride1.isInTheRoute('bairro da minha amig'), False)
        self.assertEqual(self.ride2.isInTheRoute('bairro da minha amiga'), False)
        self.assertEqual(self.ride2.isInTheRoute('bodocongs'), True)



if __name__ == '__main__':
    unittest.main()
