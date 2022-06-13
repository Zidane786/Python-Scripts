# we are going to create our own range() method
# range() method is an iterator
# iterable are not iterator BUT iterator are iterable


class MyRange:

    def __init__(self, start, end) -> int:
        self.value = start
        self.end = end

    def __iter__(self):
        """
        Creating __iter__() so our MyRange is iterable
        for our MyRange to be iterator, __iter__() has to return iterator
        i.e: it has to return an object that has __next__()
        since we will create __next__() in this class we will return the same object(i.e self)
        """
        return self

    def __next__(self):
        if self.value > self.end:  # since range() exclude end value so our custom method will also exclude end value
            raise StopIteration  # it value > end than we will raige StopIteration Error
        current = self.value # storing current self.value
        self.value += 1 # increment the value
        return current
    
# as we can see below our own range() is been created
for i in MyRange(1, 10):
    print(i)

