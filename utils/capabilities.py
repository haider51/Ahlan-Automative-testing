# utils/capabilities.py

def get_android_capabilities():
    return {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "My_Phone",
        
        # Ahlan App Details
        "appPackage": "net.ahlanmarket.app.dev",
        "appActivity": "net.ahlanmarket.app.MainActivity",
        
        "autoGrantPermissions": True,
        "appWaitActivity": "*",
        "newCommandTimeout": 300,
        "adbExecTimeout": 20000,
        "noReset": True
    }