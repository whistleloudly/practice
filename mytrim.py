def trim(s):
	string = ''
	l = len(s)
	for n in range(l):
		if s[n]==' ':
			n = n+1
			string=s[n:]
		else:
			break

	for n in range(len(string)):
		if string[n]==' ':
			return string[:n]

                    # 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
