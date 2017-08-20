from html.parser import HTMLParser

class MyParser(HTMLParser):
    def print_attributes(self, attrs):
        for attr in attrs:
            print('->', attr[0], '>', attr[1])
        def handle_starttag(self, tag, attrs):
            print('Start'.ljust(6,' '),': ',tag, sep = '')
            self.print_attributes(attrs)
        def handle_endtag(self, tag):
            print('End'.ljust(6,' '), ': ',tag, sep = '')
        def handle_startendtag(self, tag, attrs):
            print('Empty'.ljust(6,' '), ': ',tag, sep = '')
            self.print_attributes(attrs)

if __name__ == '__main__':
    parser = MyParser()
    for _ in range(int(input())):
        parser.feed(input())
