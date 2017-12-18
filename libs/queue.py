#!/usr/bin/python3

class Queue:
     def __init__(self):
         self.items = []
    
     def show(self):
        return self.items

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         print("Push item:", item)
         self.items.insert(0, item)

     def pop(self):
         item = self.items.pop()
         print("Pop item:", item)
         return item

     def peek(self):
         if self.isEmpty():
             return None
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
