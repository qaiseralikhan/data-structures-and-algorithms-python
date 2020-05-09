# Must Read This Blog: https://realpython.com/how-to-implement-python-stack/
class Stack:
    def __init__(self, items):
        """
        pass a empty list or list of element
        """
        self.items = list(items)

    
    def pop(self):
        """
        Pop a element from stack
        """
        self.items.pop()
    
    def peek(self):
        """
        return a top element on stack
        """
        return self.items[len(self.items) - 1]
    
    def push(self, element):
        """
        Push any element on stack
        """
        self.items.append(element)
    
    def isEmpty(self):
        """
        Check stack is empty or not
        return True or False
        """
        return len(self.items) == 0
    
    def size(self):
        """
        return the size of stack 
        """
        return len(self.items)

def main():
    #  Stack Operation
    s=Stack([])
    print("Stack is Empty" , s.isEmpty())
    s.push(4)
    s.push('dog')
    print("Stack Peak ", s.peek())
    s.push(True)
    print(s.size())
    print(s.isEmpty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())
    print(s.items)


if __name__ == "__main__":
    main()