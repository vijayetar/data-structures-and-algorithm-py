from ...dsa.challenges.array_binary_search.array_binary_search import BinarySearch, for_loop_search

def test_bs1():
  actual=BinarySearch([11,22,33,44,55,66,77], 90)
  expected = -1
  assert actual == expected

def test_bs2():
  actual=BinarySearch([4,8,15,16,23,42], 15)
  expected = 2
  assert actual == expected

def test_bs3():
  actual=BinarySearch([4,8,15,16,23,42], 23)
  expected = 4
  assert actual == expected

def test_bs4():
  actual=BinarySearch([4,8,15,16,23,42], 8)
  expected = 1
  assert actual == expected

def test_bs5():
  actual=BinarySearch([4,8,15,16,23,42], 42)
  expected = 5
  assert actual == expected

def test_bs6():
  actual=BinarySearch([4,8,15,16,23,42], 4)
  expected = 0
  assert actual == expected

def test_bs7():
  actual=BinarySearch([4,8,15,16,23,42], "")
  expected = -1
  assert actual == expected

def test_bs8():
  actual=BinarySearch(['a','b','c','d','e'], 4)
  expected = -1
  assert actual == expected

def test_bs9():
  actual=BinarySearch([], 4)
  expected = -1
  assert actual == expected

def test_fl1():
  actual=BinarySearch([11,22,33,44,55,66,77], 90)
  expected = -1
  assert actual == expected

def test_fl2():
  actual=for_loop_search([4,8,15,16,23,42], 15)
  expected = 2
  assert actual == expected

def test_fl3():
  actual=for_loop_search([4,8,15,16,23,42], 23)
  expected = 4
  assert actual == expected

def test_fl4():
  actual=for_loop_search([4,8,15,16,23,42], 8)
  expected = 1
  assert actual == expected

def test_fl5():
  actual=for_loop_search([4,8,15,16,23,42], 42)
  expected = 5
  assert actual == expected

def test_fl6():
  actual=for_loop_search([4,8,15,16,23,42], 4)
  expected = 0
  assert actual == expected

def test_fl7():
  actual=for_loop_search([4,8,15,16,23,42], "")
  expected = -1
  assert actual == expected

def test_fl8():
  actual=for_loop_search(['a','b','c','d','e'], 4)
  expected = -1
  assert actual == expected

def test_fl9():
  actual=for_loop_search([], 4)
  expected = -1
  assert actual == expected
