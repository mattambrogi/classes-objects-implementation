## Implementing Classes and Objects in Python

This program is an approximate implementation of classes and objects in Python. This implementation is based on Chapter 2.6 from the textbook [Composing Programs](composingprograms.com). We implement classes as if they were not built into Python by using dispatch dictionaries. 

Rough flow of the program
* A class defined and finally made through the make_class call as can be seen in account.py. A class, which is a dispatch dictionary, is returned.
* If new is called within any class, init_instance is called.
* init_instance then calls make_instance and then calls the __init__ method from the new class which is itself just a dispatch dictionary. 
* make_instance relies on bind_method for automatic binding of any methods called by the instance to the instance.


