# config utf-8

# 別解(for使わない)
def add_comma(lst):
    if len(lst) <= 0:
        return ''
    if len(lst) == 1:
        return lst[0]
    return ', '.join(lst[:-1]) + ', and ' + lst[-1]

def list2string(list):
	s = ''
	for i, l in enumerate(list):
		if i == len(list)-1:
			s += 'and ' + l
			return s
		s += l + ', '
	return s

def main():
	a = ['apples', 'bananas', 'tofu', 'cats']
	print(list2string(a))
	return

if __name__ == '__main__':
	main()