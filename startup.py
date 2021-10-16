import os
import mysql.connector

ENV_FILE = 'DC-Bot/cogs/etc/.env'
FILE1 = 'DC-Bot/API/config.py'
FILE2 = 'DC-Bot/cogs/etc/config.py'

ENV_TEMPLATE = open('templates/templateENV', 'r')
TEMPLATE1 = open('templates/templateAPICONFIG', 'r')
TEMPLATE2 = open('templates/templateBOTCONFIG', 'r')
TEMPLATE3 = open('templates/templateBOTCONFIGv2', 'r')

SQLTEMPLATE_TOKEN = open('templates/templateSQLtoken', 'r')
SQLTEMPLATE_ROLL = open('templates/templateSQLroll_txt', 'r')
SQLTEMPLATE_COUNTER = open('templates/templateSQLcounter', 'r')


def setup(path, template):
    if os.path.isfile(path):
        return f'File {path} exists!'

    else:
        f = open(path, 'w')
        for i in template:
            f.write(i)

        f.close()


def sql_setup():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='dcbot'
    )

    cur = mydb.cursor()
    cur.execute("SELECT Name FROM tokens WHERE Name='Cougars'")

    if cur.fetchone() == None:
        pass


sql_setup()

if __name__ == '__main__':
    print('Option Normal/Flask: ', end='')
    not_true = True
    while not_true:
        input_ = input()
        if input_.lower() == 'normal':
            setup(ENV_FILE, ENV_TEMPLATE)
            setup(FILE1, TEMPLATE1)
            setup(FILE2, TEMPLATE2)

            not_true = False

        elif input_.lower() == 'flask':
            print('if you pour water on a rock, nothing happens!')  # if you pour water on a rock, nothing happens!

            not_true = False

        elif input_.lower() == 'exit':
            print('Exiting...')
            break

        else:
            print('Wrong input. Possible inputs: Normal, Flask. Try it again: ', end='')
