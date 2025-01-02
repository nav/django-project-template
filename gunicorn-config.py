import os
import pathlib

_cwd = pathlib.Path.cwd()
_flag = _cwd / "is_running"

bind = "0.0.0.0:8000"
workers = 2
loglevel = "info"
pythonpath = str(_cwd / "src")
reload = os.getenv("DEBUG", "False").lower() not in ("true", "1", "t")


# Server Hooks
def when_ready(server):
    print(f"Writing liveness check flag {_flag}")
    _flag.touch(mode=0o666, exist_ok=True)


def on_exit(server):
    print(f"Removing liveness check flag {_flag}")
    _flag.unlink()
