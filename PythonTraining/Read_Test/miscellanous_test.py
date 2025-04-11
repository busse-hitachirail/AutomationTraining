x = (1, 2, 3)
assert len(x) > 5, "len(x) not > 5"



try:
    infile = open(filename)
    data = infile.read()
finally:
    infile.close()

# Refactor as
with open(filename) as infile:
    data = infile.read()

# After Python 3.10, with statements no longer need to be a
# single line. with statements may now use parentheses to split the statement across several lines, improving readability, so that the following code, which nests calls to
# read and write files using the same with
with open("empty.txt") as infile, open("other.txt", "w") as outfile:
    data = infile.read()
    outfile.write(data)

with (
    open("empty.txt") as infile,
    open("other.txt", "w") as outfile
):
    data = infile.read()
    outfile.write(data)