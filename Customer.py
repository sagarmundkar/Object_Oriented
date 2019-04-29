import datetime

from Week3.StockAccount import FileLoad
from Week3.StockAccount.DateTimeTransactionWithQueue import TransactionQueue
from Week3.StockAccount.TransactionWithStack import TransactionStack


class Customer:
    def __init__(self):
        self.company_data = FileLoad.json_file_load("json_file/company.json")
        self.customer_data = FileLoad.json_file_load("json_file/customer.json")
        self.transaction_queue = TransactionQueue()
        self.transaction_stack = TransactionStack()
        self.cus_index = 0

    def buy(self, customer_id, customer_name, company_name, no_of_share):
        cus_index = 0
        flag = True
        for i in range(len(self.customer_data)):
            if int(self.customer_data[i]["id"]) == customer_id and self.customer_data[i]["name"] == customer_name:
                cus_index = i
                flag = False
                self.cus_index = i
        if flag:
            print("Customer data not found.")
            return

        com_index = 0
        flag = True
        for i in range(len(self.company_data)):
            # print(self.company_data[i]["name"], company_name)
            if company_name == self.company_data[i]["name"]:
                com_index = i
                flag = False
                break
        if flag:
            print("Company data not found.")
            return
        print("company data :", self.company_data[com_index])

        total_amount = no_of_share * int(self.company_data[com_index]["data"]["price"])

        if int(self.customer_data[cus_index].get("balance")) >= total_amount and int(
                self.company_data[com_index]["data"].get("no_of_share")) >= no_of_share:
            self.customer_data[cus_index]["balance"] = str(
                int(self.customer_data[cus_index].get("balance")) - total_amount)
            try:
                self.customer_data[cus_index]["data"][company_name] = str(
                    int(self.customer_data[cus_index]["data"].get(company_name)) + no_of_share)
            except Exception:
                self.customer_data[cus_index]["data"][company_name] = str(no_of_share)
            # print(self.company_data[company_name].get("no_of_share"))
            self.company_data[com_index]["data"]["no_of_share"] = str(
                int(self.company_data[com_index]["data"].get("no_of_share")) - no_of_share)
            self.company_data[com_index]["data"]["balance"] = str(
                int(self.company_data[com_index]["data"]["balance"]) + total_amount)

            self.transaction_queue.transaction_queue("BUY", customer_name, company_name, str(no_of_share),
                                                     str(total_amount),
                                                     str(datetime.datetime.now()))
            self.transaction_stack.transaction_stack("BUY", customer_name, company_name, str(no_of_share),
                                                     str(total_amount),
                                                     str(datetime.datetime.now()))
        else:
            print("company or customer don't have enough share and money.")

    def sell(self, customer_id, company_name, customer_name, no_of_share):

        cus_index = 0
        flag = True
        for i in range(len(self.customer_data)):
            if int(self.customer_data[i]["id"]) == customer_id and self.customer_data[i]["name"] == customer_name:
                cus_index = i
                flag = False
                self.cus_index = i
            if flag:
                print("Customer data not found.")
                return
            flag = True
            com_index = 0
            for i in range(len(self.company_data)):
                if company_name == self.company_data[i]["name"]:
                    com_index = i
                    flag = False
            if flag:
                print("Company data not found.")
                return

            total_amount = no_of_share * int(self.company_data[com_index]["data"]["price"])

            if int(self.company_data[com_index]["data"].get("balance")) >= total_amount and int(
                    self.customer_data[cus_index]["data"].get(company_name)) >= no_of_share:
                self.customer_data[cus_index]["balance"] = str(
                    int(self.customer_data[cus_index].get("balance")) + total_amount)
                self.customer_data[cus_index]["data"][company_name] = str(
                    int(self.customer_data[cus_index]["data"].get(company_name)) - no_of_share)
                # print(self.company_data[company_name].get("no_of_share"))
                self.company_data[com_index]["data"]["no_of_share"] = str(
                    int(self.company_data[com_index]["data"].get("no_of_share")) + no_of_share)
                self.company_data[com_index]["data"]["balance"] = str(
                    int(self.company_data[com_index]["data"]["balance"]) - total_amount)
                self.transaction_queue.transaction_queue("SELL", customer_name, company_name, str(no_of_share),
                                                         str(total_amount),
                                                         str(datetime.datetime.now()))
                self.transaction_stack.transaction_stack("SELL", customer_name, company_name, str(no_of_share),
                                                         str(total_amount),
                                                         str(datetime.datetime.now()))
            else:
                print("company or customer don't have enough share and money.")

    def save(self):
        if self.company_data == None or self.customer_data == None:
            print("Data is not read")
            return
        FileLoad.json_file_write("Customer.json", self.customer_data)
        FileLoad.json_file_write("Company.json", self.company_data)
        Customer()
        self.transaction_queue.save_transaction()
        self.transaction_stack.save_transaction()

    def print_report(self):
        print(self.customer_data[self.cus_index])

    # Main method


if __name__ == "__main__":
    pass
    # obj = Customer()
    # obj.buy(1234, "Google", "jenny", 10)
    # # obj.sell(1234, "Google", "jenny", 10)
    # obj.save()
