# unitest_test

This is a "hello world" example for testing out Python's unit test package unittest.
The tests are defined in  [tests](https://github.com/mojo00/unittest_test/tree/master/tests).
# Instructions
### Check out the respository.
```
git clone https://github.com/mojo00/unittest_test.git
```
### Create Virtual Environment
```
virtualenv unittest_test_env
source unittest_test_env/bin/activate
```
### Install Python Packages
```
  pip install -r requirements.txt
```

### Run the tests
```
python setup.py test
```
Expected output
```
running test
running egg_info
writing unittest_test.egg-info/PKG-INFO
writing top-level names to unittest_test.egg-info/top_level.txt
writing dependency_links to unittest_test.egg-info/dependency_links.txt
reading manifest file 'unittest_test.egg-info/SOURCES.txt'
writing manifest file 'unittest_test.egg-info/SOURCES.txt'
running build_ext
<module 'unittest' from '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/unittest/__init__.pyc'>
<module 'unittest' from '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/unittest/__init__.pyc'>
test_helloworld (tests.test0.Test0) ... ok
test_notequal (tests.test0.Test0) ... ok
test_notequal (tests.test1.Test1) ... ok
test_numpy (tests.test1.Test1) ... FAIL

======================================================================
FAIL: test_numpy (tests.test1.Test1)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/johnkwong/Documents/Code/unittest_test/tests/test1.py", line 15, in test_numpy
    self.assertFalse( np.all( np.zeros(2) == np.array([0., 0.] ) ) )
AssertionError: True is not false

----------------------------------------------------------------------
Ran 4 tests in 0.000s

FAILED (failures=1)
'''
