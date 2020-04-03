import retirement
import pytest

def test_cal_retirement1():
    assert retirement.cal_retirement(2,2,2,2) == 2.85

def test_cal_retirement2():
    assert retirement.cal_retirement(45000, 35, 100000, 25) == 26.43

def test_cal_retirement3():
    assert retirement.cal_retirement(80000, 20, 250000, 50) == 52.26

def test_cal_retirement4():
    assert retirement.cal_retirement(20000, 35, 1000000, 80) == 112.21



