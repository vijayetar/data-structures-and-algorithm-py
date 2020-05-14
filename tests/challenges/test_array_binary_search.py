from ...dsa.challenges.array_binary_search.array_binary_search import binary_search

def test_bs1():
  actual=BinarySearch([1,2,3,4,5],6)
  expected = -1
  assert actual == expected

def test_bs2():
  actual=BinarySearch([1,2,3,4,5],1)
  expected = 0
  assert actual == expected

def test_bs3():
  actual=BinarySearch([1,2,3,4,5],5)
  expected = 4
  assert actual == expected

def test_bs4():
  actual=BinarySearch([1,2,3,4,5],4)
  expected = 3
  assert actual == expected

def test_bs5():
  actual=BinarySearch([1,2,3,4,5],2)
  expected = 1
  assert actual == expected

def test_bs5():
  actual=BinarySearch([1,2,3,4,5],2)
  expected = 1
  assert actual == expected
