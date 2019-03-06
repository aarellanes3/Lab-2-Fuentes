# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 12:22:56 2019

@author: aarel
"""
#Andres Arellanes, Dr. Olac Fuentes, Anindita Nath 
import random

class Node(object):
    # Constructor
    def __init__(self,item,next=None):  
        self.item = item
        self.next = next 
        
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None

def element_at(L, pos):
    count = 0
    temp = L.head
    while temp is not None:
        if count == pos:
            return temp.item
        count +=1
        temp = temp.next       
    print("item not found")

def IsEmpty(L):
    return L.head == None
        
def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line 
    
def Append(L,x): 
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next

def get_length(L):
    counter = 0
    temp = L.head
    while temp is not None:
        counter += 1
        temp = temp.next
    return counter

def random_number_list(n):
    L = List()
    for i in range(n):
        num = random.randint(1,101)
        Append(L,num)
    return L

def Copy(L):
    temp = L.head
    copied = List()
    while temp is not None:
        Append(copied,temp.item)
        temp = temp.next
    return copied

def Median(L):
    C = Copy(L)
    return element_at(C,get_length(C)//2)

def bubble_sort(L):
   count = 0
   change = True
   while change:
       t = L.head
       change = False
       count += 1
       while t.next is not None:
           if t.item > t.next.item:       
               x = t.item
               t.item = t.next.item
               t.next.item = x
               change = True
               count += 1
           t = t.next
   Print(L)

def merge_sort(L):       
    L1 = List()
    L2 = List()
    
    temp = L.head
    if get_length(temp)//2 < 1:
        print(temp)
        return None
    if temp is None:
        return 0
    if get_length(temp)//2 == 1:
        return temp
    else:
        return merge_sort(temp.next)
    
    temp2 = L.head
    while temp2 is not None:
        if temp2.next is None:
            Append(L2, temp2.item)
        if get_length(temp2)//2 > get_length(temp2):
            Append(L1,temp2.item)
        else:
            Append(L2, temp.item) 
    if get_length(L1)>1:
        L1 = Append(L1,merge_sort(L1))
    if get_length(L2)>1:
        L2 = Append(L2,merge_sort(L2))
       
    temp3 = L1.head
    temp4 = L2.head
    Sorted = List()
       
    if temp3 is None and temp4 is None:
        return Sorted
    if temp3 is None:
        Append(Sorted,temp2.item)
        temp4 = temp4.next
    if temp4 is None:
        Append(Sorted, temp4.item)
        temp3 = temp3.next
    if temp3.item < temp4.item:
        Append(Sorted, temp3.item)
        temp3 = temp3.next
    if temp4.item < temp3.item:
        Append(Sorted,temp4.item)
        temp4 = temp4.next
    return Sorted


L = List()
L = random_number_list(3)
Print(L)
bubble_sort(L)
print(Median(L))
print(" ")
L2 = List()
L2 = random_number_list(4)
Print(L2)
merge_sort(L2)