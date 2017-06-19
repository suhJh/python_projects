def knights2(saying):
    def inner2():
        return "we are the knights who say: '%s'" % saying
    return inner2

a = knights2('first closure')
b = knights2('second closure')

a()
b()
