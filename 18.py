class RomanNumerals:
    def __init__(self):
        self.values = {
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
            10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
            100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
        }
        self.sorted_values = sorted(self.values.keys(), reverse=True)
    def int_to_roman(self, num):
        roman_num = ''
        for value in self.sorted_values:
            while num >= value:
                num -= value
                roman_num += self.values[value]
        return roman_num
converter = RomanNumerals()
print(converter.int_to_roman(34)) 
print(converter.int_to_roman(94)) 
print(converter.int_to_roman(400)) 
print(converter.int_to_roman(1999)) 