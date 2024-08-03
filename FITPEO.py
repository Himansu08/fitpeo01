#Import all module
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


#Call the driver
driver= webdriver.Chrome()
#Maximize the window
driver.maximize_window()

#TASK
# Navigate to the FitPeo Homepage:
driver.get("https://www.fitpeo.com/home")

# Navigate to the Revenue Calculator Page:
wait = WebDriverWait(driver, 10)  # Wait for 10 seconds at most
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'MuiBox')]/a[contains(@href,'/revenue-calculator')]"))).click()
time.sleep(5)

# Scroll Down to the Slider section:
scroll_page=wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'MuiSlider')]/input")))
driver.execute_script("arguments[0].scrollIntoView();", scroll_page)
time.sleep(5)

#task 4
# Adjust the Slider to 817
# i am not set it to 820 but adjust at 817:
current_value = scroll_page.get_attribute("aria-valuenow")  # Replace with actual attribute if needed
actions = ActionChains(driver)
actions.move_to_element(scroll_page).drag_and_drop_by_offset(scroll_page,93,0).perform()
time.sleep(10)




# Update the Text Field 560 :
# :
text_field = driver.find_element(By.XPATH, "//input[@aria-invalid='false']")
actions.click(text_field).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
text_field.send_keys("560")
pos=scroll_page.get_attribute("aria-valuenow")
# Validate Slider Value 560
assert pos=="560",f"The Expected value should be 560 but we found {pos}"

# Update the text field with 820
text_field = driver.find_element(By.XPATH, "//input[@aria-invalid='false']")
actions.click(text_field).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
text_field.send_keys("820")
time.sleep(10)







# Select CPT Codes the checkbox:
cpt_codes = ["CPT-99091", "CPT-99453", "CPT-99454", "CPT-99474"]
for code in cpt_codes:
    locator="//p[text()='{}']/..//span[contains(@class,'Checkbox')]".format(code)
    checkbox = driver.find_element(By.XPATH,locator )
    checkbox.click()
    time.sleep(1)
time.sleep(10)


# Validate total recurring reimbursement
total_reimbursement_element = driver.find_element(By.XPATH, "//p[contains(text(),'Total Recurring Reimbursement for all Patients Per Month:')]/p")
total_reimbursement_text = total_reimbursement_element.text
time.sleep(10)


#Verify that the header displaying Total Recurring Reimbursement for all Patients Per Month: shows the value $110700.
assert total_reimbursement_text == "$110700",f"The Expected Total Reimbursement $110700 but found {total_reimbursement_text}"



# Close the browser
driver.quit()

















































































































































































# checkbox = ["57","2y483","2u4924u"]
# for ele in chkbox:
# 	dynamic_locator_for_chkpbx = '//input[@class="PrivateSwitchBase-input css-1m9pwf3"]/../following-sibling::span[text()="{ele}"]/../span[contains(@class,"Checkbox")]'.format(ele)
# 	wait,until(EC,visiekefnjel(By.Xpath).click()
# time.sleep(3)