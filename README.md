<h1 align="center">
bKash Check Balance Automation
</h1>

## Overview

This project tried to automate the process of balance checking in the bKash app using Appium. The script handles and denies the initial popup for location access and attempts to enter the user's bKash PIN to log in and check the balance. If the user is already logged in, the script directly checks the balance.

## Project Structure
```
.
├── README.md
└── src
    └── automation.py
```

## Prerequisites

1. **Android Device**: Ensure your Android device is connected via USB cable with USB debugging enabled and `adb` recognizes it.
2. **Appium Server**: (http://appium.io/)
3. **Python Environment**: Python 3.x
4. **adb** (https://developer.android.com/tools/adb) (part of Android SDK)

## Installation

1. **Clone the repository**:
    ```
    git clone https://github.com/YeakubSadlil/appium-automation.git 
    ```

2. **Set up Python environment**:
    ```
    pip install -r requirements.txt 
    ```

3. **Install Appium**:
    ```
    npm install -g appium 
    ```

## Run the Script

1. **Connect your Android device** your device id needs to be replaced with line 10 in automation.py:
    ```
    adb devices 
    ```

2. **Start the Appium server**:
    ```
    appium --address 127.0.0.1 --port 4723 
    ```

3. **Run the automation script**:
    ```
    python src/automation.py 
    ```

## Code Explanation

The script follows steps below:
1. **Set capabilities**: Initially it defines the necessary capabilities to connect to the Android device and launch the bKash app.
2. **Handle location access popup**: Attempts to deny the location access popup by clicking "No thanks".
3. **Enter bKash PIN**: Tries to locate the PIN input field and send the PIN to the device. If it fails, the user must log in manually.
4. **Check Balance**: Once logged in, the script clicks on the "Tap for Balance" button and shows the balance amount.

## Limitations

- **Manual login required**: If the PIN input field doesn't work, the user must manually log in to the home page.

## Requirements.txt

```
Appium-Python-Client==4.0.0

```
