main = __name__ == "__main__"
class NikitosLanguage():
    def __init__(self, code):
            self.code = code
            self.result = ''
            
    def on_error(self, c, code):
        result = self.result
        result = f'Ошибка в строке {c}: {code}'
        return result
    def compilator(self):
        result = self.result
        codes = str(self.code).split(';')
        c = 0
        commands = {'TEST': 'testing',}
        for code in codes:
            code = code.replace("\n", "").replace("\t", "").upper()
            c += 1
            if code == '':
                pass
            elif "ВЫВОД" in code:
                code = code.replace("ВЫВОД", "")
                dblq = '("' in code and ')"' in code
                sgq = '(\'' in code and '\')' in code
                if dblq or sgq :
                  code = code.replace('(', '').replace(')', '')
                  result += code +  '\n' 
                else:
                  result = self.on_error(c, code)
            elif "РЕШИТЬ" in code:
                code = code.replace("РЕШИТЬ ", "")
                try:
                    result +=  str(eval(code)) + '\n'
                except Exception as e:
                    print(e)
                    result = self.on_error(c, code)
            else:
                 result = self.on_error(c, code)
        return result
if main:
    test = NikitosLanguage('ВЫВОД(\'ТЕСТ\')')
    print(test.compilator())