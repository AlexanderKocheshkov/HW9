import func_two

def test_summator_0_60():
	assert func_two.summator(0, 60) == 60

def test_multiplexor_0_dot_5_minus_5():
	assert func_two.multiplexor(0.5, -5) == -2.5
