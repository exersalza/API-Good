from urlscan.url_grep import urlscan
from switch import Switch


def main(val=input('Input what you want: ').lower().strip(' ')):

    # val = input('Input what you want: ').lower().strip(' ')

    with Switch(val) as case:

        if case('url'):
            i = input('URL to Prove: ')

            def url_switcher(url=urlscan(str(i))):
                values = []

                with Switch(str(url).strip('<Response > [ ]')) as url_case:
                    if url_case('400'):
                        values.append('dont exists or is not reachable.')
                    if url_case('200'):
                        values.append('passed')

                return values

            print(str(url_switcher()).strip('[\']'))


main()

