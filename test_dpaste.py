import pytest
import dpaste as dp


def init_parser():
    argparser = dp.Parser()
    return argparser

def get_args():
    parser = init_parser()
    return parser.provide_arguments

def init_dpaste():
    arguments = get_args()
    app = dp.Dpaster('https://dpaste.de/api/', arguments)
    return app

def test_check_parser():
    arguments = get_args()
    if arguments:
        value = True
    else:
        value = False
    assert value == True

def test_check_api():
    app = init_dpaste()
    assert app.api == 'https://dpaste.de/api/'

#def test_convert_time():
#    app = init_dpaste()
#    app.args.expire = 'hour'
#    seconds = app.convert_time()
#    assert seconds == 3600
#
#def test_sum():
#    assert sum([1, 2, 3]) == 6, "Should be 6"
