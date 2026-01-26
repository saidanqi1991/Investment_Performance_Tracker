class TransTypeMap():
    #dictionary keyed by transaction type and valued by set of transactions
    trans_types = {}
    def __init__(self, transactions):
        for key, value in transactions:
