import unittest
from uwallet.ulord import public_key_to_bc_address

class TestBaseAddr(unittest.TestCase):
    def setUp(self):
        self._pubk = "03d485f9129050d203241ca1227adbfd9c05fe881468642959e52a7f15930eba"

class TestAddr(TestBaseAddr):
    """Test address"""
    def test_main_pubkey_to_addr(self):
        result = public_key_to_bc_address(self._pubk)
        expected = "uUtfyVXZcx68TcXS97XUp74HpcBbCVJg5g"
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()