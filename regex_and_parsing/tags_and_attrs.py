from html.parser import HTMLParser

class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        self.print_attributes(attrs)
    def print_attributes(self, attrs):
        for attr in attrs:
            print('->', attr[0], '>', attr[1])

if __name__ == '__main__':
    parser = MyParser()
    for _ in range(int(input())):
        parser.feed(input())
    parser.close()
