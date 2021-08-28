import random


class BillSplitter:
    def __init__(self, n_of_friends):
        self.n_of_friends = n_of_friends
        self.friends_dictionary = {}
        self.total_bill = None
        self.lucky = None

    def friends_name(self):
        print("\nEnter the name of every friend (including you), "
              "each on a new line:")

        i = 0
        while i != self.n_of_friends:
            name = input()
            self.friends_dictionary[name] = 0

            i += 1

        self.total_invoice_value(i)
        self.who_is_lucky()

        print(f"\n{self.friends_dictionary}")

    def total_invoice_value(self, number_of_friends):
        self.total_bill = int(input("\nEnter the total bill value:\n"))
        cost_for_one = round(self.total_bill / number_of_friends, 2)

        for i in self.friends_dictionary:
            self.friends_dictionary[i] = round(cost_for_one, 2)

    def who_is_lucky(self):
        self.lucky = input('\nDo you want to use the "Who is lucky?" '
                           'feature? Write Yes/No:\n')

        if self.lucky == "Yes":
            name = random.choice(list(self.friends_dictionary.keys()))

            self.friends_dictionary[name] = 0

            for i in self.friends_dictionary:
                if i != name:
                    self.friends_dictionary[i] \
                        = round(self.total_bill
                                / (len(self.friends_dictionary) - 1), 2)

            print(f"\n{name} is the lucky one!")
        elif self.lucky == "No":
            for i in self.friends_dictionary:
                self.friends_dictionary[i] \
                    = round(self.total_bill
                            / len(self.friends_dictionary), 2)

            print("\nNo one is going to be lucky")


if __name__ == '__main__':
    number = int(input("Enter the number of friends "
                       "joining (including you):\n"))

    try:
        assert number > 0
    except Exception:
        print("\nNo one is joining for the party")
    else:
        person = BillSplitter(number)
        person.friends_name()
