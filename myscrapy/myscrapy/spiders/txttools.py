class TxtTools:
    path = ''
    model = 'r+'
    text = ''
    def read_text(self):
        attr = []
        with open('C:\\Users\\29800\\PycharmProjects\\scrapyDemo\\myscrapy\\youdao.txt', self.model) as f:
            text = f.read()
            string = str(text).replace('', '')
            print(string)
