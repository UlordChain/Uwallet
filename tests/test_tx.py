import unittest
from uwallet.hashing import sha256

raw_tx = "010000000135ab147b67ef3c95a0c1f21701213c1df1d2953f9f444b73f8f4f3ee73484325010000006a47304402201ca2916c55947a64f52d87047778bb88d5148a3d1db341f0cab49cb4217bc6bc0220563d470f29626a7d7cc4a5e15d460142b8d4e97be904d2ff003d77c1d2ccad2f012103a245eff6a761c317fcf726c4ffa1f1f533e0dea2751181799e954c53e5924dd8ffffffff0200e87648170000001976a914dd7c628298414499ac24183b6de768988b78b9fe88ac048f8d5bba0000001976a914a1d3e2a1601d0172d198fd09c80a32b9cad8789d88ac00000000"
tx_id = "8ea1974409b53afd4042f9596708e9f1e2e5e4113afb6631cb0b1203daa99413"




class TestCreateTx(unittest.TestCase):
    def test_create_txid(self):
        """faile"""
        _tx_sha256 = sha256(raw_tx.decode('hex'))
        _tx_hex = _tx_sha256.encode('hex')
        self.assertEqual(_tx_hex, tx_id)

if __name__ == '__main__':
    unittest.main()
