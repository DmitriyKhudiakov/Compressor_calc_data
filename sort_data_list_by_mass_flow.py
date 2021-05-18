

def sort_res_data_by_mass_flow(res_data_list):
    sorted_list = []
    copy_res_data_list = res_data_list.copy()
    len_res_data_list = len(copy_res_data_list)
    while len(sorted_list) < len_res_data_list:
        min_m = 999999999.9
        min_n = 9999999999
        n_curr = -1
        for curr_data in copy_res_data_list:
            n_curr += 1
            if curr_data.ed.sec[0].m < min_m:
                min_m = curr_data.ed.sec[0].m
                min_n = n_curr
        sorted_list.append(copy_res_data_list[min_n])
        copy_res_data_list.pop(min_n)
    return sorted_list
