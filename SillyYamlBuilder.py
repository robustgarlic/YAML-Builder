import sys
import os.path
from ruamel.yaml import YAML ##yaml library see https://yaml.readthedocs.io/en/latest/ ##

##Builds future directory for ansible playbook config output##

##could be written sperately and called in from the playbook itself##

##but for now its in here##

build_dir= '/var/lib/ansible/projects/JuniperBaseConfigGenerator/build/'
host_path= '/var/lib/ansible/projects/JuniperBaseConfigGenerator/host_vars'

##User Inputed variable for Hostname must follow convention of C#XXX.LOC##

hostname= input("What is the Hostname of the Device?: ")

##Builds path for yaml file##

##yaml file is called from ansible playbook for variables in jinja2 template##

file_name= os.path.join(host_path, hostname+".yaml)

##full path build for future ansible playbook output##

output_path= os.path.join(build_dir, hostname)

##yaml defined here#

 

hosty = """\
host:
  management:
    ip:
    mask:
  loopback:
    ip:
    mask: 32
"""

 

##User input asked and defined here##

yaml = YAML()
data = yaml.load(hosty)

data['host']['management']['ip'] = input("What is your management IP?:")
data['host']['management']['mask'] = int(input("What is your management Subnet Mask?:"))
data['host']['loopback']['ip'] = input("What is your loopback IP?:")






##Checks if file already exists, if file exists it will only overwrite based on yes input from user##
##If file doesnt exist builds as normal in else statemnet##

while True:
    if os.path.isfile(file_name):
      overwrite = input("This File already exists. Overwrite? Y = yes, N = no\n")
      if overwrite.lower() == "y":
        with open(file_name, "w") as outfile:
            yaml.dump(data, outfile)
            outfile.write(file_name)
            outfile.close()
            print('****Check host_vars directory for Host YAML File****')
            break

      elif overwrite == "n":
        print('You have selected No, check whatever you need to check and try again!!')
        break

      else:
        print('You have entered invalid input, please run script again, Thank You!')
        break

    else:
      with open(file_name, "w") as outfile:
          yaml.dump(data, outfile)
          outfile.close()
          print('****Check host_vars directory for Host YAML File****')
          break