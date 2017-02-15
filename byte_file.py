import os, sys, random
def generate_file(filesize, numbytes, byteval):
	""" generate random binary file "temp" with specified file size and number of occurrences of specified byte value""" 
    size = int(filesize)
    numbytes = int(numbytes)
    try:
        assert size >= numbytes
        with open("temp", "wb+") as f:
            while size > 0:
                char = os.urandom(1)
                # write char to file only if it's not the specified byte value
                if chr(int.from_bytes(char, byteorder=sys.byteorder)) != chr(int(byteval)):
                    f.write(char)
                    size -= 1
                continue
            while numbytes > 0:
            	# find a random position in file and write the specified byte value numbytes times 
                f.seek(random.randint(0, int(filesize)-numbytes))
                f.write(bytes([int(byteval)]))
                numbytes -= 1
        # return results of char_count()        
        return char_count("temp", byteval)
    except AssertionError:
        print("file size must be greater than or equal to number of times byte appears.")
def char_count(file, byteval):
    """ takes in a file and a byte and returns the count of appearances of the byte in the file. """
    byteval = int(byteval)
    valcount = 0
    totalcount = 0
    with open(file, "rb") as f:
        for line in f:
            for i in line:
                totalcount += 1
                if i == byteval:
                    valcount += 1
    return "Byte value count: {}\nTotal bytes: {}".format(valcount, totalcount)
if __name__ == '__main__':
    import cProfile
    byteval = input("Enter byte value (0-255): ")
    numbytes = input("How many times for byte value to occur: ")
    filesize = input("Specify file size (>={}): ".format(numbytes))
    print(generate_file(filesize, numbytes, byteval))
    cProfile.run("generate_file(filesize, numbytes, byteval)")
