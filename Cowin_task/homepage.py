from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CowinAutomation:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Start the automation
    def start_automation(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            print("Browser launched and URL opened!")
            return True
        except Exception as e:
            print(f"ERROR: Unable to start the automation - {e}")
            return False

    # Close the browser
    def shutdown(self):
        self.driver.quit()
        print("Browser closed.")

    # Open FAQ and Partners links
    def open_faq_and_partners(self):
        try:
            # Click on the "Partners" link
            partners_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, " /html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a"))
            )
            partners_link.click()
            print("Clicked on Partners")
           
            # Click on the "FAQ" anchor tag
            faq_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "FAQ"))
            )
            faq_link.click()
            print("Clicked on FAQ")

            # Store the main window handle
            main_window = self.driver.current_window_handle
            
            

            # Fetch all window handles
            window_handles = self.driver.window_handles
            print(f"Windows/Frame IDs: {window_handles}")

            # Close the new windows and switch back to the main window
            for handle in window_handles:
                if handle != main_window:
                    self.driver.switch_to.window(handle)
                    self.driver.close()
                    print(f"Closed window: {handle}")
            
            # Switch back to the main window
            self.driver.switch_to.window(main_window)
            print("Returned to the main window.")
            return window_handles
        except Exception as e:
            print(f"ERROR: Unable to click on FAQ and Partners - {e}")
            return []

