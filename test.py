def f(fun, *args, **kwargs):
        print 'this is a'
        fun(*args, **kwargs)
@f
def g():
        print 'this is b'


class vimi(object):
        def __init__(self,module):
                print 'class is init'

