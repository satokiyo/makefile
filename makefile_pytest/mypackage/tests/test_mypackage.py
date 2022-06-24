from mypackage.src.mypackage import func, main


def test_func():
    assert "{:.2f}".format(func()) == "3.14", "小数点以下2桁までを比較"
    assert not func() == 3, "円周率は3ではない"


def test_main():
    assert main() == 0, "return value is 0"
