""" 

This program will delete the entire line
in file if it finds the a house bank.

"""

fn = '/home/mrocha/housebankdel/banks.txt'
fno = '/home/mrocha/housebankdel/banks_output.txt'
f = open(fn)
output = []
housebank = "CIBC"
for line in f :
    if not housebank in line:
        output.append(line)
f.close()
f = open(fno, 'w')
f.writelines(output)
f.close()

