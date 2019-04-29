from Week3.StockAccount.CompanyWithLinkedList import CompanyShareWithLinkedList
from Week3.StockAccount.Customer import Customer


class StockAccount:
    def __init__(self):
        self.customer = Customer()
        self.new_data_add = CompanyShareWithLinkedList()
        # self.customer.start()

    def stock_account(self):

        while True:
            print("------Share Stock Account--------\n1.Add Customer\n2.Add Company\n" +
                  "3.Remove Customer\n4.Remove Company\n5.Buy\n6.Sell\n7.Save\n8.Print Report\n9.Exit")
            try:
                choice = int(input("Select any one : "))
                if choice <= 0 or choice > 9:
                    raise ValueError
            except Exception or ValueError:
                print("You selected wrong choice.")
                continue

            if choice == 5 or choice == 6:
                try:
                    customer_id = int(input("Enter customer id : "))
                    customer_name = input("Enter customer name : ").strip().upper()
                    if choice == 5:
                        for i in self.customer.company_data:
                            print("Company name : ", i["name"], " \t\tNo of share : ", i["data"]["no_of_share"],
                                  "\t\tPer share price : ", i["data"]["price"])
                    else:
                        for i in self.customer.customer_data:
                            if i["id"] == str(customer_id) and i["name"] == customer_name:
                                print(i["data"])
                    company_name = input("Enter company name : ").strip().upper()
                    no_of_share = int(input("Enter number of share : "))
                    if not customer_name.isalpha() or not company_name.isalpha():
                        raise ValueError
                except ValueError:
                    print("You have entered wrong data.")
                    continue

            service = {1: "add_new_customer", 2: "add_new_company", 3: "remove_customer", 4: "remove_company", 5: "buy",
                       6: "sell", 7: "save", 8: "print_report"}
            if choice == 9:
                self.customer.save()
                return

            if 1 <= choice <= 4:
                fun = getattr(self.new_data_add, service[choice])
                # self.__init__()
                # self.customer.start()
            else:
                fun = getattr(self.customer, service[choice])

            if choice == 5 or choice == 6:
                fun(customer_id, company_name, customer_name, no_of_share)
            else:
                fun()


# Main method
if __name__ == "__main__":
    stock_account = StockAccount()
    stock_account.stock_account()
