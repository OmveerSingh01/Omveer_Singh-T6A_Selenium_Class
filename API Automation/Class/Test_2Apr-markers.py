import pytest

# Normal Marker
@pytest.mark.om
def test_name():
    assert 'Hi' == 'Hi',"Not Equal"
    assert 5 ==5 ,"Not Equal"

@pytest.mark.login
def test_login():
    print('Logging In')
    l1 = [2,3,4,5]
    if 4 in l1:
        print('Logged In')
    assert 5 == 5,"Not Equal"

@pytest.mark.skip
def test_pass():
    print('Pass')
    assert True == True,"Not Equal"
    assert False == False,"Not Equal"

@pytest.mark.skipif(3==3, reason="Not Equal")
def test_fail():
    l2= [2,3,4,5]
    if 4 in l2:
        print('Logged Out')

