class TransTypeMap():
    trans_type_map = {} #empty dictionary to all tranctions grouped by type
    def __init__(self, transactions):
        """constructor that create a dictionary keyed by transaction type and valued by set of transactions"""
        for transcation in transactions.values():
            type = transcation.type
            #add the transcation to the list associated with the transcation type
            if type not in self.trans_type_map: 
                self.trans_type_map[type] = [transcation]
            else:
                self.trans_type_map.get(type).append(transcation)    

    def get_statistics(self):
        """This method calculate the basic statistics of each transaction type and return a dictionary valued by type and keyed by statistics"""
        all_stats = {}
        for type, transactions in self.trans_type_map.items():
            count = 0
            total_amount = 0
            total_quantity = 0
            for transaction in transactions:
                count+=1
                #update amount and quantity if not none
                if transaction.amount: 
                    total_amount += transaction.amount  
                if transaction.quantity:
                    total_quantity += transaction.quantity 
            #save basic statics of current type in dictionary
            type_stats = {}
            type_stats["count"] = count
            type_stats["total_amount"] = total_amount
            type_stats["total_quantity"] = total_quantity
            #save the type : basic statiscs pair in dictionary all_stats 
            all_stats[type] = type_stats
        return all_stats
    
    def print_statistics(self):
        """This method print the basic statics of all transcation types"""
        all_stats = self.get_statistics()
        for type, type_stat in all_stats.items():
            print(f"type: {type}, count: {type_stat.get("count")}, total_amount: {type_stat.get("total_amount")}, total_quantity: {type_stat.get("total_quantity")}")