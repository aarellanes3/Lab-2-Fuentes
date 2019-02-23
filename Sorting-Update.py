# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 14:40:34 2019

@author: aarel
"""
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
    
def prepend(L,x):
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.head = Node(x,L.head)
    
def get_length(L):
    counter = 0
    temp = L.head
    while temp.next is not None:
        counter += 1
        temp = temp.next
        return counter

def random_number_list(n):
    L = List()
    for i in range(n):
        num = random.randint(1,101)
        Append(L,num)
    Print(L)
    return L
        
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
        
def element_at(L, pos):
    count = 0
    temp = L.head
    while temp is not None:
        if count == pos:
            return temp.item
        count +=1
        temp = temp.next       
    print("item not found")
            
def Copy(L):
    temp = L.head
    copied = temp
    while temp.next is not None:
        copied = Node(temp.item)
        temp = temp.next
        copied = copied.next
    return copied

def Median(L):
    C = Copy(L)
    return C.element_at(C,C.get_length(C)//2)

def merge_sort(L):
    count = 0
    nl = get_length(L)
    if nl == 0:
        count +=1
        return 
    if nl == 1:
        count +=1
        return L
    
    
    nwl = nl//2
    L1 = List() 
    L2 = List()
    temp = L.head
    for i in range(nwl):    
        Append(L1,temp.item)
        temp = temp.next
    while temp.next is not None:
        Append(L2, temp.item)
        temp = temp.next
    L1 = merge_sort(L1)
    L2 = merge_sort(L2)
    
    temp1= L1.head
    temp2= L2.head
    Sorted = List()
    if temp1.item > temp2.item:
        Append(Sorted, temp2.item)
        count +=1
        temp2 = temp2.next
    if temp1.item is None: 
        Append(Sorted, temp2.item)
        count+=1
        temp2 = temp2.next
    if temp2.item is None:
        Append(Sorted, temp1.item)
        count += 1
        temp1 = temp1.next
    if temp1.item < temp2.item:
        Append(Sorted, temp1.item)
        count+=1
        temp1 = temp1.next
    
    middle = Median(Sorted)
    print(count)
    return middle
    
       
def quick_sort(L):
    Left = List()
    Right = List()
    nl = get_length(L)
    if nl == 1:
        return L
    if nl == 0:
        return
    
    temp = L.head
    pivot = temp
    while temp.next is not None:
        if temp.item < pivot:
            Append(Left, temp.item)
        if temp.item > pivot:
            Append(Right, temp.item)
        temp = temp.next
    Left = quick_sort(Left)
    Right = quick_sort(Right)
    
    Sorted = List()
    NewL = Append(Left,pivot)    
    Sorted = Append(NewL,Right) 
    middle = Median(Sorted)
    Print(L)
    return element_at(middle)
    
def alt_sort(L):
    Left = List()
    Right = List()
    nl = get_length(L)
    if nl == 1:
        return L
    if nl == 0:
        return
    
    temp = L.head
    pivot = temp
    while temp.next is not None:
        if temp.item < pivot:
            Append(Left, temp.item)
        if temp.item >= pivot:
            Append(Right, temp.item)
        temp = temp.next
        
    if get_length(Left) > get_length(Right):
        Left = alt_sort(Left)
        middle1 = Median(Left)
        Print(Left)
        return middle1
    if get_length(Left) < get_length(Right):
        Right = alt_sort(Right)
        middle2 = Median(Right)
        Print(Right)
        return middle2
        
    
L = List()    
L = random_number_list(3)
L2 = random_number_list(3)
L3 = random_number_list(3)
L4 = random_number_list(3)

bubble_sort(L)
merge_sort(L2)
quick_sort(L3)
alt_sort(L4)