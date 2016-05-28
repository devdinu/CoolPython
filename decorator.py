class Meta:
    method_counts = {}
    max_value = 0

    @staticmethod
    def called(f):
        Meta.method_counts[f.__name__] = Meta.method_counts.get(f.__name__, 0) + 1

    @classmethod
    def get_method_count(cls, f = None):
        return cls.method_counts.get(f)

    @classmethod
    def update_max_val(cls, f, *args):
        if args:
            cls.max_value = max(args[0], cls.max_value)

    @staticmethod
    def get_arguments_as_doc(f):
        doc = "This method is decorated!\nIt takes %d arguments [" % f.func_code.co_argcount
        doc += " , ".join(f.func_code.co_varnames) + "].\n"
        if f.__doc__:
            doc += "User Defined Doc: " + f.__doc__
        return doc

def cool(f):

    def decorated_function(*args):
        # print("You Are Using A Decorated function")
        Meta.called(f)
        Meta.update_max_val(f, args)
        return f(*args)

    decorated_function.__doc__ = Meta.get_arguments_as_doc(f)
    return decorated_function



@cool
def increment(num, inc_val=1):
    return num + inc_val

newly_decorated_function = cool(increment)

@cool
def decrement(num):
    """decrements a number by 1"""
    return num - 1;

increment(1)
print(increment.__doc__)
increment(20)
increment(3)

print(increment.__doc__)
print(decrement.__doc__)

decrement(0)
decrement(2)

print(Meta.method_counts)
# print(increment.__module__)

