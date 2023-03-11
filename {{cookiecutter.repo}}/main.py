from waggle.plugin import Plugin


def main():
    with Plugin() as plugin:
        print("This is the start of an amazing app!")


if __name__ == "__main__":
    main()
