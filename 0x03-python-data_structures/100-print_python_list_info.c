#include <Python.h>

/**
  * print_python_list_info - Used to get py info
  * @p: python object
  */
void print_python_list_info(PyObject *p) {
	int i = 0, size;
	PyObject *item;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
