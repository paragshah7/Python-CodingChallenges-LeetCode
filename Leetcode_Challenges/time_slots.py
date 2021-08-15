"""
// We have a list of various types of tasks to perform.
// Task types are identified with an integral identifier: task of type 1, task of type 2, task of type 3, etc.
// Each task takes 1 time slot to execute, and once we have executed a task we need cooldown (parameter) time slots to
// recover before we can execute another task of the same type.
// However, we can execute tasks of other types in the meantime.
// The cooldown interval is the same for all task types.
// We do not reorder the tasks: always execute in order in which we received them on input.

// Given a list of input tasks to run, and the cooldown interval,
// output the minimum number of time slots required to run them.

// Examples

// Example 1
// Tasks: 1, 1, 2, 1
// Recovery interval (cooldown): 2
// Output: 7  (order is 1   1 2  1)
//                      1   1   1
// Example 2
// Tasks: 1, 2, 3, 1, 2, 3
// Recovery interval (cooldown): 3
// Output: 7  (order is 1 2 3  1 2 3)

// Example 3
// Tasks: 1, 2, 3, 4, 5, 6, 2, 4, 6, 1, 2, 4
// Recovery interval (cooldown): 6
// Output: 18  (1 2 3 4 5 6   2  4  6 1  2  4)


// iterate on the array
// push first element in the result array
// if next element is the same as the one before
//.  look at the cool down period, push 2 time units in the arr
"""

input_list = [1, 2, 3, 1, 2, 3]
# input_list = [1, 1, 2, 1]
# output = 1 0 0 1 2 0 1

total_time = 0
input_map = {}
cooldown_given = 3
# cooldown = cooldown_given + 1
cooldown = 3

for key, val in enumerate(input_list):
    if cooldown == 0:
        cooldown = cooldown_given

    if val not in input_map.keys():
        total_time += 1
        input_map[val] = cooldown
        cooldown -= 1

    else:
        # if cooldown == cooldown_given:
        #     total_time += 1
            total_time += input_map[val] + 1
            input_map[val] -= 1
            print('elif', val, total_time)
            cooldown -= 1


    # cooldown -= 1
    print('OP ->', 'time-', total_time, ' cooldown-', cooldown)

