from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from colorama import Fore, Style


def setup_driver(user_agent):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument(f"--user-agent={user_agent}")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver


def get_content(url, user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36"):
    # Handling URL
    driver = setup_driver(user_agent)
    try:
        driver.get(url)
    except WebDriverException:
        print(f"{Fore.LIGHTRED_EX}Web Driver Exception, ensure the URL '{url}' is correct{Style.RESET_ALL}")
        driver.quit()
        return []
    # Collecting content
    contents = []
    elements = driver.find_elements(By.CLASS_NAME, 'SetPageTerm-content')
    if elements:
        try:
            for i, element in enumerate(elements, 1):
                question = element.find_element(By.CLASS_NAME, 'SetPageTerm-wordText').text
                answer = element.find_element(By.CLASS_NAME, 'SetPageTerm-definitionText').text
                contents.append(f"QUESTION {i}\n{question}")
                contents.append(f"ANSWER {i}\n{answer}")
                print(f"{Fore.LIGHTBLUE_EX}Scraping Card Set: {Fore.WHITE}{i}{Fore.LIGHTYELLOW_EX}/{Fore.WHITE}{len(elements)}{Style.RESET_ALL}", end='\r')
        except NoSuchElementException:
            print(f"{Fore.LIGHTRED_EX}No matching elements found, ensure the URL is correct{Style.RESET_ALL}")
        except Exception as e:
            print(e)
    else:
        print(f"{Fore.LIGHTRED_EX}No matching elements found, ensure the URL is correct{Style.RESET_ALL}")
    driver.quit()
    return contents