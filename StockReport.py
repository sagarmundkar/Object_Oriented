import json


class StockReport:
    def __init__(self):
        self.list = []
        with open("json_file/stockreport.json") as data:
            try:
                data = json.load(data)
                for i in data:
                    self.list.append(i)
            except Exception:
                print("File is empty")

    def new_data(self):
        dt = {
            "name": '',
            "share_no": '',
            "Share_Price": ''
        }

        try:
            name = input("Enter the company name:").strip()
            share_no = input("Enter the Number of share: ").strip()
            share_price = input("Enter the share price:").strip()

            # if not name.isalpha() or not share_no.isnumeric() or not share_price.isnumeric():
            #  raise ValueError

        except ValueError:
            print("You have entered wrong data:")

        else:
            dt["name"] = name
            dt["share_no"] = share_no
            dt["Share_Price"] = share_price
            return dt

    def Stock_report(self):
        dt = self.new_data()
        self.list.append(dt)

        with open("json_file/stockreport.json", 'w') as da:
            json.dump(self.list, da)
            print("Company Added")

    def display(self):
        print("Company name\t\tNo of share\t\tPer share price")
        for i in self.list:
            print(i["name"], "\t\t\t\t", i["share_no"], "\t\t\t\t", i["Share_Price"])


if __name__ == "__main__":
    stock = StockReport()
    stock.display()
    stock.Stock_report()
    stock.display()
