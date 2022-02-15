from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyaparat.exceptions import QualityError

qualities = {
    '144p': 0,
    '240p': 1,
    '360p': 2,
    '480p': 3,
    '720p': 4,
    '1080p': 5
}


class Scraper:

    def __init__(self, url=None, quality=None):
        self.url = url
        self.quality = quality
        self.driver = driver = Chrome('./chromedriver')
        self.links = self.get_all_links()

    def get_all_links(self):
        links = []
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        chain = ActionChains(self.driver)
        chain.move_to_element(self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="download"]'))
        chain.click()
        chain.perform()
        links_element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.fade-enter-done')),
        )
        for link in links_element.find_elements(By.CSS_SELECTOR, 'li.menu-item-link'):
            selector = link.find_element(By.CSS_SELECTOR, 'a')
            links.append(selector.get_attribute('href'))
        self.driver.quit()
        return links

    def get_qualities(self):
        links = self.links
        qua = list(qualities.keys())
        available_qualities = []
        for i in range(len(links)):
            available_qualities.append(qua[i])
        return available_qualities

    def get_link(self):
        links = self.links
        available_qualities = self.get_qualities()
        if self.quality not in available_qualities:
            raise QualityError(f'This quality is unavailable\n available qualities are {available_qualities}')
        else:
            link = links[qualities[self.quality]]
            return link
