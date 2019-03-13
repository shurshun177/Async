# class Bank:
#     crisis = False
#     def create_atm(self):
#         while not self.crisis:
#             yield '$100'
#
# hsbc = Bank()
# corner_street_atm = hsbc.create_atm()
#
# wall_street_atm = hsbc.create_atm()
# print(wall_street_atm.__next__())
# print(corner_street_atm.__next__())

def makeRange(n):
    i = 0
    while i < n:
        yield i # custom range function
        i += 0.5

x = makeRange(5)
print(list(x)) # just one time
print(list(x)) # returns empty list

def func(an_iterable):  # equvalent: def func(an_iterable):
                        #                   for item in an_iterable:
    yield from an_iterable  #                       yield item

def bank_account(deposited, interest_rate):
    while True:
        calculated_interest = interest_rate * deposited
        received = yield calculated_interest
        print(received)
        if received:
            print('Received: {}'. format(received))
            deposited += received

def coroutine():
    i = -1
    while True:
        i += 1
        val = yield i
        print('Received {}'.format(val))

def fib(l=10):
    a, b = 0, 1
    for i in range(l):
        yield b # it`s right
        a, b = b, a + b

def fib2(l=10):
    a, b = 0, 1
    for i in range(l):
        yield a # not right

        a, b = b, a + b

print(3/2, 3//2, sep='\n')