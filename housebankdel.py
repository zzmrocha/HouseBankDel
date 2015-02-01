""" 

This program will delete the entire line
in file if it finds the a house bank.

This is being moved to GitHub

"""

fn = '/home/mrocha/housebankdel/banks.txt'
f = open(fn)
output = []
housebank = "CIBC"
for line in f :
    if not housebank in line:
        output.append(line)
f.close()
f = open(fn, 'w')
f.writelines(output)
f.close()



fn = '/home/mrocha/housebankdel/banks.txt'
f = open(fn)
output = []
housebank = "BMO"
for line in f :
    if not housebank in line:
        output.append(line)
f.close()
f = open(fn, 'w')
f.writelines(output)
f.close()



fn = '/home/mrocha/housebankdel/banks.txt'
f = open(fn)
output = []
housebank = "TD"
for line in f :
    if not housebank in line:
        output.append(line)
f.close()
f = open(fn, 'w')
f.writelines(output)
f.close()


