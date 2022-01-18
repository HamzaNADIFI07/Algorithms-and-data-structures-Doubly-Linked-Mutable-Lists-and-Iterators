# -*- coding: utf-8 -*-

"""
Module that implements lists with iterator interaction

Provides constructor, selectors and modifiers for mutable lists.
Lists of this module must be traversed via iterators. 

An iterator for lists allows the programmer to traverse the list in
either direction and adding elements to the list during iteration.  

An iterator has no current element; its cursor position always lies
between the element that would be returned by a call to `previous` and
the element that would be returned by a call to `next`. 

An iterator for a list of length `n` has `n+1` possible cursor positions,
as illustrated by the carets (`^`) below:

```

                      Element(0)   Element(1)   Element(2)   ... Element(n-1)
 cursor positions:  ^            ^            ^            ^                  ^
```

Note: Author
      [Dpt Informatique - FST - Univ. Lille](http://portail.fil.univ-lille1.fr)
      2021, february

"""

class EmptyList (Exception):
    """
    Exception for empty lists
    """
    def __init__ (self,msg):
        self.message = msg

class NoSuchElementException (Exception):
    """
    Exception for iterators not positionned
    """
    def __init__ (self,msg):
        self.message = msg

            
class List:
    '''
    Double-linked lists
    '''
    
    class Cell:
        '''
        Double-linked cells
        '''
        
        def __init__(self, value, next_cell, prev_cell):
            '''
            Creates a new cell with the specified values, and the links
            to the next and previous cells (if any).

            Args:
              value (any): A value
              next_cell (Cell): The successor of this cell, if any or `None` otherwise
              prev_cell (Cell): The predecessor of this cell, if any or `None` otherwise
            '''
            self.value = value
            self.next = next_cell
            self.prev = prev_cell

        def __print_without_iterator_forward (self):
            """
            Print all the list from the cell until the end
            """
            print(self.value, end=' ')
            if self.next != None:
                self.next.__print_without_iterator_forward ()
            else:
                print()

        def __print_without_iterator_reversed (self):
            """
            Print all the list from the cell back to the beginning of the list
            """
            pass

    def __init__ (self):
        """
        Creates a new empty list.
        """    
        self.head = None
        self.tail = None

    def is_empty (self):
        """
        Returns:
          bool: `True` if the list is empty, `False` otherwise.
        """
        return self.head == None and self.tail == None

    def cons (self, value):
        """
        Add the value `value` at the begining of the list
        
        Args:
          value (any): The value to be added.

        Warning: Pre-condition
                 Cannot be used with iterators
        """
        if self.head == None:
            self.head = self.tail = List.Cell(value, None, None)
        else:
            self.head = List.Cell(value, self.head, None)
            self.head.next.prev = self.head



    def print (self,reverse=False):
        """
        Args:
          reverse (bool): `True` if the the current list must be printed from the end to the beginning
        """
        if self.is_empty():
            raise EmptyList("The list has no elements")
        if reverse:
            self.tail._Cell__print_without_iterator_reversed()
        else:
            self.head._Cell__print_without_iterator_forward()


    def get_listiterator (self):
        """
        Creates a new iterator for the list

        Returns:
          ListIterator: An iterator at the beginning of the list
        """
        return List.ListIterator(self)


    class ListIterator:
        '''
        Iterator over double-linked lists
        '''
        
        def __init__(self, list):
            '''
            Builds a ListIterator on the provided list.
            The iterator is at the beginning of the list.

            Args:
              list (List): The list to iterate on
            '''

            # Beware! Your attributes cannot have the same names as the class methods.
            pass
                
        def hasNext (self):
            """
            Returns:
              bool: `True` if this list iterator has more elements when
                     traversing the list in the forward direction. 
                     (In other words, returns `True` if `self.next()` would
                     return an element rather than throwing an exception.)
            """
            pass


        def next (self):
            """
            Returns:
              the next element in the list and advances the cursor
              position. This method may be called repeatedly to iterate through
              the list, or intermixed with calls to `self.previous()` to go back
              and forth. (Note that alternating calls to next and previous will
              return the same element repeatedly.)

            Raises:
              NoSuchElementException: if there is no such element
            """
            pass

        def hasPrevious (self):
            """
            Returns: 
              bool: `True` if this list iterator has more elements when
              traversing the list in the reverse direction. (In other words,
              returns `True` if `self.previous()` would return an
              element rather than throwing an exception.)
            """
            pass

        def previous (self):
            """
            Returns:
              the previous element in the list and moves the cursor
              position backwards. This method may be called repeatedly to
              iterate through the list backwards, or intermixed with calls to
              `self.next()` to go back and forth. (Note that alternating 
              calls to next and previous will return the same element repeatedly.)
            
            Raises:
              NoSuchElementException: if there is no such element
            """
            pass
        
        def add (self,value):
            """
            Inserts the specified element into the list. The element is
            inserted immediately before the element that would be returned by
            `next()`, if any, and after the element that would be returned by
            `previous()`, if any. (If the list contains no elements, the new
            element becomes the sole element on the list.) The new element is
            inserted before the implicit cursor: a subsequent call to `next()`
            would be unaffected, and a subsequent call to `previous()` would
            return the new element.
            
            Args:
              value (any): The element
            """
            pass

        def remove (self):
            """
            Removes from the list the last element that was returned by
            `next()`. This call can only be made once per call to `next()`.
            """
            pass
