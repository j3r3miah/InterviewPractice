class Solution:
    num_words = {
        '0': 'Zero',
        '1': 'One',
        '2': 'Two',
        '3': 'Three',
        '4': 'Four',
        '5': 'Five',
        '6': 'Six',
        '7': 'Seven',
        '8': 'Eight',
        '9': 'Nine',
    }
    
    teens_words = {
        '0': 'Ten',
        '1': 'Eleven',
        '2': 'Twelve',
        '3': 'Thirteen',
        '4': 'Fourteen',
        '5': 'Fifteen',
        '6': 'Sixteen',
        '7': 'Seventeen',
        '8': 'Eighteen',
        '9': 'Nineteen',
    }
    
    tens_place_words = {
        '2': 'Twenty',
        '3': 'Thirty',
        '4': 'Forty',
        '5': 'Fifty',
        '6': 'Sixty',
        '7': 'Seventy',
        '8': 'Eighty',
        '9': 'Ninety',
    }
    
    pow10_word = {
        0: '',
        1: ' Thousand',
        2: ' Million',
        3: ' Billion',
        4: ' Trillion',
    }
    
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        
        digits = list(reversed(str(num)))
        
        rv = []        
        i = 0
        while i < len(digits):
            words = self.threeDigitsToWords(digits[i:i+3])
            if words:
                pow10 = i // 3
                words += self.pow10_word[pow10]
                rv.append(words)
            i += 3
        
        return ' '.join(reversed(rv))
        
    def threeDigitsToWords(self, digits):
        # 123, 045, 543, 13, 7, 006
        rv = []
        # hundreds place
        if len(digits) > 2 and digits[2] != '0':
            rv.append(self.num_words[digits[2]])
            rv.append('Hundred')
        # handle teens
        if len(digits) > 1 and digits[1] == '1':
            rv.append(self.teens_words[digits[0]])
        else:
            # tens place
            if len(digits) > 1 and digits[1] != '0' and digits[1] != '1':
                rv.append(self.tens_place_words[digits[1]])
            # ones place
            if len(digits) > 0 and digits[0] != '0':
                rv.append(self.num_words[digits[0]])
        return ' '.join(rv)


if __name__ == '__main__':
    import sys
    print(Solution().numberToWords(int(sys.argv[1])))
