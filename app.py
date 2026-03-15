def greet(name):
    return f"Hello, {name}! Welcome to the cloud."

def farewell(name):
    return f"Goodbye, {name}! See you in the cloud."

if __name__ == "__main__":
    user = input("Enter your name: ")
    print(greet(user))
    print(farewell(user))
