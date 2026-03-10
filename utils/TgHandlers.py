import ctypes

def open_tg_url(url: str) -> None:
    SW_HIDE = 0
    result = ctypes.windll.shell32.ShellExecuteW(None, "open", url, None, None, SW_HIDE)
    if result <= 32:
        raise OSError(f"ShellExecuteW failed with code {result}")