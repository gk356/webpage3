import pytest
import bmi

def test_calc_bmi():
     assert bmi.cal_bmi(63, 125) == 22.53

def test_cal_bmi2():
     assert bmi.cal_bmi(57, 200) == 44.01
def test_cal_bmi3():
     assert bmi.cal_bmi(76, 125) == 15.58

