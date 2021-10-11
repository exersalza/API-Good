from pyfiglet import Figlet

banner = Figlet(font='slant').renderText('API-Goose')
print(str(banner))
with open('test.txt', 'w') as f:
    for i in banner:
        f.write(i)

    f.close()
