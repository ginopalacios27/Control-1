from problem_01 import friend


def test_problem_01():
    assert friend(["Ryan", "Kieran", "Mark"]) == ["Ryan", "Mark"]
    assert friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]) == ["Ryan"]
    assert friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]) == ["Jimm", "Cari", "aret"]
    