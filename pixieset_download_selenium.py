import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from concurrent.futures import ThreadPoolExecutor

def download_image(img_url, name):
    img_response = requests.get(img_url)
    if img_response.status_code == 200:
        with open(name, 'wb') as file:
            file.write(img_response.content)
        print(f"Downloaded {name}")
    else:
        print(f"Failed to download {name}")

def download_images(url):

    # Set up Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.headless = True  # Run Chrome in headless mode (without a GUI)
    driver = webdriver.Chrome(options)

    # Open the URL
    driver.get(url)

    # Continuously scroll down until the 'Back to Top' button is found
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(3)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            # Try to locate the Back to Top button
            if driver.find_elements(By.ID, "back-top-btn"):
                break
        last_height = new_height

    # Find all image tags
    image_tags = driver.find_elements(By.TAG_NAME, 'img')
    print(f"Found {len(image_tags)} images")

    # Filter out the tags with the highest quality images and their names
    images = {}
    for tag in image_tags:
        src = tag.get_attribute('src')
        if src and '-medium.JPG' in src:
            xxlarge_src = src.replace('-medium.JPG', '-xxlarge.JPG')
            original_name = tag.get_attribute('alt').split('.')[0] + '.JPG'
            images[xxlarge_src] = original_name

    # Close the browser
    driver.quit()
    print(f"{len(images)} images to be saved")

    # Download images in parallel using ThreadPoolExecutor
    with ThreadPoolExecutor(10) as executor:
        for img_url, name in images.items():
            executor.submit(download_image, img_url, name)

# URL of the website
## change the url to your own pixieset url
url = "https://<CHANGEME>.pixieset.com/collection-XX/"

# Call the function
download_images(url)
