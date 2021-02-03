"""
Given a string s and a list of words representing a dictionary, return
whether or not the entirety of s can be segmented into dictionary words.

Note: You may assume that all the characters in s and the dictionary are
lowercase.

Ex: Given the following string s and dictionary...
s = "thedailybyte", dictionary = ["the", "daily", "byte"], return true.

Ex: Given the following string s and dictionary...
s = "pizzaplanet", dictionary = ["plane", "pizza"], return false.
"""

# Using a trie data structure should help here.
# But just using a trie wont solve all issues, for eg:
#   s = "planetpizza", dictionary = ["plane", "planet", "pizza"]
#
# Using a trie, if we just assume that "plane" is the corrent word and
# not check ahead for planet, it won't work as "tpizza" is not a word.
#
# To make this work, you need to keep checking ahead for the whole
# string, and check for a possible solution for every word length at
# which there is a match.

# TODO: incomplete
