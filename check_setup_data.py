

def is_float(str_read):
    try:
        float(str_read)
        return True
    except ValueError:
        return False


def set_vars(setup_list, enter_list):
    value_list = []
    is_ok = True
    ret_list = []
    for s_l, e_l in zip(setup_list, enter_list):
        str_read = e_l
        is_right = is_float(str_read)
        if is_right is True:
            val = float(str_read)
            if (val >= s_l[4]) and (val <= s_l[5]):
                value_list.append(val)
                ret_list.append("ok")
            else:
                is_ok = False
                ret_list.append("Error: value is not in valid range")
        else:
            is_ok = False
            ret_list.append("Error: Invalid input format")
    return ret_list, is_ok, value_list
