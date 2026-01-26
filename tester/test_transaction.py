import unittest

from app.util.transaction_loader import *
from app.dto.transaction import *

class TransactionTester(unittest.TestCase):

    def test_create_transaction(self):
        """Test the constructor of Transaction"""
        row1 = ["12/30/2024","12/30/2024","12/31/2024","TLT","iShares 20+ Year Treasury Bond ETF CUSIP: 464287432 Recurring","Buy","0.113843","$87.84","($10.00)"]
        
        transaction1 = Transaction("12302024000001", row1)
        date1 = datetime.strptime("12/30/2024", "%m/%d/%Y").date()
        self.assertEqual(date1, transaction1.date)
        self.assertEqual("TLT", transaction1.instrument)
        self.assertEqual("iShares 20+ Year Treasury Bond ETF CUSIP: 464287432 Recurring", transaction1.description)
        self.assertEqual("Buy", transaction1.type)
        self.assertEqual(Decimal("0.113843"), transaction1.quantity)
        self.assertEqual(Decimal("87.84"), transaction1.price)
        self.assertEqual(Decimal("-10.00"), transaction1.amount)

        row2 = ["12/17/2024","12/17/2024","12/18/2024","","ACH Deposit","ACH","","","$30.00"]
        transaction2 = Transaction("12302024000002", row2)
        date2 = datetime.strptime("12/17/2024", "%m/%d/%Y").date()
        self.assertEqual(date2, transaction2.date)
        self.assertIsNone(transaction2.instrument)
        self.assertEqual("ACH Deposit", transaction2.description)
        self.assertEqual("ACH", transaction2.type)
        self.assertIsNone(transaction2.quantity)
        self.assertIsNone(transaction2.price)
        self.assertEqual(Decimal("30.00"), transaction2.amount)


    def test_transaction_loader(self):
        """Test constructor and function import_and_create_dictionary of TranscationLoader """
        data2024 = TransactionLoader('data/2024.csv')
        transaction2024 = data2024.import_and_create_dictionary()
        transaction1 = transaction2024.get("12302024000001")
        date1 = datetime.strptime("12/30/2024", "%m/%d/%Y").date()
        self.assertEqual(date1, transaction1.date)
        self.assertEqual("TLT", transaction1.instrument)
        self.assertEqual("iShares 20+ Year Treasury Bond ETF CUSIP: 464287432 Recurring", transaction1.description)
        self.assertEqual("Buy", transaction1.type)
        self.assertEqual(Decimal("0.113843"), transaction1.quantity)
        self.assertEqual(Decimal("87.84"), transaction1.price)
        self.assertEqual(Decimal("-10.00"), transaction1.amount)

        self.assertEqual(392, len(transaction2024))

if __name__ == '__main__':
    unittest.main()