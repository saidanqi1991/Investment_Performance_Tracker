import csv

from app.dto.transaction import *

class TransactionLoader:
    """
    This class load and save transaction activities from given csv file.
    """

    def __init__(self, path_to_csv):
        self.path_to_csv = path_to_csv

    def import_and_create_dictionary(self):
        """
        Read given csv file. Generate transaction_id, create Transaction, and save transaction_id:Transaction pair in transactions dictionary. 
        """
        #empty dictory to store all transaction activities
        transactions = {}
        counter = 0
        with open(self.path_to_csv, newline='') as f:
            reader = csv.reader(f)
            next(reader)     #skip header
            for line in reader:
                #each valid row must have 9 fields
                if len(line) != 9:
                    continue
                counter += 1
                #tranction id is 8 date digit + 6 digits of counter
                date_part = line[0].strip().replace('/', '')
                transaction_id = f"{date_part}{counter:06d}"  
                transactions[transaction_id] = Transaction(transaction_id, line)
                
        return transactions