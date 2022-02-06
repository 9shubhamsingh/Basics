"""
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""


# Python3 program for the above approach
from collections import Counter


class Solution:
	def isanagram(self, s: str, t: str) -> bool:
		#third method
		return sorted(s) == sorted(t)

		"""
		#second method
		return Counter(s) == Counter(t)
		"""
		"""
		#first method
		if len(s) != len(t):
			return False

		countS, countT={},{}

		for i in range(len(s)):
			countS[s[i]] = 1 + countS.get(s[i],0)
			countT[t[i]] = 1 + countT.get(t[i],0)

		for c in countS:
			if countS[c] != countT.get(c,0):
				return False

		return True
		"""

if __name__ == '__main__':
	print(Solution().isanagram('ct','tac'))

