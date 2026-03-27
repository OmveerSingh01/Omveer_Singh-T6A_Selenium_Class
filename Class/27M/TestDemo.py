# Pytest File name should start with 'test_' ,then only it can detect that it is a test script
class TestDemo:
    # def __init__(self):
    #     print('Testing Demo')
    def register(self):
        print('registered')
    def test_login(self):
        print('Logging In')
    def test_logout(self):
        print('Logging Out')

'''For Pytest it is not necessary to explicitly made objects and call functions
For Pytest there is no concept of constructors'''

obj1 = TestDemo()
obj1.test_login()
obj1.test_logout()