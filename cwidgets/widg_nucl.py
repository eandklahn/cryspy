# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 09:52:24 2019

Создает окно, которое используется в главной программе как виджит.

Для общности определные три класса:

    компоновщик (формирует локальное главное окно, если только этот файл запускается)
    модель (для передачи данных представителю и изменения данных при сигнале от представителя)
    представление (дает представление от модели)

@author: ikibalin
"""

import sys

from PyQt5 import QtWidgets
#from PyQt5 import QtGui
#from PyQt5 import QtCore

import widg_min
import cmodel 





class cbuilder(widg_min.cbuilder_min):
    def __init__(self, model):
        super(cbuilder, self).__init__(model)
    def init_widget(self, model):
        widg_central = cwidget(model)
        self.setCentralWidget(widg_central)


class cwidget(widg_min.cwidget_min):
    def __init__(self, model):
        super(cwidget, self).__init__(model)

    def init_widget(self, model):
        """
        make central layout
        """
        super(cwidget, self).init_widget(model)
        lay_central = self.layout_central
        
        q_label = QtWidgets.QLabel("""
The position of atom and its isotropical displacement is shown in the table
press buttons to add and to delete atoms. 

The handbooks values of scattering amplitude for given atoms can be loaded by 
pressing button 'load bscat'.""")
        lay_central.addWidget(q_label)

        lay_h = QtWidgets.QHBoxLayout()
        b_add = QtWidgets.QPushButton("add atom")
        b_add.clicked.connect(model.add_at)
        lay_h.addWidget(b_add)

        b_del = QtWidgets.QPushButton("delete atom")
        b_del.clicked.connect(lambda: self.del_at(model))
        lay_h.addWidget(b_del)

        b_bscat = QtWidgets.QPushButton("load bscat")
        b_bscat.clicked.connect(model.load_bscat)
        lay_h.addWidget(b_bscat)
        lay_h.addStretch(1)

        lay_central.addLayout(lay_h)
        llab_m = ['name', 'type_n', 'coordx', 'coordy', 'coordz', "biso", "occ"]
        lval_type= ['text', 'text', 'val', 'val', 'val', "val", "val"]
        lab_o = "t_nucl"
        lheader = ['name', 'type_n', 'x', 'y', 'z', "biso", "occ"]
        
        self.put_tab(lay_central, lab_o, model.atom, llab_m, lval_type, lheader)
        model.add_builder(self)
        
    def del_at(self, model):
        """
        delete the atom
        """
        text, ok = self.dialog_ask("Which atoms should be deleted \n(example: 1-3, 5, 7 or all)")
        n_r = self.t_nucl.rowCount()
        lnumb = []
        if text.strip() == "all":
            lnumb = range(n_r)
        else:
            lhelp = text.split(",")
            for srange in lhelp:
                if srange.strip().isdigit():
                    lnumb.append(int(srange)-1)
                else:
                    lhelp2 = srange.split("-")
                    if len(lhelp2) !=2:
                        pass
                    elif all([lhelp2[0].strip().isdigit(), lhelp2[1].strip().isdigit()]):
                        n1, n2 = int(lhelp2[0]), int(lhelp2[1])
                        lnumb.extend(range(n1-1,n2))
        lnumb = [numb for numb in lnumb if numb < n_r]
        
        lat = [model.atom[numb] for numb in lnumb]
        model.del_at(lat)
        
        
        
        


if __name__ == '__main__':
    larg = sys.argv
    app = QtWidgets.QApplication(larg)
    model = cmodel.cmodel_ph()
    model.add_at()
    mainwind1 = cbuilder(model)

    sys.exit(app.exec_())