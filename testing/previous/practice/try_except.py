import sys
def test():
    raise EOFError

try:
    test()
except:
    type, message, traceback = sys.exc_info()
    while traceback:
        print('..........')
        print(type)
        print(message)
        print('function or module？', traceback.tb_frame.f_code.co_name)
        print('file？', traceback.tb_frame.f_code.co_filename)
        traceback = traceback.tb_next