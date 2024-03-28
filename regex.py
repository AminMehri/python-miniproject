import re

string = 'amin mehri'

# print('amin' in string)

specific_string = 'meh'
meh_index = string.index(specific_string)    # rise -1 when charactor isn't exist
print(string.find(specific_string))   #  rise error when charactor isn't exist
print(string[5:len(specific_string)])

# res = re.search('min', string)
# print(res.group())

# if re.search('mehr', string):
#     print('i found it')
# else:
#     print('there is not such a thing')

another_string = 'aminem123456789hosseiny'
# res = re.search('\d\d\d', another_string)
# print(res.group())

# res = re.search('1...5', another_string)
# print(res.group())

# res = re.search('ami[nr]', another_string)
# print(res.group())

# res = re.search('[^0-9]', another_string)
# print(res)
# res = re.search('[^a-z]', another_string)
# print(res)

# res = re.search('\s', 'foo\nbar baz')
# print(res)
# print(res.span())

# res = re.search('\S', '  \n foo  \n  ')
# print(res)

# res = re.search('[\d\w\s]', '--- ---')
# print(res)
# res = re.search('[\d\w]', '--- ---')
# print(res)

# res = re.search('.', 'foo.bar')
# print(res)
# res = re.search('\.', 'foo.bar')
# print(res)

# res = re.search('\\', 'amin\mehri')
# print(res)
# res = re.search('\\\\', 'amin\mehri')
# print(res)
# res = re.search(r'\\', 'amin\mehri')
# print(res)
# res = re.search(r'\\\\', 'amin\mehri')
# print(res)

#   note: \A like ^   and    \Z like $  but there is a diffrent between them
# res = re.search('bar$', 'foobar\n')
# print(res)
# res = re.search('bar\Z', 'foobar\n')
# print(res)

# note: \b detect words
# res = re.search(r'\bbar', 'foo bar')
# print(res)
# res = re.search(r'\bbar', 'foo.bar')
# print(res)
# res = re.search(r'\bbar', 'foobar')
# print(res)

# res = re.search(r'\bbar\b', 'foo bar baz')
# print(res)
# res = re.search(r'\bbar\b', 'foo barbaz')
# print(res)
# res = re.search(r'\bbar\b', 'foobar baz')
# print(res)

# note \B is opposite \b
# res = re.search(r'\Bfoo\B', 'barfoobaz')
# print(res)

# note: match find something at the beginning of the string.
#       but search find something anywhere in the string.
# res = re.search('^ab', 'abcde')
# print(res)
# res = re.match('^ab', 'abcde')
# print(res)
# res = re.search('bc', 'abcde')
# print(res)
# res = re.match('bc', 'abcde')
# print(res)

# res = re.search('<.*>', '%<foo> <bar> <baz>%')
# print(res)
# res = re.search('<.*?>', '%<foo> <bar> <baz>%')
# print(res)
# res = re.search('<.+>', '%<foo> <bar> <baz>%')
# print(res)
# res = re.search('<.+?>', '%<foo> <bar> <baz>%')
# print(res)
# res = re.search('ba?', 'baaaa')
# print(res)
# res = re.search('ba??', 'baaaa')
# print(res)

# res = re.search('x-{3}x', 'x---x')   
# print(res)

# for i in range(1, 8):
#     s = f"x{'-' * i}x"
#     res = re.search('x-{3,5}x', s)
#     print(res)

# res = re.search('a{3,5}', 'aaaaaaaa')
# print(res)
# res = re.search('a{3,5}?', 'aaaaaaaa')
# print(res)

# res = re.search('(bar)+', 'foo bar baz')
# print(res)
# res = re.search('(bar)+', 'foo barbar baz')
# print(res)
# res = re.search('(bar)+', 'foo barbarbarbar baz')
# print(res)

# res = re.search('(ba[rz]){2,4}(qux)?', 'bazbarbazqux')
# print(res)

# res = re.search('(foo(bar)?)+(\d\d\d)?', 'foofoobar')
# print(res)
# res = re.search('(foo(bar)?)+(\d\d\d)?', 'foofoobar123')
# print(res)
# res = re.search('(foo(bar)?)+(\d\d\d)?', 'foofoo123')
# print(res)

# res = re.search('(\w+),(\w+),(\w+)', 'foo,ques,bars')
# print(res)
# print(res.groups())
# print(res.group(1))
# print(res.group(2))
# print(res.group(3))
# print(res.group(3, 2))
# print(res.group(1, 3, 2))

# note: The following effectively does the same thing except that 
#       the groups have the symbolic names w1, w2, and w3
# res = re.search('(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)', 'foo,quux,baz')
# print(res.groups())
# print(res.group('w1'))
# print(res.group('w2'))

