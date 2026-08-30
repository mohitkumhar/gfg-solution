""" Linked List Node Structure
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

"""

class Solution:
    def primeList(self, head):

        def isPrime(num):
            if num < 2:
                return False

            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        def findNearestPrime(n):
            if n <= 1:
                return 2

            d = 0

            while True:
                if n - d >= 2 and isPrime(n - d):
                    return n - d
                if isPrime(n + d):
                    return n + d
                d += 1

        curr = head

        while curr:
            curr.data = findNearestPrime(curr.data)
            curr = curr.next

        return head
