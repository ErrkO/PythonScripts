
class CodePair:
    symbol = ''
    value = ''

    def __init__(self,symbol,value):
        self.symbol = symbol
        self.value = value


class PercentEncoder:

    codePairs = []

    def __init__(self):
        self.codePairs = [ CodePair(':','%3A')
                            ,CodePair('/','%2F')
                            ,CodePair('?','%3F')
                            ,CodePair('#','%23')
                            ,CodePair('[','%5B')
                            ,CodePair(']','%5D')
                            ,CodePair('@','%40')
                            ,CodePair('!','%21')
                            ,CodePair('$','%24')
                            ,CodePair('&','%26')
                            ,CodePair("'",'%27')
                            ,CodePair('(','%28')
                            ,CodePair(')','%29')
                            ,CodePair('*','%2A')
                            ,CodePair('+','%2B')
                            ,CodePair(',','%2C')
                            ,CodePair(';','%3B')
                            ,CodePair('=','%3D')
                            ,CodePair('%','%25')
                            ,CodePair(' ','+') ]
    
    def ParseString(self,query):
        chars = [char for char in query]
        parsed = ''

        for char in chars:
            parsed += self.ParseChar(char)

        return parsed

    def ParseChar(self,char):
        for pair in self.codePairs:
            if char == pair.symbol:
                return pair.value
            else:
                return char