from fib import *

def test_fib9():
    myval = fib(9)
    assert myval == 256, "Wrong value found for fib(9)"

def test_fib0():
    myval = fib(0)
    exval = 1.
    assert myval == exval, "Broken on 0 edge case"

def test_fib1():
    myval = fib(1)
    exval = 1.
    assert myval == exval, "Broken on 1 edge case"
	
