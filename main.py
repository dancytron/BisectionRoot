# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# -*- coding: utf-8 -*-
"""

Function for estimating roots with bisection search from p. 68 of Introduction to Computation and Programming Using
Python. 3rd edition. by John V. Guttag.

Used to test GitHub push and practice using IDE.

"""
import time


def find_root(x, power, epsilon):
    # find interval containing answer
    if x < 0 and power % 2 == 0:
        return None  # negative number
    low = min(-1, x)
    high = max(1, x)
    # use bisection search
    ans = (high + low) / 2
    while abs(ans ** power - x) >= epsilon:
        if ans ** power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return ans


num = float(input(f' enter number to find root of:  '  ))
power_of = float(input(f'enter power:  '))
# noinspection SpellCheckingInspection
epsil = float(input(f'epsilon:  '))
start = time.time()
answer = find_root(num, power_of, epsil)
end = time.time()
print(answer)
print (f' time elapsed:  {end - start}')

# print (find_root(52, 5, .1))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
