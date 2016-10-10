__author__ = "smeinecke"

import pytest
import pandapower as pp
import pandapower.networks as pn
import pandas as pd


def test_create_simple():
    net = pn.create_example_simple()
    pp.runpp(net)

    assert len(net.bus) >= 1
    assert len(net.line) >= 1
    assert len(net.gen) >= 1
    assert len(net.sgen) >= 1
    assert len(net.shunt) >= 1
    assert len(net.trafo) >= 1
    assert len(net.load) >= 1
    assert len(net.ext_grid) >= 1
    assert len(net.switch[net.switch.et == 'l']) >= 1
    assert len(net.switch[net.switch.et == 'b']) >= 1
    assert net.converged is True


def test_create_realistic():
    net = pn.create_example_realistic()
    pp.runpp(net)

    all_vn_kv = pd.Series([380, 110, 20, 10, 0.4])
    assert net.bus.vn_kv.isin(all_vn_kv).all()
    assert len(net.bus) >= 1
    assert len(net.line) >= 1
    assert len(net.gen) >= 1
    assert len(net.sgen) >= 1
    assert len(net.shunt) >= 1
    assert len(net.trafo) >= 1
    assert len(net.trafo3w) >= 1
    assert len(net.load) >= 1
    assert len(net.ext_grid) >= 1
    assert len(net.switch[net.switch.et == 'l']) >= 1
    assert len(net.switch[net.switch.et == 'b']) >= 1
    assert len(net.switch[net.switch.et == 't']) >= 1
    assert len(net.switch[net.switch.type == 'CB']) >= 1
    assert len(net.switch[net.switch.type == 'DS']) >= 1
    assert len(net.switch[net.switch.type == 'LBS']) >= 1
    assert len(net.switch[net.switch.closed == True]) >= 1
    assert len(net.switch[net.switch.closed == False]) >= 1
    assert len(net.impedance) >= 1
    assert len(net.xward) >= 1
    assert net.converged is True

if __name__ == '__main__':
    pytest.main(['-x', "test_create_example.py"])