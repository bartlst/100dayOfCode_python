# fileNotFound

try:
    file = open("a_file.txt")
except FileNotFoundError:
    print("There was a error :O")

except KeyError as error_message:
    print(f"The key {error_message} does not exist.")

else:
    pass
finally:
    raise KeyError
