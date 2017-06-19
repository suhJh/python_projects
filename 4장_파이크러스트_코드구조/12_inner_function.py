def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

return_value = outer(4, 7)
print(return_value)



def knights(saying):
    def inner(quote):
        return "we are the knight who say: '%s'" % quote
    return inner(saying)

print(knights('Ni!'))


