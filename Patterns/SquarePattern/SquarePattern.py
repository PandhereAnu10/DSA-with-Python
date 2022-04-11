## Square Pattern Code with 
   ## Input = Integer N (Total no. of Rows)
	## Output = pattern N lines (pattern will Nth times with both rows & cols)

N = int(input())
def solidSquare(N):
    for i in range(0, N):
        # Print stars after spaces
        for j in range(1, N + 1):
            print(N, end = "")
        # Move to the next line/row
        print()
solidSquare(N)


