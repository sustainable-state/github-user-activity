import sys
from github_cli import CLI


def main():
    CLI().run(sys.argv)


if __name__ == "__main__":
    main()