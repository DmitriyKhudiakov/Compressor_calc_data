from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QPushButton, QFileDialog, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QTextEdit
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
import read_import_data as rid
import write_result_data as wrd
import show_data as shd
import check_setup_data as csd
from classes.ResMassFlowData import ResMassFlowData
import pathlib


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        # initialize
        self.main_horizontal_layout = QHBoxLayout()
        self.main_vertical_layout = QVBoxLayout()
        self.add_desc_box = QGroupBox()
        self.add_group_box = QGroupBox()
        self.add_group_box_vertical_layout = QVBoxLayout()
        self.get_group_box = QGroupBox()
        self.get_group_box_vertical_layout = QVBoxLayout()
        self.import_group_box = QGroupBox()
        self.import_group_box_vertical_layout = QVBoxLayout()
        self.import_add_btn = QPushButton("Add table")
        self.import_delete_btn = QPushButton("Delete table")
        self.import_btn_horizontal_layout = QHBoxLayout()
        self.import_table = QTableWidget()
        self.import_table_select_cell = None
        self.calc_group_box = QGroupBox()
        self.calc_group_box_vertical_layout = QVBoxLayout()
        self.calc_group_box_horizontal_layout_list = []
        self.calc_group_label_var_list = []
        self.calc_group_label_lim_list = []
        self.calc_group_label_line_edit_list = []
        self.calc_group_label_error_list = []
        self.calc_group_box_horizontal_layout = QHBoxLayout()
        self.calc_label = QLabel("No data to calc")
        self.calc_btn = QPushButton("Calc results")
        dir_path = str(pathlib.Path().absolute()) + "\\source\\images\\"
        self.w_list = [[dir_path + "u.png", "[м/с] lim(0...500)", "", None, 0.0, 500.0],
                       [dir_path + "d2.png", "[м] lim(0...5)", "", None, 0.0, 5.0],
                       [dir_path + "r.png", "[Дж/(кг*К)] lim(50...500)", "", None, 50.0, 500.0],
                       [dir_path + "c_p.png", "[Дж/(кг*К)] lim(900...1100)", "", None, 900.0, 1100.0]]
        self.proc_group_box = QGroupBox()
        self.proc_group_box_vertical_layout = QVBoxLayout()
        self.proc_group_box_horizontal_layout_1 = QHBoxLayout()
        self.proc_group_box_horizontal_layout_2 = QHBoxLayout()
        self.proc_group_box_horizontal_layout_3 = QHBoxLayout()
        self.proc_group_box_label_1 = QLabel("There are not result data")
        self.proc_group_box_label_2 = QLabel("There are not result data to save")
        self.proc_group_box_label_3 = QLabel("There are not result data to show")
        self.proc_group_box_save_btn = QPushButton("Save")
        self.proc_group_box_show_btn = QPushButton("Show")
        self.there_are_ready_data = False
        self.is_all_data_ready = True
        self.enter_data_list = []
        self.res_data_list = []
        self.res_data_is_ready = False
        self.set_ui()

    def set_ui(self):
        self.setWindowTitle("Centrifugal compressor stage data calc")
        self.move(100, 100)
        self.set_desc_boc()
        self.set_add_group_box()
        self.set_get_group_box()
        self.set_import_group_box()
        self.set_calc_group_box()
        self.set_proc_group_box()
        self.add_group_box_vertical_layout.addWidget(self.import_group_box)
        self.add_group_box.setLayout(self.add_group_box_vertical_layout)
        self.get_group_box_vertical_layout.addWidget(self.calc_group_box)
        self.get_group_box_vertical_layout.addWidget(self.proc_group_box)
        self.get_group_box.setLayout(self.get_group_box_vertical_layout)
        self.main_vertical_layout.addWidget(self.add_group_box)
        self.main_vertical_layout.addWidget(self.get_group_box)
        self.setMaximumWidth(2000)
        self.main_horizontal_layout.addLayout(self.main_vertical_layout)
        self.main_horizontal_layout.addWidget(self.add_desc_box)
        self.setLayout(self.main_horizontal_layout)
        self.show()

    def set_desc_boc(self):
        self.add_desc_box.setTitle("Description")
        self.add_desc_box.setMinimumWidth(800)
        te = QTextEdit()
        file_is_open = True
        file_path = str(pathlib.Path().absolute()) + "\\source\\description.html"
        try:
            file = open(file_path, "r", encoding="utf-8")
        except OSError:
            file_is_open = False
        if file_is_open is True:
            te.setReadOnly(True)
            te.setStyleSheet("background-color: #F0F0F0")
            te.setHtml(str(file.read()))
            te.toHtml()
            horizontal_layout = QHBoxLayout()
            horizontal_layout.addWidget(te)
            self.add_desc_box.setLayout(horizontal_layout)

    def set_add_group_box(self):
        self.add_group_box.setTitle("Add data")
        self.add_group_box.setMaximumHeight(400)

    def set_get_group_box(self):
        self.get_group_box.setTitle("Get data")
        self.get_group_box.setMaximumHeight(400)

    def set_import_group_box(self):
        self.import_group_box.setTitle("Import data")
        self.import_table.setFixedSize(700, 300)

        self.import_table.setColumnCount(2)
        self.import_table.setRowCount(1)
        self.import_table.setStyleSheet("background-color: #F0F0F0")
        self.import_table.horizontalHeader().hide()
        self.import_table.verticalHeader().hide()
        self.import_table.setItem(0, 1, QTableWidgetItem())
        self.import_table.setItem(0, 0, QTableWidgetItem())
        self.import_table.setColumnWidth(0, 700)
        self.import_table.setColumnWidth(1, 100)
        self.import_table.setItem(0, 0, QTableWidgetItem("Imported file name"))
        self.import_table.setItem(0, 1, QTableWidgetItem("Data valid"))
        self.import_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.import_table.setFixedWidth(802)
        self.import_add_btn.setFixedSize(QSize(100, 30))
        self.import_add_btn.clicked.connect(self.import_add_btn_clicked)
        self.import_delete_btn.setFixedSize(QSize(100, 30))
        self.import_delete_btn.clicked.connect(self.import_delete_btn_clicked)
        self.import_btn_horizontal_layout.addStretch(1)
        self.import_btn_horizontal_layout.addWidget(self.import_add_btn)
        self.import_btn_horizontal_layout.addWidget(self.import_delete_btn)
        self.import_group_box_vertical_layout.addWidget(self.import_table)
        self.import_group_box_vertical_layout.addLayout(self.import_btn_horizontal_layout)
        self.import_group_box.setLayout(self.import_group_box_vertical_layout)

    def set_calc_group_box(self):
        self.calc_group_box.setTitle("Calc data")
        self.calc_group_box.setFixedHeight(200)
        for i in range(4):
            self.calc_group_box_horizontal_layout_list.append(QHBoxLayout())
            self.calc_group_label_var_list.append(QLabel())
            h_pix_map = QPixmap(self.w_list[i][0])
            self.calc_group_label_var_list[-1].setPixmap(h_pix_map)
            self.calc_group_label_var_list[-1].setFixedWidth(50)
            self.calc_group_label_lim_list.append(QLabel(self.w_list[i][1]))
            self.calc_group_label_lim_list[-1].setFixedWidth(150)
            self.calc_group_label_line_edit_list.append(QLineEdit())
            self.calc_group_label_line_edit_list[-1].setFixedWidth(150)
            self.calc_group_label_error_list.append(QLabel(""))
            self.calc_group_box_horizontal_layout_list[-1].addWidget(self.calc_group_label_var_list[-1])
            self.calc_group_box_horizontal_layout_list[-1].addWidget(self.calc_group_label_lim_list[-1])
            self.calc_group_box_horizontal_layout_list[-1].addWidget(self.calc_group_label_line_edit_list[-1])
            self.calc_group_box_horizontal_layout_list[-1].addWidget(self.calc_group_label_error_list[-1])
            self.calc_group_box_vertical_layout.addLayout(self.calc_group_box_horizontal_layout_list[-1])
        self.calc_btn.setFixedSize(QSize(100, 30))
        self.calc_btn.clicked.connect(self.calc_btn_clicked)
        self.calc_group_box_horizontal_layout.addWidget(self.calc_label)
        self.calc_group_box_horizontal_layout.addWidget(self.calc_btn)
        self.calc_group_box_vertical_layout.addLayout(self.calc_group_box_horizontal_layout)
        self.calc_group_box.setLayout(self.calc_group_box_vertical_layout)

    def set_proc_group_box(self):
        self.proc_group_box.setTitle("Proc data")
        self.proc_group_box_save_btn.setFixedSize(QSize(100, 30))
        self.proc_group_box_save_btn.clicked.connect(self.proc_group_box_save_btn_clicked)
        self.proc_group_box_show_btn.setFixedSize(QSize(100, 30))
        self.proc_group_box_show_btn.clicked.connect(self.proc_group_box_show_btn_clicked)
        self.proc_group_box_horizontal_layout_1.addWidget(self.proc_group_box_label_1)
        self.proc_group_box_horizontal_layout_2.addWidget(self.proc_group_box_label_2)
        self.proc_group_box_horizontal_layout_2.addWidget(self.proc_group_box_save_btn)
        self.proc_group_box_horizontal_layout_3.addWidget(self.proc_group_box_label_3)
        self.proc_group_box_horizontal_layout_3.addWidget(self.proc_group_box_show_btn)
        self.proc_group_box_vertical_layout.addLayout(self.proc_group_box_horizontal_layout_1)
        self.proc_group_box_vertical_layout.addLayout(self.proc_group_box_horizontal_layout_2)
        self.proc_group_box_vertical_layout.addLayout(self.proc_group_box_horizontal_layout_3)
        self.proc_group_box.setLayout(self.proc_group_box_vertical_layout)

    def update_calc_label(self):
        for row in range(1, self.import_table.rowCount()):
            if self.import_table.item(row, 1).text() == "Error":
                self.is_all_data_ready = False
            else:
                self.there_are_ready_data = True
        if (self.is_all_data_ready is True) and (self.there_are_ready_data is True):
            self.calc_label.setText("Data is ready to calc")
        elif self.there_are_ready_data is False:
            self.calc_label.setText("No data to calc")
        else:
            self.calc_label.setText("Some data has an error")

    def import_add_btn_clicked(self):
        full_path = QFileDialog.getOpenFileName(self, "Open file", "")[0]
        is_valid, enter_data = rid.read_data(full_path, "mass_flow_data")
        self.import_table.insertRow(1)
        self.import_table.setItem(2, -2, QTableWidgetItem(full_path))
        if is_valid is True:
            self.import_table.setItem(2, -1, QTableWidgetItem("Data is valid"))
        else:
            self.import_table.setItem(2, -1, QTableWidgetItem("Error"))
        self.there_are_ready_data = False
        self.is_all_data_ready = True
        self.update_calc_label()
        self.enter_data_list.append(enter_data)

    def import_delete_btn_clicked(self):
        self.import_table.removeRow(1)
        self.there_are_ready_data = False
        self.is_all_data_ready = True
        self.update_calc_label()
        self.enter_data_list = self.enter_data_list[:-1]

    def calc_btn_clicked(self):
        if (self.is_all_data_ready is True) and (self.there_are_ready_data is True):
            self.res_data_list = []
            for ed in self.enter_data_list:
                enter_list = []
                for curr_line_edit in self.calc_group_label_line_edit_list:
                    enter_list.append(curr_line_edit.text())
                ret_list, is_ok, val_list = csd.set_vars(self.w_list, enter_list)
                for curr_lbl, mes in zip(self.calc_group_label_error_list, ret_list):
                    curr_lbl.setText(mes)
                if is_ok is True:
                    self.res_data_list.append(ResMassFlowData(ed, val_list[0], val_list[1], val_list[2], val_list[3]))
                    if self.res_data_list[-1].calc_parameters() is True:
                        self.res_data_is_ready = True
                        self.proc_group_box_label_1.setText("Result data is calculated")
                        self.proc_group_box_label_2.setText("Result data is ready to save")
                        self.proc_group_box_label_3.setText("Result data is ready to show")
                    else:
                        self.res_data_is_ready = False
                        self.proc_group_box_label_1.setText("Error in calculating results")
                        self.proc_group_box_label_2.setText("Result data is NOT ready to save")
                        self.proc_group_box_label_3.setText("Result data is NOT ready to show")

    def proc_group_box_save_btn_clicked(self):
        if self.res_data_is_ready is True:
            name = QFileDialog.getSaveFileName(self, "Save", "/", ".txt")[0]
            wrd.save_data_in_file(name, self.res_data_list)

    def proc_group_box_show_btn_clicked(self):
        if self.res_data_is_ready is True:
            shd.plot(self.res_data_list)
