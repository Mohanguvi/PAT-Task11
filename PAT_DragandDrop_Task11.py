import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class DragAndDrop:
    def __init__(self, url):
        """Initialize the DragAndDrop class."""
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.action = ActionChains(self.driver)

    def boot(self):
        """Load the webpage and switch to the iframe."""
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")) #to perform drag and drop need to switch to the iframe
        time.sleep(3)   # delay to load element

    def quit(self):
        """Quit the WebDriver."""
        self.driver.quit()

    def dragAndDrop(self):
        """Perform drag and drop action."""
        try:
            self.boot() # Boot the page and switch to iframe
            source_element = self.driver.find_element(By.ID, "draggable")   # Locate source (draggable) element
            target_element = self.driver.find_element(By.ID, "droppable")   # Locate target (droppable) element
            self.action.drag_and_drop(source_element, target_element).perform()     # Perform drag and drop action
            dropped_text = target_element.text      # Get text of the dropped element
            # Verify if the drag and drop is successful
            expected_text = "Dropped!"
            if dropped_text == expected_text:
                print("Drag and drop successful!")
            else:
                print("Drag and drop unsuccessful!")
            return dropped_text
        except NoSuchElementException as e:
            print("Error during drag and drop:", e)
        finally:
            time.sleep(5)
            self.quit()

url = "https://jqueryui.com/droppable/"
obj = DragAndDrop(url)
dropped_text = obj.dragAndDrop()


'''
Output: Drag and drop successful!
'''


