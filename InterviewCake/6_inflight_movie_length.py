"""
https://www.interviewcake.com/question/python3/inflight-entertainment?course=fc1&section=hashing-and-hash-tables
Write a function that takes an integer flight_length (in minutes) and a list of integers movie_lengths (in minutes) and
returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.
"""

# What if we wanted to fill the flight length as nicely as possible with any number of movies (not just 2)?

# def can_two_movies_fill_flight(movie_lengths, flight_length):
# def can_two_movies_fill_flight(movie_lengths, flight_length):
# #
# #     # Movie lengths we've seen so far
# #     movie_lengths_seen = set()
# #     movie_lengths.sort()
# #     remaining = flight_length
# #
# #     for movie in movie_lengths:
# #         remaining = remaining - movie
# #         print(movie, remaining)
# #         if remaining < 0:
# #             if -remaining in movie_lengths_seen:
# #                 return True
# #             else:
# #                 remaining = flight_length
# #         movie_lengths_seen.add(movie)
# #
# #     return False
#     # Movie lengths we've seen so far
#     movie_lengths_seen = set()
#     movie_lengths.sort()
#     remaining = flight_length
#
#     for movie in movie_lengths:
#         remaining = remaining - movie
#         print(movie, remaining)
#         if remaining < 0:
#             if -remaining in movie_lengths_seen:
#                 return True
#             else:
#                 remaining = flight_length
#         movie_lengths_seen.add(movie)
#
#     return False
from icecream import ic as print

def can_two_movies_fill_flight(movie_lengths: list, flight_length: int):
    for index, movie1 in enumerate(movie_lengths):
        for movie2 in movie_lengths[index+1:]:
            if movie1 + movie2 == flight_length:
                print(movie1, movie2)
                return True
    return False


print(can_two_movies_fill_flight([1, 1, 3, 5, 9], 8))
print(can_two_movies_fill_flight([1, 1, 3, 5, 9], 6))

