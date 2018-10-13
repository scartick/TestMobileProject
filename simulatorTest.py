
import unittest
from appium import webdriver
import desired_capabilities
import os
import page
 

# Test cases   
class Tests(unittest.TestCase): 
    
    def setUp(self):
        self.desired_caps = desired_capabilities.get_desired_capabilities('TestApp.app.zip')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps) 
      
   # def tearDownClass(self):
      #  cmd = 'killall Simulator'
      #  os.system(cmd)
 
    def test_compute_sum(self):  
        self.driver.implicitly_wait(80)
        self.page.input_first_field(3)
        self.page.input_second_field(2)
        self.page.copute_sum()
        result = self.page.get_compute_sum()
        self.assertEqual(result, "5")  

if __name__ == '__main__':
    unittest.main()  
