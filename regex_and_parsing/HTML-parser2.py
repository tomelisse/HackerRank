from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        endlines = data.count('\n')
        print('>>> Single-line Comment') if endlines == 0 else print('>>> Multi-line Comment')
        print(data)
    def handle_data(self, data):
        if data != '\n':
            print('>>> Data')
            print(data)
          
if __name__ == '__main__':
    parser = MyHTMLParser()
    html = ""       
    for _ in range(int(input())):
        html += input().rstrip()
        html += '\n'    
    parser.feed(html)
    parser.close()
