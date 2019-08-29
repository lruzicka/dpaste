import pytest
import dpaste as dp


def init_parser():
    argparser = dp.Parser()
    return argparser

def get_args(arguments):
    parser = init_parser()
    return parser.provide_arguments(arguments)

def init_dpaste(arguments):
    args = get_args(arguments)
    app = dp.Dpaster('https://dpaste.de/api/', args)
    return app

def test_check_parser():
    arguments = get_args(['-f','file.in','-l','python','-e','week', '-c', 'Hej'])
    if arguments:
        value = True
    else:
        value = False
    assert value == True

def test_check_api():
    app = init_dpaste([])
    assert app.api == 'https://dpaste.de/api/'

def test_convert_time_hour():
    app = init_dpaste(['-e','hour'])
    app.convert_time()
    assert app.expiry == 3600

def test_convert_time_week():
    app = init_dpaste(['-e','week'])
    app.convert_time()
    assert app.expiry == 604800

def test_convert_time_month():
    app = init_dpaste(['-e','month'])
    app.convert_time()
    assert app.expiry == 2592000

def test_convert_time_never():
    app = init_dpaste(['-e','never'])
    app.convert_time()
    assert app.expiry == 'never'

def test_convert_time_day():
    app = init_dpaste(['-e', 'day'])
    app.convert_time()
    assert app.expiry == 86400

def test_get_paste_content():
    app = init_dpaste(['-c', 'TestLine'])
    app.get_paste()
    assert app.content == 'TestLine'

def test_get_paste_file():
    app = init_dpaste(['-f', 'testfile'])
    app.get_paste()
    with open('./testfile') as infile:
        fcontent = infile.readlines()[0]
    assert app.content == fcontent

#def test_convert_time():
#    app = init_dpaste()
#    app.args.expire = 'hour'
#    seconds = app.convert_time()
#    assert seconds == 3600
#
#def test_sum():
#    assert sum([1, 2, 3]) == 6, "Should be 6"
