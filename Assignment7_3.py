class Numbers:
	def __init__(self):
		self.value=int(input("Enter the number : "))

	def ChkPrime(self):
		if self.value > 1: 
  
   			for i in range(2, self.value//2): 
   				if (self.value % i) == 0: 
   					print(self.value, "is not a prime number") 
   					break
   			else: 
   				print(self.value, "is a prime number") 
  
		else:
   			print(self.value, "is not a prime number") 

	def ChkPerfect(self):
		sum1 = 0
		for i in range(1, self.value):
			if(self.value % i == 0):
				sum1 = sum1 + i
		if (sum1 == self.value):
			print("Number is perfect :True")
		else:
			print("Number is perfect :False")

	def Factors(self):
		print("Factors are : ")
		for i in range(1, self.value + 1):
   			if self.value % i == 0:
   				print(i,end=" ")

	def SumFactors(self):
		print()
		sum=0
		for i in range(1, self.value + 1):
			if self.value % i == 0:
				sum=sum+i
		print("Sum is : ",sum)

def main():
	obj1=Numbers()
	obj1.ChkPrime()
	obj1.ChkPerfect()
	obj1.Factors()
	obj1.SumFactors()

	obj2=Numbers()
	obj2.ChkPrime()
	obj2.ChkPerfect()
	obj2.Factors()
	obj2.SumFactors()

if (__name__=="__main__"):
	main()