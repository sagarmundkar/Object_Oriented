import json


class DataManagement:
    def __init__(self):
        price1 = weight1 = 0
        with open("json_file/datamangement.json") as json_file:
            data = json.load(json_file)
            for i in data:
                print("***********", i, "*************")
                for j in data[i]:
                    price1 += int(j["price"])
                    weight1 += int(j["weight"])
                print("Price : ", price1)
                print("Weight : ", weight1)


if __name__ == "__main__":
    obj = DataManagement()
