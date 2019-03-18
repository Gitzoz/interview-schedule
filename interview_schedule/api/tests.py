from django.test import TestCase
from .models import AppointmentSlot
from .validators import *
import datetime

class ValidationTestCase(TestCase):
    def test_begin_must_before_end(self):
        begin = datetime.datetime.strptime('2018-06-29T08:15', '%Y-%m-%dT%H:%M')
        end = datetime.datetime.strptime('2018-06-28T08:15', '%Y-%m-%dT%H:%M')
        self.assertRaises(serializers.ValidationError, beginIsBeforeEnd, begin, end)

    def test_begin_is_before_end(self):
        end = datetime.datetime.strptime('2018-06-29T08:15', '%Y-%m-%dT%H:%M')
        begin = datetime.datetime.strptime('2018-06-28T08:15', '%Y-%m-%dT%H:%M')
        result = beginIsBeforeEnd(begin, end)
        self.assertEqual(True, result)

    def test_date_must_be_at_full_hour(self):
        date = datetime.datetime.strptime('2018-06-29T08:15', '%Y-%m-%dT%H:%M')
        self.assertRaises(serializers.ValidationError, mustBeAtFullHour, date)

    def test_date_is_at_full_hour(self):
        date = datetime.datetime.strptime('2018-06-29T08:00', '%Y-%m-%dT%H:%M')
        self.assertEqual(mustBeAtFullHour(date), date)

