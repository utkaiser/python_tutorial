cd <folder_dir>\Python_Tutorial\Teil_4_Testing\tutorial

#führt die Testfunktionen einzeln aus
python3 -m pytest my_tests.py::test_multiply_by_2_happypath
python3 -m pytest my_tests.py::test_multiply_by_2_parametrized_happypath
python3 -m pytest my_tests.py::test_multiply_by_2_extremepath