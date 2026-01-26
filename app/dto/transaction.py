from datetime import datetime
from decimal import Decimal

class Transaction:
    """
    This class is constructed from transcation id and row list read from csv file. 
    """

    def __init__(self, transaction_id, row):
        if transaction_id is None or row is None:
            raise ValueError("transaction_id or csv_row cannot be None.");
        self.transcation_id = transaction_id
        self.date = datetime.strptime(row[0].strip(), "%m/%d/%Y").date()
        instrument_str = row[3].strip()
        self.instrument = instrument_str if instrument_str else None
        self.description = row[4].strip().replace("\n", " ")
        self.type = row[5].strip()
        qty_str = row[6].strip()
        self.quantity = Decimal(qty_str) if qty_str else None
        price_str = row[7].strip().replace("$", "")
        self.price = Decimal(price_str) if price_str else None
        amount_str = row[8].strip()
        if not amount_str:
            self.amount = Decimal(0)
        elif amount_str.startswith("(") and amount_str.endswith(")"):
            cleaned = amount_str[2:-1].replace(",", "")
            self.amount = -Decimal(cleaned)  #ignore () and $
        else:
            cleaned = amount_str.replace("$", "").replace(",", "")
            self.amount = Decimal(cleaned)

    