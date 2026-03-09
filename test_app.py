from app import sumF

def test_SumF():
    assert sumF(1,2) == 3
    assert sumF(-1,1) == 0
    assert sumF(0,0) == 0
    assert sumF(2.5,3.5) == 6.0