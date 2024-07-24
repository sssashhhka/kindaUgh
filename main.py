import os


def start() -> None:
    pass


if os.name == "posix":
    start()
elif os.name == "nt":
    print("Program may have little problems on Windows")
else:
    exit("Sry ;(")
