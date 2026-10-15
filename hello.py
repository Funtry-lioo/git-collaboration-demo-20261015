def greet(name=None):
    cleaned = name.strip() if name is not None else ""
    if not cleaned:
        return "Hello, Git collaboration!"
    return f"Hello, {cleaned}!"


if __name__ == "__main__":
    print(greet())
