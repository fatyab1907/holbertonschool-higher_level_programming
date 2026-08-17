#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if "/tmp" not in sys.path:
        sys.path.append("/tmp")
    import hidden_4

    for name in sorted(dir(hidden_4)):
        if not name.startswith("__"):
            print(name)
