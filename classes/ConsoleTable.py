

class ConsoleTable:
    def __init__(self, n_col, col_width_list):
        self.n_col = n_col
        self.col_width_list = col_width_list
        self.rows_data_list = []

    def add_row(self, val_list):
        self.rows_data_list.append(val_list)

    @staticmethod
    def add_space_to_len(change_str, width):
        if len(change_str) >= width:
            return change_str
        else:
            while len(change_str) < width:
                change_str += " "
            return change_str

    def get_write_data(self):
        write_data = ""
        for curr_row in self.rows_data_list:
            print_str = ""
            for curr_cell, curr_width in zip(curr_row, self.col_width_list):
                print_str += "|" + self.add_space_to_len(str(curr_cell), curr_width)
            write_data += print_str + "|" + "\n"
        return write_data
