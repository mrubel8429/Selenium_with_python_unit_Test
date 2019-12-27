import unittest
from selenium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("../drivers/chromedriver")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    def test_Google_Search(self):
        self.driver.get("https://google.com")
        x=self.driver.title
        print("Title of this page is :", x)
        self.assertEqual(x,"Google")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Complete Test")


if __name__ == '__main__':
    unittest.main()
