from classes.EnterMassFlowData import EnterMassFlowData


def read_str_table(line, enter_data):
    line = line.replace(" ", "")
    list_var = line.split(",")
    list_float = []
    if len(list_var) > 10:
        print("More variables were read in the line than necessary (10) - ", list_var)
        return False
    elif len(list_var) < 10:
        print("Fewer variables were read in the line than necessary (10) - ", list_var)
        return False
    for curr_var in list_var:
        try:
            float(curr_var)
        except ValueError:
            print("This value cannot be converted to float - ", curr_var)
            return False
        list_float.append(float(curr_var))
    enter_data.add_section(list_float)


def check_number_of_lines(lines_list):
    new_list = []
    for curr_line in lines_list:
        if curr_line.isspace() is False:
            curr_line = curr_line.replace("\n", "")
            new_list.append(curr_line)
    if len(new_list) != 8:
        print("Incorrect number of nonblank lines in the input file - ", len(lines_list), " instead of 8")
        return False, None
    else:
        return True, new_list


def read_data(full_file_path, data_name):
    if ((full_file_path[-3:] == "txt") or (full_file_path[-3:] == "csv")) is False:
        print("Wrong file format (need txt or csv)")
        return False, None
    try:
        file = open(full_file_path, "r")
    except OSError:
        print("Could not open/read file:", full_file_path)
        return False, None
    lines_list = file.readlines()
    is_num_str_valid, lines_list = check_number_of_lines(lines_list)
    if is_num_str_valid is False:
        return False, None
    enter_data = EnterMassFlowData(data_name)
    for curr_line in lines_list:
        if read_str_table(curr_line, enter_data) is False:
            return False, None
    return True, enter_data
