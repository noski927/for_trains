import sys

class StreamData:
    def create(self, fields, lst_values):
        pass


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res

sd = StreamData()
sd.create() 

sr = StreamReader()
data, result = sr.readlines()