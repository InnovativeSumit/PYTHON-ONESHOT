from calendar import*
year = int(input('Enter Year:'))
print(calendar(year, 2, 1, 8, 3))

# Argument	Value	Explanation
# year	User input	Year to print
# 2	w	Each date takes 2 characters
# 1	l	1 blank line between weeks
# 8	c	8 spaces between months
# 3	m	3 months per row