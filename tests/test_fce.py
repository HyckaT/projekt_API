import transform_fce
import unittest

class TestFunkcion(unittest.TestCase):
    def feet_to_meters(self):
        self.assertAlmostEqual(transform_fce.feet_to_meters(100), 30.48)
        self.assertAlmostEqual(transform_fce.feet_to_meters(200), 50) # zkouška špatných dat
        self.assertIsInstance(transform_fce.kelvin_to_celsius("100"), ValueError, "Nastala chyba")
        #assert transform_fce.kelvin_to_celsius(200) == -73

    def test_kelvin_to_celsius(self):
        self.assertEqual(transform_fce.kelvin_to_celsius(100),-173.14999999999998,"Nastala chyba")
    