# This Python file uses the following encoding: windows-1251

import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from util import read_text
import My_ElGamal as elg

def get_task_val():
    v_tsk_p = elg.get_prime_number_in_range(10, 100)
    v_tsk_g = elg.get_primitive_root(v_tsk_p)
    v_tsk_x = elg.get_prime_number_in_range(1, v_tsk_p - 1)
    v_tsk_m = elg.get_random_message(6)
    return v_tsk_p,v_tsk_g,v_tsk_x,v_tsk_m

class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('��� �� ����� ���-������: �������� �������')
        self.setFixedSize(700,800)

        main_layout = QGridLayout(self)
        self.setLayout(main_layout)

        # create a tab widget
        tab = QTabWidget(self)
        tab.setFont(QFont('Arial', 12))
        # Page Theory
        page_text = QWidget(self)
        layout = QFormLayout()
        page_text.setLayout(layout)
        text = read_text('text_mod1_block1.html')
        label_text = QLabel(text)
        label_text.setFont(QFont('Arial', 12))
        label_text.setWordWrap(True)
        scrollArea = QScrollArea()
        scrollArea.setWidget(label_text)
        layout.addRow(scrollArea)
        # Page Example
        page_example = QWidget(self)
        layout_ex = QFormLayout()
        page_example.setLayout(layout_ex)
        layout_ex.addRow(QLabel('�������� ��� �� ����� ���-������'))
        layout_ex.addRow(QLabel('����� ��������:'))
        self.inp_ex_m = QLineEdit()
        self.inp_ex_p = QLineEdit()
        self.inp_ex_g = QLineEdit()
        self.inp_ex_x = QLineEdit()
        btn_ex = QPushButton("������")
        btn_ex.clicked.connect(self.click_btn_ex)
        self.outp_ex = QTextBrowser()
        self.inp_ex_m.setFixedSize(620,20)
        self.inp_ex_p.setFixedSize(620,20)
        self.inp_ex_g.setFixedSize(620,20)
        self.inp_ex_x.setFixedSize(620,20)
        layout_ex.addRow(QLabel('m = '), self.inp_ex_m)
        layout_ex.addRow(QLabel('p = '), self.inp_ex_p)
        layout_ex.addRow(QLabel('g = '), self.inp_ex_g)
        layout_ex.addRow(QLabel('x = '), self.inp_ex_x)
        layout_ex.addRow(btn_ex)
        layout_ex.addRow(QLabel('�����:'))
        layout_ex.addRow(self.outp_ex)
        # Page Task
        page_task = QWidget(self)
        layout_tsk = QFormLayout()
        page_task.setLayout(layout_tsk)
        layout_tsk.addRow(QLabel('�������� ��� ���-������ �� �������� ����������'))
        self.v_tsk_p,self.v_tsk_g,self.v_tsk_x,self.v_tsk_m = get_task_val()
        self.task_text = QLabel(f'��������� �� ������� ���������� ���: \np = {self.v_tsk_p}, g = {self.v_tsk_g}, x = {self.v_tsk_x}, m = {self.v_tsk_m}')
        self.tsk_r = QLineEdit()
        self.tsk_s = QLineEdit()
        btn_tsk_chk = QPushButton("���������")
        btn_tsk_rst = QPushButton("��������")
        self.outp_tsk = QTextBrowser()
        btn_tsk_chk.clicked.connect(self.click_btn_tsk_chk)
        btn_tsk_rst.clicked.connect(self.click_btn_tsk_rst)
        self.tsk_r.setFixedSize(620,20)
        self.tsk_s.setFixedSize(620,20)
        layout_tsk.addRow(self.task_text)
        layout_tsk.addRow(QLabel('����� ��������:'))
        layout_tsk.addRow(QLabel('r = '), self.tsk_r)
        layout_tsk.addRow(QLabel('s = '), self.tsk_s)
        layout_tsk.addRow(btn_tsk_chk)
        layout_tsk.addRow(btn_tsk_rst)
        layout_tsk.addRow(QLabel('�����:'))
        layout_tsk.addRow(self.outp_tsk)

        # add pane to the tab widget
        tab.addTab(page_text, '������')
        tab.addTab(page_example, '�������')
        tab.addTab(page_task, '������')
        
        main_layout.addWidget(tab, 0, 0, 2, 1)

        self.show()

    def click_btn_ex(self):
        try:
            v_exmpl_m = str(self.inp_ex_m.text())
            v_exmpl_p = int(self.inp_ex_p.text())
            v_exmpl_g = int(self.inp_ex_g.text())
            v_exmpl_x = int(self.inp_ex_x.text())
            self.outp_ex.setText(elg.ds_ElGamal_outp(v_exmpl_m, v_exmpl_p, v_exmpl_g, v_exmpl_x))
        except ValueError:
            self.outp_ex.setText(f"����� ��������: \nm - ������ \np, g, x - ����� ����a")
    
    def click_btn_tsk_chk(self):
        try:
            v_tsk_r = int(self.tsk_r.text())
            v_tsk_s = int(self.tsk_s.text())
            v_r, v_s = elg.ds_ElGamal(self.v_tsk_m, self.v_tsk_p, self.v_tsk_g, self.v_tsk_x)
            if (v_tsk_r == v_r and v_tsk_s == v_s):
                self.outp_tsk.setText(f"r = {v_tsk_r}\ns = {v_tsk_s}\n�����")
            else:
                self.outp_tsk.setText(f"r = {v_tsk_r}\ns = {v_tsk_s}\n�������")
            self.update()
        except ValueError:
            self.outp_tsk.setText(f"����� ��������: \nr - ����� ����� \ns - ����� �����")

    def click_btn_tsk_rst(self):
        try:
            self.v_tsk_p,self.v_tsk_g,self.v_tsk_x,self.v_tsk_m = get_task_val()
            self.task_text.setText(f'��������� �� ������� ���������� ���: \np = {self.v_tsk_p}, g = {self.v_tsk_g}, x = {self.v_tsk_x}, m = {self.v_tsk_m}')
            self.update()
        except ValueError:
            print(ValueError)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())