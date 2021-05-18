from classes.ConsoleTable import ConsoleTable
import sort_data_list_by_mass_flow as sort_data


def print_table(res_data_list):
    res_data_list = sort_data.sort_res_data_by_mass_flow(res_data_list)
    table_start_list = [2, 25, 15]
    start_row = ["№", "Величина", "Ед. изм."]
    for curr_data in res_data_list:
        table_start_list.append(25)
        start_row.append("start_mass_flow = " + str(round(curr_data.ed.sec[0].m, 3)))
    table = ConsoleTable(3 + len(res_data_list), table_start_list)
    table.add_row(start_row)
    table.add_row([1, "Phi", "-"] + [i.Phi for i in res_data_list])
    table.add_row([2, "psi_T", "-"] + [i.psi_T for i in res_data_list])
    table.add_row([3, "n_impeller", "-"] + [i.n_impeller for i in res_data_list])
    table.add_row([4, "hp_impeller", "Дж/кг"] + [i.hp_impeller for i in res_data_list])
    table.add_row([5, "hd_impeller", "Дж/кг"] + [i.hd_impeller for i in res_data_list])
    table.add_row([6, "hi_impeller", "Дж/кг"] + [i.hi_impeller for i in res_data_list])
    table.add_row([7, "eta_p_impeller", "-"] + [i.eta_p_impeller for i in res_data_list])
    table.add_row([8, "eta_p_f_impeller", "-"] + [i.eta_p_f_impeller for i in res_data_list])
    table.add_row([9, "ratio_P_impeller", "-"] + [i.ratio_P_impeller for i in res_data_list])
    table.add_row([10, "ratio_P_f_impeller", "-"] + [i.ratio_P_f_impeller for i in res_data_list])
    table.add_row([11, "psi_i_impeller", "-"] + [i.psi_i_impeller for i in res_data_list])
    table.add_row([12, "n_stage", "-"] + [i.n_stage for i in res_data_list])
    table.add_row([13, "hp_stage", "Дж/кг"] + [i.hp_stage for i in res_data_list])
    table.add_row([14, "hd_stage", "Дж/кг"] + [i.hd_stage for i in res_data_list])
    table.add_row([15, "hi_stage", "Дж/кг"] + [i.hi_stage for i in res_data_list])
    table.add_row([16, "eta_p_stage", "-"] + [i.eta_p_stage for i in res_data_list])
    table.add_row([17, "eta_p_f_stage", "-"] + [i.eta_p_f_stage for i in res_data_list])
    table.add_row([18, "ratio_P_stage", "-"] + [i.ratio_P_stage for i in res_data_list])
    table.add_row([19, "ratio_P_f_stage", "-"] + [i.ratio_P_f_stage for i in res_data_list])
    table.add_row([20, "psi_i_stage", "-"] + [i.psi_i_stage for i in res_data_list])
    return table.get_write_data()


def save_data_in_file(file_path, data_list):
    data_write = print_table(data_list)
    if (file_path[-4:] == ".txt") and (len(file_path) > 5):
        with open(file_path, "w+", encoding='utf-8') as file_write:
            file_write.write(data_write)
        file_write.close()
    else:
        file_path += ".txt"
        with open(file_path, "w+", encoding='utf-8') as file_write:
            file_write.write(data_write)
        file_write.close()
