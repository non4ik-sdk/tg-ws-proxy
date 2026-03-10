import ctypes

def show_error(text: str, title: str = "TG WS Proxy — Ошибка") -> None:
    ctypes.windll.user32.MessageBoxW(0, text, title, 0x10)


def show_info(text: str, title: str = "TG WS Proxy") -> None:
    ctypes.windll.user32.MessageBoxW(0, text, title, 0x40)