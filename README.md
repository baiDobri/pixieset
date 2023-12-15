# Python Script for Downloading Images from Pixieset Collections

## Overview
This script is designed to automate the downloading of high-quality images from Pixieset collections. It uses Selenium for web automation and a ThreadPoolExecutor for efficient parallel downloading.

## Features
- **Automatic Scrolling**: Scrolls through the Pixieset collection page until the 'Back to Top' button is found.
- **Image Identification and Filtering**: Identifies image tags and filters for the highest quality images.
- **Parallel Downloading**: Utilizes a ThreadPoolExecutor for downloading images in parallel.
- **Customizable URL**: Easily adaptable to any Pixieset collection by modifying the URL variable.

## Requirements
- Selenium
- ThreadPoolExecutor (part of the standard Python library)

## Usage
1. **Set Up Selenium**: Ensure Selenium is installed and properly set up with the required web driver.
2. **Specify the URL**: Modify the `URL` variable in the script to point to the desired Pixieset collection.
3. **Run the Script**: Execute the script. It will automatically navigate the Pixieset collection, identify and download the high-quality images.
