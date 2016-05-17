#To do:
# - Implement 'current category' (related to next point)
# - List categories using self and expense_dict instead of list_categories
# - Implement pdf exportation (automatically per month?)

import datetime
import csv
import statistics

def instructions():
    print('Welcome to Tresxpense!\n'
          'Choose one of the following options:\n'
          'a - list expense categories\n'
          's - change current category (default groceries)\n'
          'd - enter a new expense and description\n'
          'f - category\'s statistics\n'
          # 'x - export category as pdf\n'
          'q - quit\n')

class expense_list(object):
    def __init__(self, name):
        self.name = name

    def new_expense(self):
        while True:
            try:
                return float(input('Enter the new expense:\n'))
            except ValueError:
                print('Please enter a number.')

    def expense_description(self):
        while True:
            try:
                return input('Expense description (optional): ')
            except:
                print('Not valid input!')

    def file_writer(self, list):
        with open(self.name, 'a') as file:
            for item in list:
                file.write('%s     ' % item)
            file.write('\n')

    def file_extender(self, date_time, expense, description):
        new_line = []
        new_line.extend((date_time, expense, description))
        return new_line

    def file_extractor(self):
        expenses = []
        with open(self.name, newline='') as file:
            reader = csv.reader(file, delimiter=' ')
            for row in reader:
                if row[6]:
                    expenses.append(float(row[6]))
                else:
                    continue
            return expenses

    def average_expense(self, data):
        return print('Average: %.2f' % (sum(data) / len(data)))

    def median_expense(self, data):
        return print('Median: %.2f' % (statistics.median(sorted(data))))

    def std_dev_expense(self, data):
        return print('Std. dev: %.2f' % (statistics.stdev(data)))

class food(expense_list):
    pass

class gas(expense_list):
    pass

class fun(expense_list):
    pass

class rent(expense_list):
    pass

class clothes(expense_list):
    pass

class car(expense_list):
    pass

def list_categories():
    categories = {'1': 'groceries', '2': 'gas', '3': 'for fun',
                  '4': 'rent and utilities', '5': 'clothes', '6': 'car'}
    for k, v in sorted(categories.items()):
        print(k, '-', v)

def change_category():
    expense_dict = {'1': food('groceries'), '2': gas('gas'), '3': fun('for fun'),
                    '4': rent('rent and utilities'), '5': clothes('clothes'), '6': car('car')}
    while True:
        choice = input('Switch to which category?\n')
        if choice in expense_dict:
            return expense_dict[choice]
        else:
            print('Not a valid category!')

def default_opts():
    opts = ('a', 's', 'd', 'f', 'x', 'q')
    return opts

def user_choice(options, message = 'What would you like to do?\n'):
    while True:
        choice = input(message)
        if choice in options:
            return choice
        else:
            print('That\'s not a valid option!')

def current_date_time():
    current = datetime.datetime.now()
    return current.strftime('%Y-%m-%d %H:%M')

def main_loop():
    category = food('groceries')
    while True:
        # print('Current category: ', category)
        opts = default_opts()
        choice = user_choice(opts)
        if choice == 'a':
            list_categories()
        elif choice == 's':
            category = change_category()
        elif choice == 'd':
            n = category.new_expense()
            d = category.expense_description()
            dt = current_date_time()
            category.file_writer(category.file_extender(dt, n, d))
        elif choice == 'f':
            category.average_expense(category.file_extractor())
            category.median_expense(category.file_extractor())
            category.std_dev_expense(category.file_extractor())
        elif choice == 'q':
            break

instructions()
main_loop()
print('bye!')