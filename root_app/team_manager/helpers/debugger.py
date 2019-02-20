#!/usr/bin/env python
# -*- coding: utf-8 -*-

import platform
import sys
#from kitchen.text.converters import getwriter
import inspect
import re
import traceback

if platform.uname()[0].lower() !="windows":
    from blessings import Terminal
#else:
#    raise Exception("Your Platform is Windows which are not support colorful command line output! Please stop using functions from debugging.py")

from nose.plugins.attrib import attr
#from cached_property import cached_property

#UTF8Writer = getwriter('utf8')
#sys.stdout = UTF8Writer(sys.stdout)

t = Terminal()
colores = {'b':'t.bold_on_bright_blue', 'r':'t.bold_on_bright_red', 'g':'t.bold_on_bright_green', 'w':'t.bold_black_on_bright_white', 'm':'t.bold_white_on_bright_magenta', "c":'t.bold_white_on_bright_cyan', "y":'t.bold_white_on_bright_yellow', "b":'t.bold_white_on_bright_black'}
pattern = re.compile(r'\(\s?\((.*?)\).*\).*$')

def p(context_to_print, name_to_print='DEBUGING', c='w', r=False):
    '''
    Functionality: Print-Function for Debigging 
    '''
    try:
        context_to_print = context_to_print.decode("utf-8")
    except:
        pass

    if platform.uname()[0].lower() !="windows":
        #t = Terminal()
        #colores = {'b':'t.bold_on_bright_blue', 'r':'t.bold_on_bright_red', 'g':'t.bold_on_bright_green', 'w':'t.bold_black_on_bright_white', 'm':'t.bold_white_on_bright_magenta', "c":'t.bold_white_on_bright_cyan', "y":'t.bold_white_on_bright_yellow', "b":'t.bold_white_on_bright_black'}
        #colores = {'b':'t.bold_blue', 'r':'t.bold_red', 'g':'t.bold_green', 'w':'t.bold', 'm':'t.bold_magenta'}

        
        if isinstance(context_to_print, tuple):
            #p("tzui")
            stack = traceback.extract_stack()
            filename, lineno, function_name, code = stack[-2]
            #var_names = re.compile(r'\((.*?)\).*').search(code).groups()[0]
            var_names = pattern.search(code)
            if var_names:
                var_names = var_names.groups()[0]
                var_names = var_names.strip(" ").strip(",").strip(" ")
                #var_names = var_names.split("[")
                var_names = var_names.split(",")
                var_names = [var.strip(" ") for var in  var_names]
                #print var_names
                #print (context_to_print, var_names)
                if len(context_to_print)== len(var_names):

                    temp_elem_to_print = ""
                    for var_name,var_value in zip(var_names, context_to_print):
                        var_value = repr(var_value) if r else var_value
                        var_name = var_name if (("'" not in var_name) and ('"' not in  var_name)) else None
                        #temp_elem_to_print += "\n   {start}{var_name}{stop}  = '{var_value}'\n".format(var_name=var_name,var_value=var_value,t=t, start=t.bold_black_on_bright_white, stop=t.normal)
                        temp_elem_to_print += u"\n   {start}{var_name}{stop}  = {var_value}\n".format(var_name=var_name,var_value=var_value,t=t, start=t.bold_magenta, stop=t.normal)
                    if temp_elem_to_print:
                        r = False
                        #temp_elem_to_print = "\n" + temp_elem_to_print
                        context_to_print = temp_elem_to_print
                        #p(context_to_print)
                        #print context_to_print
                else:
                    #print()
                    print("ERROR(P): No right Number of extracted val_names")
                #else:
        #p()
        context_to_print =repr(context_to_print) if r else context_to_print 
        print(u"\n\n{start} <{0}>{stop}  \n  {1}  \n   {start} </{0}>{stop}\n".format(  name_to_print,  context_to_print, t=t, start=eval(colores[c]), stop=t.normal   ))

    else:
        print("p() is not supported for 'Windows'-OS.")




def wipd(f):
    '''
    decorator for nose attr.
    '''
    return attr('wipd')(f)

def wipdn(f): # now
    '''
    decorator for nose attr.
    '''
    return attr('wipdn')(f)

def wipdl(f): #later
    '''
    decorator for nose attr.
    '''
    return attr('wipdl')(f)

def wipdo(f): # open
    '''
    decorator for nose attr.
    '''
    return attr('wipdo')(f)

# def cached(timeout=None):
#     def decorator(func):
#         def wrapper(self, *args, **kwargs):
#             value = None
#             key = '_'.join([type(self).__name__, str(self.id) if hasattr(self, 'id') else '', func.__name__])

#             if settings.CACHING_ENABLED:
#                 value = cache.get(key)

#             if value is None:
#                 value = func(self, *args, **kwargs)

#                 if settings.CACHING_ENABLED:
#                     # if timeout=None Django cache reads a global value from settings
#                     cache.set(key, value, timeout=timeout)

#             return value

#         return wrapper

#     return decorator



# def cachedproperty(func):
#     " Used on methods to convert them to methods that replace themselves\
#         with their return value once they are called. "

#     def cache(*args):
#         self = args[0] # Reference to the class who owns the method
#         funcname = func.__name__
#         ret_value = func(self)
#         setattr(self, funcname, ret_value) # Replace the function with its value
#         return ret_value # Return the result of the function

#     return property(cache)


# def p(func):
#     def func_wrapper(name):
#         return "<\n{0}>{1}</{0}\n>".format(func.__name__, func(name))
#     return func_wrapper


# def markup(func):
#   def func_wrapper(name):
#       return "<\n{0}>{1}</{0}\n>".format(func.__name__, func(name))
#   return func_wrapper



