"""ToDo entry point script."""
# app/__main__.py

from app import cli, __app_name__

def main():
    cli.app(prog_name=__app_name__)

if __name__ == "__main__":
    main()