try:
    from rich.console import Console
    from rich.markdown import Markdown
    from rich.traceback import install

    install()
    console = Console()
except ModuleNotFoundError:
    print(
        "Rich is not installed! Please install it using `pip install rich` and try again."
    )
    exit(1)
