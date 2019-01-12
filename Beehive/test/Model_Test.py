

# Created by Jake Stephens

import unittest


class Model_Test(unittest.TestCase):

    def test_1(self):
        pass

    def setUp(self):
        print("setup")

    def tearDown(self):
        print("teardown")


if __name__ == '__main__':
    unittest.main()