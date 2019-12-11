import pytest
import numpy
from cryspy.common.cl_fitable import Fitable

from cryspy.pd1dcif_like.cl_pd_exclude import PdExclude, PdExcludeL

STR_FROM_CIF_1 = """
 loop_
 _pd_exclude_id
 _pd_exclude_ttheta_min
 _pd_exclude_ttheta_max
  1   4.0  12.0 
  2  30.0  45.0 
  3  58.0  63.0 
"""

def test_init():
    try:
        _object = PdExcludeL()
        flag = True
    except:
        flag = False
    assert flag

def test_to_cif():
    try:
        _object = PdExcludeL()
        _str = _object.to_cif
        flag = True
    except:
        flag = False
    assert flag

def test_init_el():
    try:
        _object = PdExclude()
        flag = True
    except:
        flag = False
    assert flag

def test_to_cif_el():
    try:
        _object = PdExclude()
        _str = _object.to_cif
        flag = True
    except:
        flag = False
    assert flag


def test_from_cif():
    l_obj = PdExcludeL.from_cif(STR_FROM_CIF_1)
    assert len(l_obj) == 1
    _obj = l_obj[0]
    assert _obj.id == ["1", "2", "3"]
    assert _obj["1"].ttheta_min == 4.0
    val = _obj.to_cif(separator=".")

