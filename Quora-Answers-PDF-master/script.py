import time
import pdfkit
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from config import url, phantomjs_path


driver = webdriver.PhantomJS(executable_path=phantomjs_path)
driver.set_window_size(1366, 768) # optional
driver.get(url)   # Go to the specified url
time.sleep(3)

body = driver.find_element_by_tag_name("body")
answers_count = int(driver.find_element_by_class_name("answer_count").text.split(" ")[0])	#Find the total number of answers
print "Total answers : ", answers_count
answers_loaded_count = len(driver.find_elements_by_class_name("pagedlist_item"))	# Number of Answers on the first page

counter = 0

while True:

	body.send_keys(Keys.END)		#Load the page completely so that it contains all the answers
	time.sleep(3)
	answers_loaded_again_count = len(driver.find_elements_by_class_name("pagedlist_item"))
	if answers_loaded_count == answers_loaded_again_count:		#checking if it reached the bottom
		count += 1
		if count == 2:
			break
	else:
		answers_loaded_count = answers_loaded_again_count

time.sleep(3)


raw_html = driver.page_source		#returns html code of the complete page

file_name = url.split('/')[-1]+'.pdf'
pdfkit.from_string(raw_html,file_name)
