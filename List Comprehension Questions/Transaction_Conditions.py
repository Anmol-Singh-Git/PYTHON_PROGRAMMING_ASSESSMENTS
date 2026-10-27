transaction=[5000,-2000,3000,-1000,7000,-500]
positive=[ money  for money in transaction   if money>0 ]
withdrawals=[ money  for money in transaction   if money<0 ]
print("transaction total:",transaction)
print("only postive money:",positive)
print("only withdrawal amount:",withdrawals)
