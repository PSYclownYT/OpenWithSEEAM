import winreg

def register_url_scheme(scheme, app_path):
    key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Classes\{}".format(scheme))
    winreg.SetValueEx(key, "", 0, winreg.REG_SZ, "URL: {}".format(scheme))
    winreg.SetValueEx(key, "URL Protocol", 0, winreg.REG_SZ, "")
    winreg.SetValueEx(key, "DefaultIcon", 0, winreg.REG_SZ, app_path)

    command_key = winreg.CreateKey(key, r"shell\open\command")
    winreg.SetValueEx(command_key, "", 0, winreg.REG_SZ, '"{}" "%1"'.format(app_path))

    winreg.CloseKey(command_key)
    winreg.CloseKey(key)

register_url_scheme("myapp", r"C:\path\to\your\app.exe")