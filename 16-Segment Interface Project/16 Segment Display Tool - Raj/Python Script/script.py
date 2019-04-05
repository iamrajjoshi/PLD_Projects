'''
Converts Logic Friday minimized equations to WINCUPL code
Note: Don't copy over "Minimized:" heading from Logic Friday (Just the Equations)
Based on Spencer Ng's Script, Created by Raj Joshi
'''
filename = input("Enter the filename of the minimized equations: ")
output = ''
with open(filename, 'r') as fi:
	for _ in range(16):
		inputline = " ".join((fi.readline()[:-2]).split()) #for each equation take out last two char (';\n') and random white space
		output += inputline.split(' = ')[0] + ' = ' #store output symbol and = in output string
		productterms = (inputline.split(' = ')[1]).split(' + ') #get all product terms and split individual terms
		for i in range(len(productterms)):
			output += '('
			literals = productterms[i].split(' ') #get each literal
			for j in range(len(literals)):
				if len(literals[j]) == 2: output+= ('!' + literals[j])[:-1] #if len = 2 (A') --> Not (Also take out ' (not symbol LF))
				else: output += literals[j] #its not a !
				if j != (len(literals)-1): output+='&' #don't add a & for last term
			output += ')'
			if i != (len(productterms)-1): output += '#' #don't add a # fot last term
		output += ';\n'
with open('WINCUPL.txt', 'w') as fo: fo.write(output)
print(output + "\nThe converted equations have been saved in 'WINCUPL.txt'")