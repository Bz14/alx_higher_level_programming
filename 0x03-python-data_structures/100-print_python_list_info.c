#include <Python.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info - print information about python lists
 * @p: python list object
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p), i;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
		printf("Element %li: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
