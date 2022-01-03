#include "Python.h"
#include "swmm5.h"
#include "autocache.h"

const char *INPUT_FILE="swmm.inp";
const char *OUTPUT_FILE="swmm.out";
const char *REPORT_FILE="swmm.rpt";

static PyObject* run_swmm(PyObject *self, PyObject *args) {

    char *inp = NULL;

    if(!PyArg_ParseTuple(args, "s", &inp)){
        return NULL;
    }

    update_cached_file(INPUT_FILE, inp, strlen(inp));
    swmm_run(INPUT_FILE, REPORT_FILE, OUTPUT_FILE);

    struct CachedFile *output_contents = get_cached_file(OUTPUT_FILE, "r");
    struct CachedFile *report_contents = get_cached_file(REPORT_FILE, "r");
    update_len_cached_file(output_contents);
    update_len_cached_file(report_contents);
    PyObject *python_output_file = PyBytes_FromStringAndSize(output_contents->data, output_contents->size);
    PyObject *python_report_file = PyUnicode_FromStringAndSize(report_contents->data, report_contents->size);
    return PyTuple_Pack(2, python_output_file, python_report_file);
}

PyDoc_STRVAR(run_swmm_doc, "Docstring for run_swmm function.");

static struct PyMethodDef module_functions[] = {
    {"run_swmm", run_swmm, METH_VARARGS, run_swmm_doc},
    {NULL, NULL}
};
static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "swmm_cached._swmm_cached", /* m_name */
    NULL,             /* m_doc */
    -1,               /* m_size */
    module_functions, /* m_methods */
    NULL,             /* m_reload */
    NULL,             /* m_traverse */
    NULL,             /* m_clear */
    NULL,             /* m_free */
};

static PyObject* moduleinit(void) {
    PyObject *module;


    module = PyModule_Create(&moduledef);


    if (module == NULL)
        return NULL;

    return module;
}

PyMODINIT_FUNC PyInit__swmm_cached(void) {
    init_cache();
    return moduleinit();
}

