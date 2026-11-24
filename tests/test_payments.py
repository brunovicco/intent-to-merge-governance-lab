import unittest
from app.payments import authorize, register

class PaymentContract(unittest.TestCase):
    def test_authorization(self):
        self.assertTrue(authorize("payment-operator"))
        self.assertFalse(authorize("guest"))
    def test_invalid(self):
        for amount in (0,-1):
            with self.assertRaises(ValueError): register({}, "a", amount)
    def test_idempotency(self):
        store={}; first=register(store,"a",10)
        self.assertEqual(first, register(store,"a",10))
        self.assertEqual(len(store),1)
        self.assertNotEqual(first["id"],register(store,"b",10)["id"])
    def test_conflict(self):
        store={}; first=register(store,"a",10)
        with self.assertRaises(ValueError): register(store,"a",20)
        self.assertEqual(store,{"a":first})

if __name__ == "__main__": unittest.main()
