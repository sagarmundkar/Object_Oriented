import json
from re import search


class service:
    def __init__(self):
        self.Person_data = []
        self.file_name = None

    def Create(self):
        try:
            file_name = input("Enter the file name:")
            if search("[a-zA-Z]", file_name) is not None:
                f = open(file_name + ".json", "w+")
                f.close()

            else:
                raise ValueError

        except IOError:
            print("File is not Found.")

    def Open(self):
        file_name = input("Enter the file name")
        try:
            with open(file_name + ".json") as data:
                self.Person_data = json.load(data)
                self.file_name = file_name
        except IOError:
            print("File is not Found.")

    def Save(self):
        try:
            with open(self.file_name + ".json") as data:
                data = json.dump(self.Person_data, data)
                data.close()
        except Exception:
            print("File is not saved")

    def AddPerson(self):
        try:
            first_name = input("Enter the name:")
            last_name = input("Enter the Full name")
            address = input("Enter the address")
            city = input("Enter the city name")
            state = input("Enter the state name")
            zip_code = int(input("Enter the zip code"))
            phone_number = int(input("Enter the mobile number"))

            if not first_name.isalpha() and not last_name.isalpha() and not address.isalpha() and not city.isalpha() and not state.isalpha() and not zip_code.isnumeric and not phone_number.isnumeric():
                raise ValueError

        except ValueError:
            print("You have entered your data.")

        else:
            new_person = {"data": {}}
            new_person["data"]["address"] = address
            new_person["data"]["city"] = city
            new_person["data"]["state"] = state
            new_person["data"]["zip_code"] = zip_code
            new_person["data"]["phone_number"] = phone_number
            flag = True

            for i in self.Person_data:
                if i["first_name"] == first_name and i["last_name"] == last_name:
                    print("Duplicate data")
                    flag = False
                    break

            if flag:
                self.Person_data.append(new_person)
                print(self.Person_data)

    def delete_person(self):
        try:
            first_name = input("Enter the first name:").upper()
            last_name = input("Enter the last name").upper()
            if first_name.isalpha() and not last_name.isalpha():
                raise ValueError
        except ValueError:
            print("You have entered data in alphabetic")

        else:
            for i in range(len(self.Person_data)):
                if self.Person_data[i]["first_name"] == first_name and self.Person_data[i]["last_name"] == last_name:
                    self.Person_data.remove(self.Person_data[i])
                    print("Data Deleted")
                    break

    def edit_person(self):

        print("Enter data for editing")
        try:
            first_name = input("Enter first name : ").strip().upper()
            last_name = input("Enter last name : ").strip().upper()
            if not first_name.isalpha() and not last_name.isalpha():
                raise ValueError
        except ValueError:
            print("You have to enter name in alphabet.")
        else:
            flag = True
            for i in range(len(self.Person_data)):
                if self.Person_data[i]["first_name"] == first_name and self.Person_data[i]["last_name"] == last_name:
                    flag = False
                    while True:
                        choice = int(input(
                            "\t1.First Name\n\t2.Last Name\n\t3.Addresss\n\t4.City\n\t5.State\n\t6.Zip Code\n\t7.Mobile Number\n\t8.Nothing want to change\n\tSelect choice : "))
                        if choice == 1:
                            first = input("Enter first name : ").strip().upper()
                            if not first.isalpha():
                                print("You have to enter first name in alphabet.")
                            else:
                                self.Person_data[i]["first_name"] = first
                        elif choice == 2:
                            last = input("Enter last name : ").strip().upper()
                            if not last.isalpha():
                                print("You have to enter last name in alphabet.")
                            else:
                                self.Person_data[i]["last_name"] = last
                        elif choice == 3:
                            addr = input("Enter address : ").strip().upper()
                            self.Person_data[i]["data"]["address"] = addr
                        elif choice == 4:
                            city = input("Enter city : ").strip().upper()
                            if not city.isalpha():
                                print("You have to enter city in alphabet.")
                            else:
                                self.Person_data[i]["data"]["city"] = city
                        elif choice == 5:
                            state = input("Enter state : ").strip().upper()
                            if not state.isalpha():
                                print("You have to enter state in alphabet.")
                            else:
                                self.Person_data[i]["data"]["state"] = state
                        elif choice == 6:
                            zip_code = input("Enter zip code : ").strip()
                            if not zip_code.isnumeric() and len(zip_code) != 6:
                                print("You have to enter zip code in numeric with 6 digit.")
                            else:
                                self.Person_data[i]["data"]["zip_code"] = zip_code
                        elif choice == 7:
                            phone_number = input("Enter phone number : ").strip()
                            if not phone_number.isnumeric() and len(phone_number) == 10:
                                print("You have to enter phone number in numeric with 10 digit.")
                            else:
                                self.Person_data[i]["data"]["phone_number"] = phone_number
                        elif choice == 8:
                            return
                        else:
                            print("You selected wrong choice.")
            if flag:
                print("Data not available.")


# Main method
if __name__ == "__main__":
    s = service()
    s.Open()
    s.edit_person()
    s.Save()
