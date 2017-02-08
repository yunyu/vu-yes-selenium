import sys, os, time
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = getattr(webdriver, sys.argv[1])()

driver.get("https://webapp.mis.vanderbilt.edu/more/Entry.action")
print("Loading login page...")
assert "Vanderbilt Single Sign-on" == driver.title

vunetId = driver.find_element_by_name("username")
vunetId.clear()
vunetId.send_keys(os.environ["VUNET_ID"])

password = driver.find_element_by_name("password")
password.clear()
password.send_keys(os.environ["VUNET_PW"])

driver.find_element_by_name("submit").click()
print("Signing in...")

WebDriverWait(driver, 15, 0.05).until(EC.title_contains("Student Registration"))
driver.find_element_by_xpath("//*[contains(text(), 'In Cart')]").click()
print("Opening cart...")

enrollmentMenus = WebDriverWait(driver, 15, 0.05).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".yui-button.yui-menu-button.enrollmentButton")))
print("Selecting waitlist if full... (" + str(len(enrollmentMenus)) + " menus)")

for menu in enrollmentMenus:
	menu.click()
	print("Clicking menu...")

	for waitlistText in reversed(WebDriverWait(driver, 5, 0.05).until(EC.presence_of_all_elements_located((By.XPATH, 
	 	"//*[contains(text(), 'Waitlist If Full')]")))):
	 	try:
	 		waitlistText.click()
	 		print("Clicked waitlist!")
	 	except ElementNotVisibleException:
	 		pass

submit = driver.find_element_by_id("enrollButton")
clicked = False

try:
	submit.click()
	clicked = True
except:
	pass

if not clicked:
	print("Unable to find submit button!")
else:
	print("Button clicked, waiting...")
	WebDriverWait(driver, 15, 0.05).until(EC.invisibility_of_element_located((By.ID, "ajaxModalPanel_c")))
	time.sleep(0.2)

driver.close()
