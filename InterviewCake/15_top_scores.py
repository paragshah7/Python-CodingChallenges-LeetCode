"""
https://www.interviewcake.com/question/python3/top-scores?course=fc1&section=sorting-searching-logarithms
Write a function that takes:

a list of unsorted_scores
the highest_possible_score in the game
and returns a sorted list of scores in less than O(n\lg{n})O(nlgn) time.

For example:

  unsorted_scores = [37, 89, 41, 65, 91, 53]
HIGHEST_POSSIBLE_SCORE = 100

# Returns [91, 89, 65, 53, 41, 37]
sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)
"""
from icecream import ic as print

def top_scores(unsorted_scores, highest_possible_score):
    #
    # A map of all numbers
    score_counts = {}

    # Populate score_counts
    for score in unsorted_scores:
        score_counts[score] = 1

    print(score_counts)

    sorted_scores = []
    count = 0

    min = unsorted_scores[0]
    max = unsorted_scores[0]
    for i in unsorted_scores[1:]:
        if i > max:
            max = i
        if i < min:
            min = i

    print(max)

    # For each item in score_counts
    for score in range(min, max+1):
        try:
            if score_counts[score]:
                sorted_scores.append(score)
        except:
            continue


    print(sorted_scores)


unsorted_scores = [-37, 89, -41, 65, 91, 53]
HIGHEST_POSSIBLE_SCORE = 100
top_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)
