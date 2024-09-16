# Homework 3 CSS selectors
from selenium.webdriver.common.by import By

# Amazon logo on create account page
driver.find_element(By.CSS_SELECTOR, ".a-icon.a-icon-logo")
# Create Account Box
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")
# Your Name Box
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")
# Email Box
driver.find_element(By.CSS_SELECTOR, "#ap_email")
# Password Box
driver.find_element(By.CSS_SELECTOR, "#ap_password")
# "Passwords must be at least 6 characters
driver.find_element(By.CSS_SELECTOR, "[placeholder='At least 6 characters']")
# Re-enter password box
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")
# Continue Button
driver.find_element(By.CSS_SELECTOR, "#continue")
# Conditions of use link
driver.find_element(By.CSS_SELECTOR, "[href*='condition_of_use?']")
# Privacy Notice Link
driver.find_element(By.CSS_SELECTOR, "[href*='notification_privacy_notice']")
# Sign in link
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")


