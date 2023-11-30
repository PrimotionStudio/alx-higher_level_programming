#!/usr/bin/python3
if __name__ == "__main__":
    import dis
    import marshal
    with open("hidden_4.pyc", "rb") as file:
        _ = file.read(16)
        bytecode = marshal.load(file)
        names = set()
        for code in dis.get_instructions(bytecode):
            if code.opname == "STORE_NAME":
                names.add(code.argval)
        for name in sorted(names):
            if (name[0:2] != '__'):
                print(name)
