import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
initial_list = ['hello', 'World']
lib.print_python_list_info(initial_list)
modefied_list = initial_list.copy()
del modefied_list[1]
lib.print_python_list_info(modefied_list)
extended_list = modefied_list + [4, 5, 6.0, (9, 8), [9, 8, 1024], "Holberton"]
lib.print_python_list_info(extended_list)
empty_liste = []
lib.print_python_list_info(empty_list)
single_element_list = []
single_element_list.append(0)
lib.print_python_list_info(single_element_list)
multi_element_list = single_element_list + [1, 2, 3, 4]
lib.print_python_list_info(multi_element_list)
multi_element_list.pop()
lib.print_python_list_info(multi_element_list)
