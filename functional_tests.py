from selenium import webdriver

#browser = webdriver.Firefox()
#browser.get('http://localhost:8000')

# assert 'Django' in browser.title
#assert 'To-Do' in browser.title, "Browser title was mumus galau" + browser.title

#browser.quit()

import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

#	def check_for_now_row_in_list_table(self, row_text):
#		table = self.browser.find_element_by_id('id_list_table')
#		rows = table.find_elements_by_tag_name('tr')
#		self.assertIn(row_text, [row.text for now in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get('http://localhost:8000')

		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
#		self.fail('Finish the test!')
		
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribbute('placeholder'),
			'Enter a to-do item'
		)

		inputbox.send_keys('Buy peacock feathers')
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Buy peacock feathers')
		)
		self.fail('Finish the test!')

if __name__=='__main__':
	unittest.main(warnings="ignore")
