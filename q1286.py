"""
1286. Iterator for Combination
Medium
https://leetcode.com/problems/iterator-for-combination/
Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.


Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false


Constraints:

1 <= combinationLength <= characters.length <= 15
There will be at most 10^4 function calls per test.
It's guaranteed that all calls of the function next are valid.
Accepted
35,249
Submissions
49,782
"""

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.chs = characters
        self.comblen = combinationLength
        self.totlen = len(self.chs)
        self.idx = [_ for _ in range(self.comblen)]
        self.idx[-1] -= 1


    def next(self) -> str:
        k = self.comblen  # the digit where the calculation stop propagating
        while k > 0:
            k -= 1
            self.idx[k] += 1
            if self.idx[k] < self.totlen + k + 1 - self.comblen:
                break
        for i in range(k+1, self.comblen):
            self.idx[i] = self.idx[i-1] + 1

        return ''.join([self.chs[k] for k in self.idx])

    def hasNext(self) -> bool:
        return self.idx[0] != self.totlen - self.comblen


s = 'abc'
l = 2
x = CombinationIterator(s, l)
print(x.next())
print(x.hasNext())
print(x.next())
print(x.hasNext())
print(x.next())
print(x.hasNext())