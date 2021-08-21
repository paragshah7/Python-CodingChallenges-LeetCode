"""
https://www.interviewcake.com/question/python3/inflight-entertainment?course=fc1&section=hashing-and-hash-tables
Write a function that takes an integer flight_length (in minutes) and a list of integers movie_lengths (in minutes) and
returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.

Basically Two-sum
"""
# What if we wanted to fill the flight length as nicely as possible with any number of movies (not just 2)?

from icecream import ic as print

# Brute force
# def can_two_movies_fill_flight(movie_lengths: list, flight_length: int):
#     for index, movie1 in enumerate(movie_lengths):
#         for movie2 in movie_lengths[index+1:]:
#             if movie1 + movie2 == flight_length:
#                 print(movie1, movie2)
#                 return True
#     return False

# Using dict
def can_two_movies_fill_flight(movie_lengths: list, flight_length: int):

    # Convert list to dict
    movie_dict = {}
    for movie in movie_lengths:
        if movie not in movie_dict:
            movie_dict[movie] = 1
    print(movie_dict)

    # Look up the difference since it O(1)
    for movie in movie_dict:
        rem_movie = flight_length - movie
        if rem_movie in movie_dict:
            return True
    return False


print(can_two_movies_fill_flight([1, 1, 3, 6, 9], 8))
print(can_two_movies_fill_flight([1, 1, 3, 5, 9], 6))
