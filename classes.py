
"""
Make class.
If new called from any class, init instance called.
Init instance then calls make_instance and calls __init__ method of newly created instance. 
make__instance relies on bind_method for automatic binding of called methods to the instance. 
"""

def make_instance(cls):
  """ Return a new object instance, which is a dispatch dictionary"""
  def get_value(name):
    # First checks instance then class attributes
    if name in attributes:
      return attributes[name]
    else:
      value = cls['get'](name)
      return bind_method(value, instance)
  def set_value(name, value):
    attributes[name] = value
  attributes = {}
  instance = {'get': get_value, 'set': set_value}
  return instance

def bind_method(value, instance):
  """Return a bound method if value is callable, or value otherwise.
  If a method is called, self will be bound to the value of instance. If called on noncallable value, just returns value."""
  if callable(value):
    def method(*args):
      return value(instance, *args)
    return method
  else:
    return value

def make_class(attributes, base_class=None):
  """Return a new class, which is a dispatch dictionary.
  We pass no base_class although Python classes do inherit from the Class called type."""
  def get_value(name):
    # Checks if exists in class, else base class
    if name in attributes:
      return attributes[name]
    elif base_class is not None:
      return base_class['get'](name)
  def set_value(name, value):
    attributes[name] = value
  def new(*args):
    return init_instance(cls, *args)
  cls = {'get' : get_value, 'set' : set_value, 'new' : new}
  return cls

def init_instance(cls, *args):
  """Return a new object with type cls, initialized with args.
  Makes instance, then calls instance __init__ method."""
  instance = make_instance(cls)
  init = cls['get']('__init__')
  if init:
    init(instance, *args)
  return instance


