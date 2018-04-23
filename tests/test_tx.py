import unittest
from uwallet.hashing import sha256

raw_tx = "0100000001e5f8eaf93b96140cfefc42b0b14935a1eb6073a61b21083b3495293fca10306d010000006b483045022100db422bbd44a5879a847b1a326336510a00807799d09c77000c078adc263fd88e022058baa007a7d7b23d413ad905c511552a230478ab3e4c4e26104971e903760aaf01210223b9deaa3c9b2e6f563553052e4f510c80b7eca1de882446dd245797f47bfe8cffffffff0200e40b54020000001976a914dd7c628298414499ac24183b6de768988b78b9fe88ac94176930dd0000001976a914ffb9a19a6a4b10ef29f9a9915affe947b34c069788ac00000000"
tx_id = "9a810d451c0223f9dc5e0f99ef9fbe9390dbf82c8425a6c9f23e12348bb3bd0d"



class TestCreateTx(unittest.TestCase):
    def test_create_txid(self):
        _tx_sha256 = sha256(sha256(raw_tx.decode('hex')))
        _tx_hex = _tx_sha256[::-1].encode('hex')
        self.assertEqual(_tx_hex, tx_id)

if __name__ == '__main__':
    unittest.main()
