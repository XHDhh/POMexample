#coding = utf-8
import unittest
class FristCase001(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('所有case的前置条件')

    def setUp(self):
        print('前置条件')

    def tearDown(self):
        print('后置条件')

    #case名要以test开始
    def testfirst001(self):
        print('02first case')

    @unittest.skip('不执行这一条')
    def first002(self):
        print('02second case')

    def testfirst003(self):
        print('02third case')



if __name__ == '__main__':
    unittest.main()
    #suite = unittest.TestSuite()
    #suite.addTest(FristCase01('first02'))
    #unittest.TextTestRunner().run(suite)