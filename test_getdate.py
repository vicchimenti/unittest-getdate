from unittest import TestCase
from get_time import getdate


class TestGetdate(TestCase):

    def assertIsTrue(self, test_value):
        try:
            self.assertIs(test_value, True)
            return True
        except ValueError:
            return False

    def assertIsFalse(self, test_value):
        try:
            self.assertIs(test_value, False)
            return True
        except ValueError:
            return False

    def test_getdate(self):
        test_input = '2019-01-01'
        test_result = self.assertIsTrue(getdate(test_input))
        if test_result is True:
            print(test_input + ' Pass')
        else:
            print(test_input + ' Fail')

        self.assertTrue(getdate('2019-12-12'))
        self.assertTrue(getdate('2019-12-13'))
        self.assertTrue(getdate('2019-12-27'))
        self.assertTrue(getdate('2019-10-28'))
        self.assertTrue(getdate('2019-10-29'))
        self.assertTrue(getdate('2019-10-30'))
        self.assertTrue(getdate('2019-10-31'))

        test_input = '2019-12-0'
        if self.assertIsFalse(getdate(test_input)) is True:
            print(test_input + ' Pass')
        else:
            print(test_input + ' Fail')

        self.assertFalse(getdate('2019-0-12'))
        self.assertFalse(getdate('2019-13-12'))
        self.assertFalse(getdate('2019-27-12'))
        self.assertFalse(getdate('2019-28-10'))
        self.assertFalse(getdate('2019-29-10'))
        self.assertFalse(getdate('2019-30-10'))
        self.assertFalse(getdate('2019-31-10'))
        self.assertFalse(getdate('2019-100-10'))
        self.assertFalse(getdate('2019-10-100'))


# if __name__ == '__main__':
#     unittest.main()

# def check_valid_inputs(self):
# def check_invalid_inputs(self):
#     check_valid_inputs(self)
