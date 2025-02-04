import os

class Sample1:
    
    def __init__(self):
        self.some_var = "some_var"
    
    def hello_world(self):
        return os.environ.get('HELLO_STRING', "Hello, World!")
    
    def get_some_var(self):
        return self.some_var

if __name__ == "__main__":
    sample = Sample1()
    print(sample.hello_world())
    print(sample.get_some_var())