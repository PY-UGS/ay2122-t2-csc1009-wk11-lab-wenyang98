class Calculator:

    # Constructor
    def __init__(self, input1, input2):
        self.input1 = input1 # param input1 - first number input
        self.input2 = input2 # param input1 - first number input
        self.result = 0 # param result set to 0 - no result yet

    # func to sum input1 and input2
    def adder(self):
        self.result = self.input1 + self.input2
        print("Add: {} + {} = {:.2f}".format(self.input1, self.input2, self.result)) #prints result it in 2dp

    # func to subtract input1 and input2
    def subtractor(self):
        self.result = self.input1 - self.input2
        print("Subtract: {} - {} = {:.2f}".format(self.input1, self.input2, self.result)) #prints result it in 2dp

    # func to multiply input1 and input2
    def multiplier(self):
        self.result = self.input1 * self.input2
        print("Multiply: {} * {} = {:.2f}".format(self.input1, self.input2, self.result)) #prints result it in 2dp

    # func to divide input1 and input2
    def divider(self):
        try:
            self.result = self.input1 / self.input2
            print("Divide: {} / {} = {:.2f}".format(self.input1, self.input2, self.result)) #prints result it in 2dp
        except ZeroDivisionError:
            print("Divisor can never be 0.")
        

    # sets input 1, 2 & result to 0
    def clear(self):
        self.input1 = 0
        self.input2 = 0
        self.result = 0

def main():
        # 2 user input for 1st and 2nd number
        input1 = float(input("Enter the first number: "))
        input2 = float(input("Enter the second number: "))

        # Creating obj calculator
        calculator = Calculator(input1, input2)

        # perform functions to the obj created
        calculator.adder()
        calculator.subtractor()
        calculator.multiplier()
        calculator.divider()
        calculator.clear()

main()