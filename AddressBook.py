from Week3.AddressBook.Service import service


class AddressBook:
    def __init__(self):

        self.obj = service()

    def address_book(self):
        try:
            while True:
                print("**************************************************")
                print("1.Create\n2.Open\n3.Save\n4.Add Person\n5.Delete Person\n6.Edit Person\n7.Quit")

                choice_selected = int(input("Select any choice : "))
                if choice_selected == 7:
                    self.obj.Save()
                    print("Exited")
                    return
                elif choice_selected > 7:
                    print("You have selected wrong choice.")
                    continue
                choice = {1: "Create", 2: "Open", 3: "Save",
                          4: "AddPerson", 5: "delete_person", 64: "edit_person"}
                fun = getattr(self.obj, choice[choice_selected])
                fun()
        except ValueError:
            print("You have enter wrong input.")
            self.address_book()


# Main method
if __name__ == "__main__":

    obj = AddressBook()
    obj.address_book()
