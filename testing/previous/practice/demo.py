import sys
def test():
    raise EOFError
try:
    raise EOFError
except EOFError as e:
    print( 'got it')
    raise ImportError from e