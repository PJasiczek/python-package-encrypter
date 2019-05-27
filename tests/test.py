from myPackage import somePython


def test_encryptText():
    '''
    make sure that square is arranged correctly
    '''

    assert somePython.encryptText("abcdefghijklmnoprst","adaa") == "beaXa", 'something went wrong!'