class CustomError(Exception): ...

try:
    file = open("a.txt")
except FileNotFoundError:
    print("FileNotFoundError")
except TypeError:
    print("TypeError")
else:
    print("No error")
finally:
    print("Closed file")
    raise CustomError
    file.close()
