# Section 02-1
# Print 구문의 이해

# 기본 출력
print('Hello Python!')
print("Hello Python!")
print('''Hello Python!''')
print("""Hello Python!""")
print()

# Separator 옵션
print('T', 'E', 'S', 'T', sep='')
print('2019', '02', '19', sep='-')
print('niceman', 'google.com', sep='@')

# end 옵션
print('Welcome To', end=' ')
print('the black parade', end=' ')
print('piano notes')
print()

# format 함수: [], {}, ()
print('{} and {}'.format('you', 'Me'))
print('{0} and {1} and {0}'.format('you', 'me'))
print('{a} are {b}'.format(a='You', b='Me'))
# % 사용
print("%s's favorite number is %d" % ('Eunki', 7))

print("Test1: %5d, Price: %4.2f" %(776, 6534.123))
print("Test1: {0: 5d}, Price: {1: 4.2f}".format(776, 6534.123))
print("Test1: {a: 5d}, Price: {b: 4.2f}".format(a=776, b=6534.123))