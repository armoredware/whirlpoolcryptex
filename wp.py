import whirlpool
hashed_string = ''
count = 0
while(hashed_string[0:3]!='09f'):
        count = count + 1
	wp = whirlpool.new(str(count))
	hashed_string = wp.hexdigest()

print(hashed_string)
print(count)


