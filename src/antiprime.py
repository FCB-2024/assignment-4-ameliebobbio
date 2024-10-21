## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
import sys

def main(x) :
	## YOU CODE SHOULD START HERE AST THE SAME
	## IDENTATION AS THIS COMMENT
	i=1
	r=0
	while i<=x:
		if x%i==0:
			r=r+1
		i=i+1

	d=0
	l=1
	while l<x and d<r:
		d=0
		a=1
		while a<=l:
			if l%a==0:
				d=d+1
			a=a+1
		l=l+1

	if d>=r:
		res="not anti-prime"
	else:
		res="anti-prime"

	## THE LAST LINES OF YOUR CODE SHOULD EITHER
	## RETURN THE VALUE "anti-prime" or "not anti-prime"
	## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
	## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
	## "anti-prime" or "not anti-prime"
	return(res)

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :

	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
	if len(sys.argv) > 2:
		print("error: antiprime.py <x>")
	else:
		x = int(sys.argv[1])
		print(main(x))
