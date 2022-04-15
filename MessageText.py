
class MessageText:

    symbols_to_del = [',', '.', '!', '?', ':', ';', '/']

    def __init__(self,msg) -> None:
        self.msg = msg

    def Lower(self):
        self.msg = self.msg.lower()

    def DeleteSymbols(self):
        for i in self.msg:
            if i in self.symbols_to_del:
                self.msg=self.msg.replace(i,'')
                