#The Gregory-Leibniz series is used for the calculation of Pi
#pi=4(1-1/3+1/5-1/7+1/9-1/11+...........)
#Since the above series consists of infinite terms
#hence the loops are iterated for 10^6 times
#to get the value of pi correct to 7 decimal places # pi=3.14159215359

class PiApproximator(object):
  def piCalculator(self):
    positiveSum = 0.0
    negativeSum = 0.0
    terms = 1000000

    for n in range(1,terms,1):
      positiveSum += 1/((4*n)-3.0)
    for n in range(1,terms,1):
      negativeSum += 1/((4*n)-1.0)

    piEstimate=4*(positiveSum-negativeSum)
    return piEstimate






