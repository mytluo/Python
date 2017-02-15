import string
def insert_newlines(file, every=80):
	""" takes in a file and inserts a newline every 80 characters """
    flist = []
    with open(file, "r") as f:
        for line in f:
        	# if line is already less than 80 characters, append to flist
            if len(line) < every:
                flist.append(line)
            else:
                start = 0
                cutoff = 0
                tracker = every
                for i, char in enumerate(line):
                	# update cutoff index of whitespace in line as long as it's within 80 characters per section of the line
                    if char in string.whitespace and i <= tracker:
                        cutoff = i
                    elif i > tracker:
                        flist.append(line[start:cutoff])
                        start = cutoff+1
                        tracker += every
                    # append last section of the line once the end of the original line is reached   
                    elif i == len(line.rstrip())-1:
                        flist.append(line[start:])

    return "\n".join(flist)
