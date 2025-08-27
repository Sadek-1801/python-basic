# import random

# for i in range(100):
#   if random.randint(0, 1) == 0:
#     print('H', end=' ')
#   else:
#     print('T', end=' ')
# print()

def a():
  print('a() starts')
  b()
  d()
  print('a() returns')

def b():
  print('b() starts')
  c()
  print('b() returns')

def c():
  print('c() starts')
  print('c() returns')

def d():
  print('d() starts')
  print('d() returns')

# a()

def spam():
  eggs = 'SPAMSPAM'
  bacon()
  print(eggs)

def bacon():
  ham = 'hamham'
  eggs = 'BACONBACON'
  print(eggs)


spam()
