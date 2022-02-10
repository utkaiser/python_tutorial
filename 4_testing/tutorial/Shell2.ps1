cd <folder_dir>\Python_Tutorial\Teil_4_Testing\tutorial

python3 -m pytest -v --cov-report html:my_tests_results/py_cov.html --cov=<folder_dir>\Python_Tutorial\Teil_4_Testing\tutorial\my_functions --html=my_tests_results/py-test-results.html my_tests.py