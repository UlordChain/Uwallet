import  unittest
from uwallet.util import format_satoshis

class TestUtil(unittest.TestCase):
    def test_format_satoshis(self):
        result = format_satoshis(1357)
        expected = "0.00001357"
        self.assertEqual(expected, result,"test format_satoshis failed")

    def test_fromat_satoshis_diff_positive(self):
        result = format_satoshis(2468,is_diff=True)
        expected = "+0.00002468"
        self.assertEqual(expected, result, "test format_satoshis diff positive failed")

    def test_format_satoshis_diff_negative(self):
        result = format_satoshis(-1234, is_diff=True)
        expected = "-0.00001234"
        self.assertEqual(result, expected, "test format_satoshis diff negative failed")