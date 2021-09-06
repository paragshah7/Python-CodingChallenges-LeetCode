"""
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

"""

def group_anagrams(words):
    word_dict = {}

    for word in words:

        # sort each word and put in dict
        sorted_word = ''.join(sorted(word))

        # add new word to dict
        if sorted_word not in word_dict:
            word_dict[sorted_word] = [word]

        else:
            word_dict[sorted_word].append(word)

    return list(word_dict.values())


strs = ["eat","tea","tan","ate","nat","bat"]
# strs = ["a"]
# strs = [""]
print(group_anagrams(strs))
