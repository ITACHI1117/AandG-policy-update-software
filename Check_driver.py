from selenium import webdriver
import requests
import zipfile
import wget
import subprocess
import os
from pathlib import Path
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service



# CHROMEDRIVER_PATH =  r""
CHROMEDRIVER_FOLDER = r"./"
LATEST_DRIVER_URL = "https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_STABLE"
SOURCE_FILE = r"./chromedriver-win64/chromedriver.exe"
DESTINATION_DIRECTORY = r"./"

def Check_and_install_Updated_driver():
    Status =""
    def get_latest_driver():
        downloads_path = Path.home() / "Downloads/LATEST_RELEASE_STABLE"
        file_path = downloads_path

        with open(file_path, 'r') as file:
            file_content = file.read()

        # Display the content that was read from the file
        print(file_content)
        return file_content

    def download_latest_version(version_number):
        print("Attempting to download latest driver online......")
        download_url = "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/119.0.6045.105/win64/chromedriver-win64.zip"
        # "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/119.0.6045.105/win64/chromedriver-win64.zip"
        # download zip file
        latest_driver_zip = wget.download(download_url, out=CHROMEDRIVER_FOLDER)
        # read & extract the zip file
        try:
            with zipfile.ZipFile(latest_driver_zip, 'r') as downloaded_zip:
                # You can chose the folder path to extract to below:
                downloaded_zip.extractall(path=CHROMEDRIVER_FOLDER)
            # delete the zip file downloaded above
            os.remove(latest_driver_zip)
            os.rename(SOURCE_FILE, os.path.join(DESTINATION_DIRECTORY, os.path.basename(SOURCE_FILE)))
            os.remove(f"./chromedriver-win64")
        except Exception as error:
            print(error)

    def check_driver():
        # run cmd line to check for existing web-driver version locally
        cmd_run = subprocess.run("chromedriver --version",
                                 capture_output=True,
                                 text=True)
        # Extract driver version as string from terminal output
        local_driver_version = cmd_run.stdout.split()[1]
        print(f"Local driver version: {local_driver_version}")
        # check for latest chromedriver version online
        response = get_latest_driver()
        online_driver_version = response
        print(f"Latest online chromedriver version: {online_driver_version}")
        if local_driver_version == online_driver_version:
            return True
        else:
            os.remove(r"chromedriver.exe")
            download_latest_version(online_driver_version)

    check_driver()

    if check_driver() == True:
        Status = "The Driver Version is up-to-date"
        print("The Driver Version is up-to-date")
    return Status


Status = Check_and_install_Updated_driver()
print(Status)