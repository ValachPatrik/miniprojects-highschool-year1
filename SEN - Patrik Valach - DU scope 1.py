owner = ''
balance = 0

def create_account (meno):
    global owner, balance
    owner = meno
    balance = 0
    return owner, balance

def deposit(income):
    global balance
    balance += income
    return balance

def withdrawal(outcome):
    global balance
    balance -= outcome
    print(locals())
    return balance

def print_balance():
    s = ''
    s = s + owner + ' ' + str(balance)
    if balance < 0:
        s += '!'
    return s

meno = input('Insert name: ')
print(create_account(meno))

income = int(input('how much to deposit: '))
print('current balance after deposit: ' + str(deposit(income)))

outcome = int(input('how much to withdrawal: '))
print('current balance after withdrawal: ' + str(withdrawal(outcome)))

print(print_balance())