def main_print_triangle(n):
    list1 = ['*']*n
    list2 = [' ']*(n-1)
    first_list = merge_lists_elementwise(list1, list2)

    for i in range(n):
        if i == 0:
            print(''.join(first_list))
        elif (i%2) == 1:
            curr_odd_list = change_list_in_odd_step(first_list, i)
            print(curr_odd_list)
        else:
            curr_even_list = change_list_in_even_step(first_list, i)
            print(curr_even_list)


def merge_lists_elementwise(list1, list2):
    list_result = [list1[0]]
    for i in range(len(list1)-1):
        list_result += [list2[i], list1[i+1]]
    return list_result


def replace_stars_and_spaces(curr_list):
    curr_string = ''.join(curr_list)
    tmp_string1 = curr_string.replace('*', 'a')
    tmp_string2 = tmp_string1.replace(' ', '*')
    result = tmp_string2.replace('a', ' ')
    return list(result)


def change_list_in_odd_step(curr_list, step):
    result = replace_stars_and_spaces(curr_list[step:-step])
    return ''.join([' ']*step + result + [' ']*step)


def change_list_in_even_step(last_even_list, step):
    list_result = [' ']*step + last_even_list[step:-step] + [' ']*step
    return ''.join(list_result)


main_print_triangle(10)
