print(~25)

'''
Two's Complement Rules:
In two's complement (which Python uses for signed integers):

If the leftmost bit is 0 → positive number
If the leftmost bit is 1 → negative number

Converting 11111010 to decimal:
Since the leftmost bit is 1, this represents a negative number.
Method 1: Standard two's complement conversion
11111010 (binary) → negative number

Step 1: Flip all bits
11111010 → 00000101

Step 2: Add 1
00000101 + 1 = 00000110

Step 3: Convert to decimal and make negative
00000110 = 6 in decimal
So the result is -6
Method 2: Mathematical formula
For 8-bit two's complement:
If first bit is 1, then: value = decimal_value - 256

11111010 as unsigned decimal = 250
Since first bit is 1: 250 - 256 = -6
Method 3: Bit-by-bit calculation
Position: 7  6  5  4  3  2  1  0
Binary:   1  1  1  1  1  0  1  0
Values: -128 64 32 16  8  0  2  0

Sum: -128 + 64 + 32 + 16 + 8 + 0 + 2 + 0 = -6
Here's the complete code to visualize this:
pythondef explain_twos_complement_conversion(binary_str):
    print(f"Converting {binary_str} to decimal using two's complement:")
    print("=" * 50)
    
    # Convert to unsigned first
    unsigned = int(binary_str, 2)
    print(f"As unsigned: {unsigned}")
    
    # Check if negative (first bit is 1)
    if binary_str[0] == '1':
        print("First bit is 1, so this is negative in two's complement")
        
        # Method 1: Flip bits and add 1
        print("\nMethod 1 - Flip bits and add 1:")
        flipped = ''.join('1' if bit == '0' else '0' for bit in binary_str)
        print(f"Original: {binary_str}")
        print(f"Flipped:  {flipped}")
        flipped_decimal = int(flipped, 2)
        print(f"Flipped decimal: {flipped_decimal}")
        print(f"Add 1: {flipped_decimal} + 1 = {flipped_decimal + 1}")
        print(f"Make negative: -{flipped_decimal + 1}")
        
        # Method 2: Subtract 2^n
        bit_width = len(binary_str)
        print(f"\nMethod 2 - Subtract 2^{bit_width}:")
        print(f"{unsigned} - {2**bit_width} = {unsigned - 2**bit_width}")
        
        # Method 3: Weighted sum
        print(f"\nMethod 3 - Weighted sum:")
        total = 0
        for i, bit in enumerate(reversed(binary_str)):
            if i == bit_width - 1:  # Most significant bit
                weight = -(2**i)
            else:
                weight = 2**i
            
            if bit == '1':
                total += weight
                print(f"Position {i}: {bit} × {weight:4} = {weight if bit=='1' else 0:4}")
            
        print(f"Total: {total}")
    
    else:
        print("First bit is 0, so this is positive")
        print(f"Value: {unsigned}")

# Test with your example
explain_twos_complement_conversion("11111010")
Quick way to remember:

11111010 = 250 as unsigned
But since first bit is 1, it's negative in two's complement
250 - 256 = -6

That's why Python's ~5 gives -6!
'''

a = int(input())
b = int(input())
s = a and b
t = a or b
u = not(a) 
print(s, t, u)