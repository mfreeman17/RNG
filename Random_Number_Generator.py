import time

# Code by Matthew Freeman
# Use python 3 to run


class lfsr:
    # Class implementing linear feedback shift register.
    # This class helps produce psedo random numbers.
    # algorithim was found here: https://www.maximintegrated.com/en/design/technical-documents/app-notes/4/4400.html
    def __init__(self, taps):
        # Receives a list of taps. Taps are the bit positions that are XOR-ed
        # together and provided to the input of lfsr
        self.taps = taps
         # initial state of lfsr
        self.register = '1111111111111111'

   # following methods converts integers to binary strings and vice-versa
   #--------------------------------------------------------
    def int_to_bin(self, i):
        o = '{0:b}'.format(i)
        return o

    def bin_to_int(self, b):
        return int(b, 2)
   #--------------------------------------------------------



    def clock(self, bit):
        # Receives input bit and simulates one clock cycle
        # This xors bits then shifts and returns output bit
        # input bit are XOR-ed with the taps
        res = int(self.register[self.taps[0]])
        for m in range(1, len(self.taps)):
            tap = self.taps[m]
            res = res ^ int(self.register[tap])

        res = str(res ^ int(bit))
        o = self.register[len(self.register) - 1]
        self.register = res + self.register[:-1]

        return o  # returns output bit

    def seed(self, s):
        # This function seeds the lfsr by feeding all bits from s into clock
        s = self.int_to_bin(s)
        for i in s:
            self.clock(i)

    def get_output(self, n, skip=0):
        # This function clocks lfsr 'skip' number of cycles,
        # then clocks 'n' cycles more and records the output. Then returns
        # the output as an int.
        for x in range(skip):
            self.clock("0")
        out = ''
        for x in range(n):
            out += self.clock("0")
        out = self.bin_to_int(out)
        return out

    def get_random_int(self, min, max):
        # This function returns a psedo random integer using the lfsr
        # It takes a min integer and a max integer, and uses 1000 skips, then 1000 bits
        out = self.get_output(1000, 1000)
        out = out % (max - min + 1)
        out += min
        return out


if __name__ == "__main__":
    l = lfsr([2, 4, 5, 7, 11, 14])
    l.seed(int(time.time()))          # seeds to time to make output appear more random
    print(l.get_random_int(-1000, 1000))  # prints a random integer between -1000 and 1000
