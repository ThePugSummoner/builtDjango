from django.test import TestCase
from datetime import datetime
from .models import Reservation
# Create your tests here.

class ReservationModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.reservation = Reservation.objects.create (
            name = "John",
            contact = "123456789",
            count = 4,
            notes = "Something here"
        )

    def test_fields(self):
        
        self.assertIsInstance(self.reservation.name, str)

        self.assertIsInstance(self.reservation.contact, str)

        self.assertIsInstance(self.reservation.count, int)

        self.assertIsInstance(self.reservation.notes, str)

    def test_timestamps(self):

        self.assertIsInstance(self.reservation.booking_time, datetime)
