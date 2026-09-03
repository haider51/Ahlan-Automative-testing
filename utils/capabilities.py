def get_android_capabilities():
    return {
        "platformName": "Android",
        # THE ENGINE CHANGE: UiAutomator2 -> Flutter
        "automationName": "Flutter",
        "deviceName": "My_Phone",
        
        # Ahlan App Details (Make sure to use the debug APK in real tests!)
        "appPackage": "net.ahlanmarket.app.dev",
        "appActivity": "net.ahlanmarket.app.MainActivity",
        
        "autoGrantPermissions": True,
        "newCommandTimeout": 300,
        "adbExecTimeout": 20000,
        "noReset": True,
        "forceAppLaunch": True
    }