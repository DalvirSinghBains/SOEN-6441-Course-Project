class PiApproximatorSecond(object):
    def piCalculator(self):
        positiveSum = 0.0
        negativeSum = 0.0
        terms = 1000

        for n in range(1,terms,1):
            positiveSum += 1/(n*((4*n)-1.0)*((4*n)-2.0))
        for n in range(1,terms,1):
            negativeSum += 1/(n*((4*n)+1.0)*((4*n)+2.0))

        piEstimate=(3+(positiveSum-negativeSum))
        return piEstimate


#hence the loops are iterated for 10^4 times
#to get the value of pi correct to 11 decimal places # pi=3.14159265359

#hence the loops are iterated for 10^3 times
#to get the value of pi correct to 11 decimal places # pi=3.14159265356

#hence the loops are iterated for 10^2 times
#to get the value of pi correct to 8 decimal places # pi=3.14159262187