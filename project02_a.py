output_file=input('Enter your file name:')
if '.txt' in output_file:
    pass
else:
    print('The file name should have a .txt file extension')
    exit()
inp=input('Enter the year:').lower()
if inp=='' or input=='all':
    with open('measles.txt','r') as main_file:
        with open(output_file,'w') as output:
            for line in main_file:
                output.write(line)
elif inp.isdigit():
    with open('measles.txt','r') as main_file:
        with open(output_file,'w') as output:
            for line in main_file:
                year=line[-5:]
                if year.startswith(inp):
                    output.write(line)
