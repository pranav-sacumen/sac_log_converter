"""Test cases for leef to json."""
# import unittest

# from sac_log_converter import convert_leef_to_json  # pylint: disable=C0103


# class TestSequenceFunctions(unittest.TestCase):
#     """Testing the function sequences."""

#     def setUp(self):
#         """Set up the objects."""
#         self.l = convert_leef_to_json.convert_leef_to_json_Logger(
#             "TestVendor", "TestName", convert_leef_to_json.__version__)

#     def test_delimeter_error(self):
#         """Testing the delimiter errors."""
#         with self.assertRaises(ValueError):
#             convert_leef_to_json.convert_leef_to_json_Logger(
#                 "TestVendor", "TestName", convert_leef_to_json.__version__, delimiter="a")
#             raise ValueError("value not found")

#     def testLogger(self):
#         """Testing the logger."""
#         self.assertEqual(self.l.product_vendor, "TestVendor")
#         self.assertEqual(
#             self.l.product_name, "TestName")
#         self.assertEqual(
#             self.l.product_version, convert_leef_to_json.__version__)

#     def testEventString(self):
#         """Testing event string."""
#         keys = {"key1": "value1",
#                 "key2": "value2",
#                 "key3": "value3",
#                 }

#         event_id = 1989

#         header = "convert_leef_to_json:1.0|TestVendor|TestName|{0}|{1}|". \
#                  format(convert_leef_to_json.__version__,
#                         str(event_id))

#         attributes = "key1=value1\tkey2=value2\tkey3=value3"

#         expected = header + attributes

#         test_string = self.l.logEvent("1989", keys)
#         self.assertEqual(test_string, expected)


# if __name__ == "__main__":
#     unittest.main()
