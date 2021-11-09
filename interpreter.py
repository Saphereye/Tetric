"""
==================================
TETRIC : TExT editoR wIth Commands
==================================
"""
log = open('logfile.txt', 'w')
dividerSymbol = '|'
predefinedFunc = {'0.5': '½',
                  'mu': 'μ',
                  'int': '∫',
                  'inf': '∞',
                  'x': '×',
                  '/': '÷',
                  'Cdel': 'Δ',
                  'sdel': 'δ',
                  'pi': 'π',
                  'theta': 'θ',
                  '2root': '√'}

# operator : [description,example]
operators = {'.': ['multiply text by n times', "5 . hello", "(5,5) . hello"],
             '-': ['delete n previous letter, by default 1', "1 -"],
             '--': ['delete n previous line(s), by default 1']}
numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}


# list to str
def join(inputList):
    outputString = ''
    for i in inputList:
        outputString += i + ' '
    return outputString


# replace 1st occurrence of element with another in a list
def replace(givenList, original, new):
    for i in range(len(givenList)):
        if givenList[i] == original:
            return givenList[:i] + [new] + givenList[i + 1:]


def converter(inputText):
    # |9..| means 9 times .
    # number first
    elements = []
    buffer = ''
    count = 0
    divCount = 0
    outputText = ''
    for i in inputText + 'ͷ':
        # print(count, divCount, outputText, buffer)
        if i == dividerSymbol:
            if divCount:
                divCount = 0
                count += 1
                elements.append([True, buffer])
                buffer = ''
            else:
                count += 1
                divCount += 1
                elements.append([False, buffer])
                buffer = ''
        elif i == 'ͷ':
            elements.append([False, buffer])
        else:
            buffer += i
            count += 1
    # print(elements)
    for i in elements:
        if i[0]:
            if i[1] in predefinedFunc:
                outputText += predefinedFunc[i[1]]
            else:
                contents = []
                buffer = ''
                # print(i[1])
                for j in range(len(i[1])):
                    if i[1][j] in operators:
                        try:
                            contents.append(eval(buffer.strip()))
                        except:
                            contents.append('')
                        contents.append(i[1][j].strip())
                        contents.append(i[1][j + 1:].strip())
                        break
                    else:
                        buffer += i[1][j]
                # print(contents)
                operator = contents[1]
                number = contents[0]
                text = contents[2]
                if operator == '.':
                    if str(type(number)) == "<class 'tuple'>":
                        for _ in range(number[0]):
                            for __ in range(number[1]):
                                outputText += text
                            outputText += '\n'
                    else:
                        try:
                            outputText += contents[0] * contents[2]
                        except:
                            log.write("something's not right")
                if operator == '-':
                    try:
                        outputText += '\b' * number
                        # outputText = outputText[:-number]
                    except TypeError:
                        log.write('Incorrect argument for - operator')
        else:
            outputText += i[1]
    # print(elements)
    return outputText


log.close()
if __name__ == "__main__":
    while 1:
        x = input()
        print(converter(x))
