import subprocess

def ip_batch_file(ip,template):

    with open(r"C:/Users/PTX/Desktop/WIPtools/Actions/template_batch.bat",'w+') as batch :
        
        lines = template.readlines()
        print(lines)
        for line in lines:
            print(line,type(line))
            line = line.replace("destprn",ip)
            print(line)
            batch.write(line)

    #subprocess.call([r"C:/Users/PTX/Desktop/WIPtools/Actions/template_batch.bat"])


ip = "192.168.201.225"
file = open("C:/Users/PTX/Desktop/WIPtools/BatchTemplate/iptest.txt") 

ip_batch_file(ip,template=file)
    
            
        
