def merge_lists(my_list, alices_list):
    merged_list = []
    i = j = 0
    current_index = 0
    while current_index < len(my_list) + len(alices_list):
        if i == len(my_list):
            merged_list.append(alices_list[j])
            break
        elif j == len(alices_list):
            merged_list.append(my_list[i])
            break
        elif my_list[i] < alices_list[j]:
            merged_list.append(my_list[i])
            i += 1
        else:
            merged_list.append(alices_list[j])
            j += 1
        current_index += 1

        print(merged_list)

    return merged_list


my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]
print(merge_lists(my_list, alices_list))