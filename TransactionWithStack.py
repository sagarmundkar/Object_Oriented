import json

from week2.Stack import Stack


class TransactionStack:
    def __init__(self):

        self.stack = Stack()
        with open("json_file/Transaction_Stack.json") as data:
            try:
                temp = json.load(data)
            except Exception:
                pass
            else:
                for i in temp:
                    self.stack.push(i)

    def transaction_stack(self, transaction, customer_name, company_name, no_of_share, cost, time):

        new_transaction = {"transaction": transaction, "customer_name": customer_name, "company_name": company_name,
                           "no_of_share": no_of_share, "cost": cost, "time": time}
        self.stack.push(new_transaction)

    def save_transaction(self):

        temp1 = []
        size = self.stack.size()
        for i in range(size):
            temp1.append(self.stack.pop())
        with open("Transaction_stack.json", 'w') as data:
            json.dump(temp1, data)


# Main method
if __name__ == "__main__":
    pass
