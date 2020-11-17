# Wi-Fi switch for UPC routers
- Actually supported just for Czech language

## Requirements
- [Python](https://www.python.org/downloads/)
- [Mozilla Firefox](https://www.mozilla.org/)
- [Gecko driver](https://github.com/mozilla/geckodriver/releases)

## How to start
- Be sure you've passed Installation and Configuration !!
    - Win: double click to start.bat
    - Any other OS: open terminal in ./switch folder and type "python main.py"

## Installation
1. Download latest [release](https://github.com/JakubSladek/upc-router-wifi-switch/releases)
2. Unzip files anywhere you want
3. Install required packages
    - Win: double click to install.bat
    - Any other OS: Open the folder in terminal and type "pip install -r requirements.txt" and press enter

## Configuration
1. Open /config folder and edit config.py with any text editor
2. Use scheme below to edit your config

- password: your login password to router
- url: router login url
- headless: run in background
- firefoxPath: absolute path to firefox binary
- geckoPath: absolute path to gecko driver binary

### Example:
```python 
switch = {
    "password": "myPassword123",
    "url": "http://192.168.0.1/",
    "headless": True,
    "firefoxPath": r"C:\Program Files\Mozilla Firefox\firefox.exe",
    "geckoPath": r"C:\Gecko\geckodriver.exe"
}
```