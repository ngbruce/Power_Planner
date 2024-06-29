import winreg

def delete_sub_keys(hkey, sub_key):
    try:
        open_key = winreg.OpenKey(hkey, sub_key, 0, winreg.KEY_READ | winreg.KEY_WRITE)
        while True:
            try:
                sub_sub_key = winreg.EnumKey(open_key, 0)
                printf(f"{sub_key}\\{sub_sub_key}")
                delete_sub_keys(hkey, f"{sub_key}\\{sub_sub_key}")
            except OSError:
                break
        winreg.CloseKey(open_key)
        winreg.DeleteKey(hkey, sub_key)
    except FileNotFoundError:
        pass

def delete_keys_with_prefix(base_key, key_path, prefix):
    try:
        with winreg.OpenKey(base_key, key_path, 0, winreg.KEY_READ | winreg.KEY_WRITE) as key:
            i = 0
            while True:
                try:
                    sub_key_name = winreg.EnumKey(key, i)
                    if sub_key_name.startswith(prefix):
                        delete_sub_keys(base_key, f"{key_path}\\{sub_key_name}")
                    else:
                        i += 1
                except OSError:
                    break
    except FileNotFoundError:
        print(f"Key not found: {key_path}")
        pass

if __name__ == "__main__":
    base_key = winreg.HKEY_LOCAL_MACHINE
    key_path = r"SOFTWARE\Classes\Installer\Products"
    prefix = "7D2F3875100"
    
    delete_keys_with_prefix(base_key, key_path, prefix)
