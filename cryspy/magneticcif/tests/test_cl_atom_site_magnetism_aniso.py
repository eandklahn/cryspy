import pytest
import math
import numpy
from cryspy.common.cl_fitable import Fitable

from cryspy.magneticcif.cl_atom_site_magnetism_aniso import AtomSiteMagnetismAniso, AtomSiteMagnetismAnisoL

STR_FROM_CIF_1 = """
 loop_  
 _atom_site_magnetism_aniso_label
 _atom_site_magnetism_aniso_chi_type
 _atom_site_magnetism_aniso_chi_11
 _atom_site_magnetism_aniso_chi_12
 _atom_site_magnetism_aniso_chi_13
 _atom_site_magnetism_aniso_chi_22
 _atom_site_magnetism_aniso_chi_23
 _atom_site_magnetism_aniso_chi_33
 _atom_site_magnetism_aniso_moment_type
 _atom_site_magnetism_aniso_moment_11
 _atom_site_magnetism_aniso_moment_12
 _atom_site_magnetism_aniso_moment_13
 _atom_site_magnetism_aniso_moment_22
 _atom_site_magnetism_aniso_moment_23
 _atom_site_magnetism_aniso_moment_33
  Fe3A Cani -3.468(74) 0.0 0.0 -3.468 0.0 -3.468 Mani 0. 0. 0. 0. 0. 0.
  Fe3B Cani 3.041      0.0 0.0  3.041 0.0  3.041 Mani 0. 0. 0. 0. 0. 0.
    
    """

def test_init():
    try:
        _object = AtomSiteMagnetismAnisoL()
        flag = True
    except:
        flag = False
    assert flag

def test_to_cif():
    try:
        _object = AtomSiteMagnetismAnisoL()
        _str = _object.to_cif
        flag = True
    except:
        flag = False
    assert flag

def test_init_el():
    try:
        _object = AtomSiteMagnetismAniso()
        flag = True
    except:
        flag = False
    assert flag

def test_to_cif_el():
    try:
        _object = AtomSiteMagnetismAniso()
        _str = _object.to_cif
        flag = True
    except:
        flag = False
    assert flag


def test_from_cif():
    rel_tol, abs_tol =0.001, 0.0001
    l_obj = AtomSiteMagnetismAnisoL.from_cif(STR_FROM_CIF_1)
    assert len(l_obj) == 1
    _obj = l_obj[0]
    assert _obj.label == ["Fe3A", "Fe3B"]
    print("chi_11: ", _obj["Fe3A"].chi_11)
    assert math.isclose(_obj["Fe3A"].chi_11.value, -3.468, rel_tol=rel_tol, abs_tol=abs_tol)
    val = _obj.to_cif(separator=".")

