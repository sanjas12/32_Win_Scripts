from cx_Freeze import setup, Executable
import sys

# Основные настройки
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Для скрытия консоли (если нужно)

build_options = {
    "packages": ["pyautogui", "time"],
    "excludes": [
        "asttokens", "asyncio", "certifi", "chardet", "colorama", "comm", 
        "contourpy", "curses", "cycler", "dateutil", "debugpy", "distutils",
        "email", "executing", "fontTools", "greenlet", "html",
        "http", "iniconfig", "ipykernel", "IPython", "jedi",
        "jupyter_client", "jupyter_core", "kiwisolver", "lib2to3", "lxml",
        "matplotlib", "matplotlib_inline", "mouseinfo", "mpl_toolkits", "numpy",
        "pandas", "parso", "PIL", "pkg_resources", "platformdirs", "pluggy",
        "prompt_toolkit", "psutil", "pure_eval", "pydoc_data", "pyexpat",
        "pygments", "pymsgbox", "pyparsing", "pyperclip", "PyQt5", "pyrect",
        "pyscreeze", "pytest", "pytweening", "pytz", "pywin32_system32",
        "setuptools", "sqlalchemy", "sqlite3", "stack_data", "tomllib",
        "tornado", "traitlets", "unittest", "urllib", "wcwidth"
    ],
    "include_files": []
}

# Настройка сборки
setup(
    name="MouseMover",
    version="1.0",
    description="Автоматическое перемещение мыши каждые 10 минут",
    options={"build_exe": build_options},
    executables=[
        Executable(
            "mouse_mover.py",
            base=base,
            icon=None,
            target_name="MouseMover.exe"
        )
    ]
)