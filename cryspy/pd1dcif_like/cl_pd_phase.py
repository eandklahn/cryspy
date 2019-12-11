__author__ = 'ikibalin'
__version__ = "2019_12_10"
import os
import numpy

import warnings
from typing import List, Tuple

from cryspy.common.cl_item_constr import ItemConstr
from cryspy.common.cl_loop_constr import LoopConstr
from cryspy.common.cl_fitable import Fitable

class PdPhase(ItemConstr):
    """
PdPhase describes ...

Description in cif file::

 _pd_phase_label  Fe3O4 
 _pd_phase_scale  0.02381 
 _pd_phase_igsize 0.0
    """
    MANDATORY_ATTRIBUTE = ("label", "scale")
    OPTIONAL_ATTRIBUTE = ("igsize", )
    INTERNAL_ATTRIBUTE = ()
    PREFIX = "pd_phase"
    def __init__(self, label=None, scale=None, igsize=None):
        super(PdPhase, self).__init__(mandatory_attribute=self.MANDATORY_ATTRIBUTE, 
                                      optional_attribute=self.OPTIONAL_ATTRIBUTE, 
                                      internal_attribute=self.INTERNAL_ATTRIBUTE,
                                      prefix=self.PREFIX)

        self.label = label
        self.scale = scale
        self.igsize = igsize

    @property
    def label(self):
        return getattr(self, "__label")
    @label.setter
    def label(self, x):
        if x is None:
            x_in = None
        else:
            x_in = str(x)
        setattr(self, "__label", x_in)

    @property
    def scale(self):
        return getattr(self, "__scale")
    @scale.setter
    def scale(self, x):
        if x is None:
            x_in = None
        elif isinstance(x, Fitable):
            x_in = x
        else:
            x_in = Fitable()
            flag = x_in.take_it(x)
        setattr(self, "__scale", x_in)

    @property
    def igsize(self):
        return getattr(self, "__igsize")
    @igsize.setter
    def igsize(self, x):
        if x is None:
            x_in = None
        elif isinstance(x, Fitable):
            x_in = x
        else:
            x_in = Fitable()
            flag = x_in.take_it(x)
        setattr(self, "__igsize", x_in)

    def __repr__(self):
        ls_out = []
        ls_out.append(f"PdPhase:\n{str(self):}")
        return "\n".join(ls_out)
            
    def _show_message(self, s_out: str):
        warnings.warn("***  Error ***\n"+s_out, UserWarning, stacklevel=2)

    @property
    def is_variable(self) -> bool:
        """
Output: True if there is any refined parameter
        """
        res = any([self.scale.refinement, 
                   self.igsize.refinement])
        return res        

    def get_variables(self) -> List:
        """
Output: the list of the refined parameters
        """
        l_variable = []
        if self.scale.refinement: l_variable.append(self.scale)
        if self.igsize.refinement: l_variable.append(self.igsize)
        return l_variable
    


class PdPhaseL(LoopConstr):
    """
PdPhaseL describes ...

Description in cif file::

 loop_
 _pd_phase_label
 _pd_phase_scale
 _pd_phase_igsize
  Fe3O4 0.02381 0.0
    """
    CATEGORY_KEY = ("label", )
    ITEM_CLASS = PdPhase
    def __init__(self, item=[], loop_name=""):
        super(PdPhaseL, self).__init__(category_key=self.CATEGORY_KEY, item_class=self.ITEM_CLASS, loop_name=loop_name)
        self.item = item

    def __repr__(self) -> str:
        ls_out = []
        ls_out.append("PdPhaseL: ")
        ls_out.append(f"{str(self):}")
        return "\n".join(ls_out)
