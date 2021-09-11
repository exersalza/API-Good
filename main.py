from urlscan.scangrep import urlscan



if input('Input what you want: ').lower() == 'url':
    i = input('URL to Prove: ')

    if '400' in str(urlscan(i)):
        print('coggers')
