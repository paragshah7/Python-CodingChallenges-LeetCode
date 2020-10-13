"""Write a function that takes an integer flight_length (in minutes)
and a list of integers movie_lengths (in minutes)
and returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.
"""

"""What if we wanted to fill the flight length as nicely as possible with any number of movies (not just 2)?"""

def can_two_movies_fill_flight(movie_lengths, flight_length):

    # Movie lengths we've seen so far
    movie_lengths_seen = set()
    movie_lengths.sort()
    remaining = flight_length

    for movie in movie_lengths:
        remaining = remaining - movie
        print(movie, remaining)
        if remaining < 0:
            if -remaining in movie_lengths_seen:
                return True
            else:
                remaining = flight_length
        movie_lengths_seen.add(movie)

    return False


print(can_two_movies_fill_flight([1, 1, 3, 5, 9], 8))
print(can_two_movies_fill_flight([1, 1, 3, 5, 9], 6))

