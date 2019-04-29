from Week3.StockAccount import FileLoad
from week2.LinkedList import LinkedList


class CompanyShareWithLinkedList:
    def __init__(self):
        self.customer_list = LinkedList()
        self.company_list = LinkedList()

    def add_new_customer(self):

        customer_data = FileLoad.json_file_load("json_file/customer.json")
        for i in customer_data:
            self.customer_list.add(i)
        try:
            customer_id = input("Enter customer id : ").strip()
            customer_name = input("Enter customer name : ").strip().upper()
            balance = input("Enter balance to add share market account : ").strip()
            if not customer_id.isnumeric() or not customer_name.isalpha() or not balance.isnumeric():
                raise ValueError
        except ValueError:
            print("You have entered wrong data.")
            return
        data = {}
        new_customer = {"id": customer_id, "name": customer_name, "balance": balance, "data": data}
        flag = True
        for i in range(self.customer_list.size()):
            temp = self.customer_list.get_by_index(i)
            if temp["id"] == customer_id or str(temp["name"]) == customer_name:
                print("Your account already available.")
                flag = False
                break
        if flag:
            self.customer_list.add(new_customer)

        list = []
        size = self.customer_list.size()
        for i in range(size):
            list.append(self.customer_list.poll_first())

        FileLoad.json_file_write("json_file/customer.json", list)

    def add_new_company(self):

        company_data = FileLoad.json_file_load("json_file/company.json")
        for i in company_data:
            self.company_list.add(i)
        try:
            company_name = input("Enter company name : ").strip().upper()
            no_of_share = input("Enter number of share : ").strip()
            price = input("Enter share per price : ").strip()
            balance = input("Enter balance amount : ").strip()
            if not company_name.isalpha() or not no_of_share.isnumeric() or not price.isnumeric() or not balance.isnumeric():
                raise ValueError
        except ValueError:
            print("You have entered wrong data.")
            return

        new_company = {company_name: {"no_of_share": no_of_share, "price": price, "balance": balance}}
        flag = True
        for i in range(self.company_list.size()):
            data = self.company_list.get_by_index(i)
            if data.get(company_name) == None:
                print("Your account already available.")
                flag = False
                break
        if flag:
            self.company_list.add(new_company)

        list = []
        size = self.company_list.size()
        for i in range(size):
            list.append(self.company_list.poll_first())
        # print(self.company_list.display())

    def remove_customer(self):

        customer_data = FileLoad.json_file_load("json_file/customer.json")
        for i in customer_data:
            self.customer_list.add(i)
        try:
            customer_id = input("Enter customer id : ").strip()
            customer_name = input("Enter customer name : ").strip().upper()
            if not customer_id.isnumeric() or not customer_name.isalpha():
                raise ValueError
        except ValueError:
            print("You have entered wrong data.")
            return

        for i in range(self.customer_list.size()):
            temp = self.customer_list.get_by_index(i)
            if temp["id"] == customer_id or str(temp["name"]) == customer_name:
                self.customer_list.delete_by_index(i)
                break

        list = []
        size = self.customer_list.size()
        for i in range(size):
            list.append(self.customer_list.poll_first())

        FileLoad.json_file_write("json_file/customer.json", list)

    def remove_company(self):

        company_data = FileLoad.json_file_load("json_file/company.json")
        for i in company_data:
            self.company_list.add(i)
        try:
            company_name = input("Enter company name : ").strip().upper()
            if not company_name.isalpha():
                raise ValueError
        except ValueError:
            print("You have entered wrong data.")
            return

        flag = True
        for i in range(self.company_list.size()):
            data = self.company_list.get_by_index(i)
            if data.get(company_name) == None:
                self.company_list.delete_by_index(i)
                break

        list = []
        size = self.company_list.size()
        for i in range(size):
            list.append(self.company_list.poll_first())
        # print(self.company_list.display())

    def save(self):
        pass


# Main method
if __name__ == "__main__":
    obj = CompanyShareWithLinkedList()
    obj.add_new_company()
