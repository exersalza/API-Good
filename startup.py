import os

ENV_FILE = 'DC-Bot/cogs/etc/.env'
FILE1 = 'DC-Bot/API/config.py'
FILE2 = 'DC-Bot/cogs/etc/config.py'


ENV_TEMPLATE = open('templates/templateENV', 'r')
TEMPLATE1 = open('templates/templateAPICONFIG', 'r')
TEMPLATE2 = open('templates/templateBOTCONFIG', 'r')
TEMPLATE3 = open('templates/templateBOTCONFIGv2', 'r')


def setup(path, template):
  if os.path.isfile(path):
    return f'File {path} exists!'

  else:
    f = open(path, 'w')
    for i in template:
      f.write(i)
    
    f.close()



if __name__ == '__main__':
  _input = input('Option: ')
  if _input == 'normal':
    setup(ENV_FILE, ENV_TEMPLATE)
    setup(FILE1, TEMPLATE1)
    setup(FILE2, TEMPLATE2)
  elif _input == 'flask':
    print('if you poure water on a rock, nothing happens!')  # if you poure water on a rock, nothing happens!
  else:
    raise ValueError('Wrong input. Possible inputs: normal, flask')
