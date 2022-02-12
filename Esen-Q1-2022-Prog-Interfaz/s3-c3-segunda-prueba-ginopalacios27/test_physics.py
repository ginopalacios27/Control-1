from physics import getVelocity, getMean


def test_add():
    result = getVelocity(0, 0)
    assert result == 0
    result = getVelocity(4, 2)
    assert result == 2


def test_addNumberList_pepito():
    result = getMean([])
    assert result == 0
    result = getMean([1, 2])
    assert result == 3 / 2
    result = getMean([1, 2, 3])
    assert result == 6 / 3
