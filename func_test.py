import func

def test_summ_1_2():
    assert func.summ(1, 2) == 3

def test_summ_2_2():
    assert func.summ(2, 2) == 4

def test_summ_0_0():
    assert func.summ(0, 0) == 0

def test_summ_10_0_dot_6():
    assert func.summ(10, 0.6) == 10.6

def test_summ_10_minus_2():
    assert func.summ(10, -2) == 8

def test_diff_1_2():
    assert func.diff(1, 2) == -1

def test_diff_4_2():
    assert func.diff(4, 2) == 2

def test_diff_10_8():
    assert func.diff(10, 8) == 2

def test_diff_0_dot_5_2():
    assert func.diff(0.5, 2) == -1.5

def test_diff_1_minus_2():
    assert func.diff(1, -2) == 3

def test_mult_1_2():
    assert func.mult(1, 2) == 2

def test_mult_4_2():
    assert func.mult(4, 2) == 8

def test_mult_8_0_dot_5():
    assert func.mult(8, 0.5) == 4

def test_mult_0_dot_5_0_dot_5():
    assert func.mult(0.5, 0.5) == 0.25

def test_mult_minus_0_dot_5_minus_0_dot_5():
    assert func.mult(-0.5, -0.5) == 0.25
