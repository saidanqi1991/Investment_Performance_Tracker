class Transcatioin:
    """
    This class is constructed from transcation id and dictionary row read from csv file. 
    """

    def __init__(self, transaction_id, row):
        if transaction_id is None or row is None:
            raise ValueError("transaction_id or csv_row cannot be None.");
        self.transcation_id = transaction_id
        self.date = row["Activity Date"]
        self.instrument = row["Instrument"]
        self.trans_code = row["Trans Code"]
        self.quantity = row["Quantity"]
        self.price = row["Price"]
        self.amount = row["Amount"]

    