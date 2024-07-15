import requests
from bs4 import BeautifulSoup
import os
import re
from urllib.parse import urlparse
import string
from urllib.parse import urljoin

def scrape_pinterest_board(url):
    # Function to sanitize a filename
    def sanitize_filename(filename):
    # Remove invalid characters from the filename
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        filename = ''.join(c for c in filename if c in valid_chars)
        return filename

    # URL of your HTML file in the repository
    #url = #PINTERESR URL

    # Fetch the HTML content from the URL
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
    else:
        raise Exception(f"Failed to fetch HTML from {url}. Status code: {response.status_code}")

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all image tags
    img_tags = soup.find_all('img')

    # Directory to save images
    save_dir = 'images'

    # Create the directory if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)

    img_list=[]

    # Download each image
    for img in img_tags:
        img_url = img.get('src')
        
        # Extract filename from URL
        img_name = os.path.basename(urlparse(img_url).path)
        
        # Sanitize the filename
        img_name = sanitize_filename(img_name)
        
        img_save_path = os.path.join(save_dir, img_name)
        
        # Download the image
        response = requests.get(img_url)
        if response.status_code == 200:
            with open(img_save_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {img_name} successfully.")
            img_list.append(img_name)

        else:
            print(f"Failed to download {img_name}. Status code: {response.status_code}")
    return img_list


#This would not be required when integrated on the Myntra website but is written for convenience purposes.

def scrape_myntra(url):
    # Function to sanitize a filename
    def sanitize_filename(filename):
    # Remove invalid characters from the filename
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        filename = ''.join(c for c in filename if c in valid_chars)
        return filename

    # URL of your HTML file in the repository
    #url = myntra website

    # Fetch the HTML content from the URL
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
    else:
        raise Exception(f"Failed to fetch HTML from {url}. Status code: {response.status_code}")

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all image tags
    img_tags = soup.find_all('img')

    # Directory to save images
    save_dir = 'images'

    # Create the directory if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)

    img_list=[]

    # Download each image
    for img in img_tags:
        img_url = img.get('src')
        
        # Extract filename from URL
        img_name = os.path.basename(urlparse(img_url).path)
        
        # Sanitize the filename
        img_name = sanitize_filename(img_name)
        
        img_save_path = os.path.join(save_dir, img_name)
        
        # Download the image
        response = requests.get(img_url)
        if response.status_code == 200:
            with open(img_save_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {img_name} successfully.")
            img_list.append(img_name)

        else:
            print(f"Failed to download {img_name}. Status code: {response.status_code}")
    return img_list
