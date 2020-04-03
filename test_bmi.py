import pytest
import bmi

def test_calc_bmi():
     assert bmi.cal_bmi(56.25,1.5750000000000002) == 22.67573696145124

def test_cal_bmi2():
     assert bmi.cal_bmi(45.0, 1.725) == 15.1
def test_cal_bmi3():
     assert bmi.cal_bmi(90.0, 1.425) == 44.32132963988919

