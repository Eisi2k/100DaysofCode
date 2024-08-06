#functions


def greeting():
    print("Hello")
    print("Hello")
    print("Hello")


greeting()

def greeting_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")
    print("Hello")

greeting_with_name("Philipp")

#functions with more than 1 input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What ist is lie in {location}")

greet_with("Philipp", "Nowhere")

greet_with("nowhere", "Philipp")


greet_with(location="nowhere", name="Philipp")