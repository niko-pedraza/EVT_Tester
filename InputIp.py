import subprocess
import os


def ip_batch_file(ip,dest_port, template, new_file):
    out_file_path = os.getcwd() + f'{new_file}'
    print(out_file_path)
    with open(out_file_path, 'w+') as batch:
        lines = template.readlines()
        print(lines)
        for line in lines:
            print(line, type(line))
            line = line.replace("destprn", ip)
            line = line.replace('d1prn',f'd{dest_port}prn')
            print(line)
            batch.write(line)

    subprocess.call([out_file_path])


ip = input('IP:')
dNprn = input('Destination Port(1-8):')
if not (1 <= int(dNprn) <= 8):
    dNprn = 1

template = input('batch name:')
directory = R'C:\Users\pniko\Desktop\BatchTemplates'

file = open(directory + f'\{template}')
out_filename = input('new batch file name(.bat,.cmd):')

ip_batch_file(ip,dNprn, file, out_filename)
