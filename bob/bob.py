#
# Skeleton file for the Python "Bob" exercise.
#


def hey(what):
    ans = ''
    what = what.rstrip()
    if what.isspace() or what == '':
        return 'Fine. Be that way!'
    if what.endswith('?'):
        ans = 'Sure.'
    if what.isupper():
        ans = 'Whoa, chill out!'
    if ans=='':
        ans = 'Whatever.'
    return ans
