import time

startTime = time.time()

# Class to convert words and numbers
class Converter(object):
    tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    thousands = ['', 'thousand', 'million', 'billion']
    lessThan20 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

    def numberToWords(self, num):
        if num == 0:
            return 'zero'
        ans = ''
        i = 0
        while num > 0:
            if num % 1000 != 0:
                ans = f'{self.helper(num % 1000)}{Converter.thousands[i]} {ans}'
                i += 1
                num //= 1000
            return ans.strip()

    def helper(self, n):
        if n == 0:
            return ''
        elif n < 20:
            return Converter.lessThan20[n] + ' '
        elif n < 100:
            return Converter.tens[n // 10] + ' ' + self.helper(n % 10)
        else:
            return f'{Converter.lessThan20[n // 100]} hundred and {self.helper(n % 100)}'


converter = Converter()
mathDict = {}

for i in range(999, 0, -1):
    mathDict[converter.numberToWords(i)] = str(i)

mathDict.update(
    {
        'equals': '=',
        'multiple': '*',
        'plus': '+',
        'substract': '-',
        'division': '/',
        '=': '==',
    }
)

# Read input file
with open('input.txt', 'r') as fp:
    inputFileData = fp.read()

# To reset output file data
with open('output.txt', 'w') as fp:
    pass

for key, val in mathDict.items():
    inputFileData = inputFileData.replace(key, val)

inputFileData = inputFileData.split('\n')[:-1]

n = int(inputFileData[0])
questions = inputFileData[1:]

for caseNo in range(len(questions)):
    question = questions[caseNo]
    question = question.strip()

    with open('output.txt', 'a') as fp:
        fp.write(f'Case #{caseNo+1}: {str(eval(question)).lower()}\n')

print(f'Program taken {time.time() - startTime} seconds to generate output.txt file')
