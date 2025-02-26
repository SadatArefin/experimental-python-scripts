import contextlib
import os

@contextlib.contextmanager
def my_context():
    print('Enter')
    yield
    print('Exit')

with my_context() as x:
    print('Inside')

@contextlib.contextmanager
def in_dir (dir):
    original_dir = os.getcwd()
    os.chdir(dir)
    yield
    os.chdir(original_dir)

with in_dir('dist'):
    print(os.listdir())