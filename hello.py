def greet(name=None):
    if name is None:
        return "Hello, Git collaboration!"
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet())
