from unittest import TestCase
from get_time import getdate


class TestGetdate(TestCase):

    # valid value confirmation returns a bool
    def assertIsTrue(self, test_value):
        try:
            self.assertIs(test_value, True)
            return True
        except ValueError:
            return False

    # invalid value confirmation returns a bool
    def assertIsFalse(self, test_value):
        try:
            self.assertIs(test_value, False)
            return True
        except ValueError:
            return False

    # test suite
    def test_getdate(self):

        test_input = '2019-01-01'
        test_result = self.assertIsTrue(getdate(test_input))
        if test_result is True:
            print(test_input + ' Passed : Expected Result True : Actual Result True')
        else:
            print(test_input + ' Failed : Expected Result True : Actual Result False')

        test_input = '2019-12-12'
        test_result = self.assertIsTrue(getdate(test_input))
        if test_result is True:
            print(test_input + ' Passed : Expected Result True : Actual Result True')
        else:
            print(test_input + ' Failed : Expected Result True : Actual Result False')

        test_input = '2019-12-13'
        test_result = self.assertIsTrue(getdate(test_input))
        if test_result is True:
            print(test_input + ' Passed : Expected Result True : Actual Result True')
        else:
            print(test_input + ' Failed : Expected Result True : Actual Result False')

        test_input = '2019-12-27'
        test_result = self.assertIsTrue(getdate(test_input))
        if test_result is True:
            print(test_input + ' Passed : Expected Result True : Actual Result True')
        else:
            print(test_input + ' Failed : Expected Result True : Actual Result False')

        test_input = '2019-10-28'
        test_result = self.assertIsTrue(getdate(test_input))
        if test_result is True:
            print(test_input + ' Passed : Expected Result True : Actual Result True')
        else:
            print(test_input + ' Failed : Expected Result True : Actual Result False')

        test_input = '2019-10-29'
        test_result = self.assertIsTrue(getdate(test_input))
        if test_result is True:
            print(test_input + ' Passed : Expected Result True : Actual Result True')
        else:
            print(test_input + ' Failed : Expected Result True : Actual Result False')

        test_input = '2019-10-30'
        test_result = self.assertIsTrue(getdate(test_input))
        if test_result is True:
            print(test_input + ' Passed : Expected Result True : Actual Result True')
        else:
            print(test_input + ' Failed : Expected Result True : Actual Result False')

        test_input = '2019-10-31'
        test_result = self.assertIsTrue(getdate(test_input))
        if test_result is True:
            print(test_input + ' Passed : Expected Result True : Actual Result True')
        else:
            print(test_input + ' Failed : Expected Result True : Actual Result False')

        test_input = '2019-12-00'
        test_result = self.assertIsFalse((getdate(test_input)))
        if test_result is True:
            print(test_input + ' Passed : Expected Result False : Actual Result False')
        else:
            print(test_input + ' Failed : Expected Result False : Actual Result True')

        test_input = '2019-00-12'
        test_result = self.assertIsFalse((getdate(test_input)))
        if test_result is True:
            print(test_input + ' Passed : Expected Result False : Actual Result False')
        else:
            print(test_input + ' Failed : Expected Result False : Actual Result True')

        test_input = '2019-13-12'
        test_result = self.assertIsFalse((getdate(test_input)))
        if test_result is True:
            print(test_input + ' Passed : Expected Result False : Actual Result False')
        else:
            print(test_input + ' Failed : Expected Result False : Actual Result True')

        test_input = '2019-27-12'
        test_result = self.assertIsFalse((getdate(test_input)))
        if test_result is True:
            print(test_input + ' Passed : Expected Result False : Actual Result False')
        else:
            print(test_input + ' Failed : Expected Result False : Actual Result True')

        test_input = '2019-28-10'
        test_result = self.assertIsFalse((getdate(test_input)))
        if test_result is True:
            print(test_input + ' Passed : Expected Result False : Actual Result False')
        else:
            print(test_input + ' Failed : Expected Result False : Actual Result True')

        test_input = '2019-29-10'
        test_result = self.assertIsFalse((getdate(test_input)))
        if test_result is True:
            print(test_input + ' Passed : Expected Result False : Actual Result False')
        else:
            print(test_input + ' Failed : Expected Result False : Actual Result True')

        test_input = '2019-30-10'
        test_result = self.assertIsFalse((getdate(test_input)))
        if test_result is True:
            print(test_input + ' Passed : Expected Result False : Actual Result False')
        else:
            print(test_input + ' Failed : Expected Result False : Actual Result True')

        test_input = '2019-31-10'
        test_result = self.assertIsFalse((getdate(test_input)))
        if test_result is True:
            print(test_input + ' Passed : Expected Result False : Actual Result False')
        else:
            print(test_input + ' Failed : Expected Result False : Actual Result True')

        test_input = '2019-100-10'
        test_result = self.assertIsFalse((getdate(test_input)))
        if test_result is True:
            print(test_input + ' Passed : Expected Result False : Actual Result False')
        else:
            print(test_input + ' Failed : Expected Result False : Actual Result True')

        test_input = '2019-10-100'
        test_result = self.assertIsFalse((getdate(test_input)))
        if test_result is True:
            print(test_input + ' Passed : Expected Result False : Actual Result False')
        else:
            print(test_input + ' Failed : Expected Result False : Actual Result True')


# if __name__ == '__main__':
#     unittest.main()


# def check_valid_inputs(self):
# def check_invalid_inputs(self):
#     check_valid_inputs(self)

    # confirm test result
    # def confirm_test_input(self, test_input):
    #     test_result = self.assertIsTrue(getdate(test_input))
    #     if test_result is True:
    #         print(test_input + ' Pass')
    #     else:
    #         print(test_input + ' Fail')

# test_parameter = '2019-1-1'
# confirm_test_input(test_parameter)
