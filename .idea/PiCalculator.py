#use the Gregory-Leibniz series for the calculation of Pi
#pi=4(1-1/3+1/5-1/7+1/9-1/11+...........)
#
def pi_calculator(terms):
 positive_sum = 0.0
 negative_sum = 0.0

 for n in range(1,terms,1):
    positive_sum += 1/((4*n)-3.0)
 print(positive_sum) #return positive_sum #4.30098911394

 for n in range(1,terms,1):
    negative_sum += 1/((4*n)-1.0)
 print(negative_sum) #return negative_sum #3.14159260358

 pi_estimate=4*(positive_sum-negative_sum)
 print(pi_estimate)

pi_calculator(10000000) #here the loops are iterated 10^7 times to get the value of pi correct to 7 decimal places # pi=3.14159260358

