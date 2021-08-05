import json

items = json.loads('[{"id":1, "text": "Item 1"}, {"id":2, "text": "Item 2"}]')

for item in items:
    print(item['text'])

# 1
print(50+50)
print(100-10)

# 2
# print(30+*6,6^6,6**6,6+6+6+6+6+6)
print(30 +6)
print(pow(6, 6))
print(6+6+6+6+6+6)

# 3
print("Hello World")

for i in range(10):
    print("Hello World : " + str(i+1))

# 4 

def monthly_payment_calc(loanSize, interestRate, lengthOT): 
    monthlyRate = interestRate/12
    payment = (loanSize * monthlyRate) / (1 - pow((1 + monthlyRate), -lengthOT))

    print(round(payment)) 



monthly_payment_calc(800000, .06, 103)
