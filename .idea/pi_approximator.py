class PiApproximator(object):
    """It calculates the approximate value of Pi based on Nilakantha's series.It has a method namely pi_calculator that returns the approximate value of pi."""

    def pi_calculator(self):
        """Iterates the loops as per specified number of times and return the approximate value of pi."""
        positiveSum = 0.0
        negativeSum = 0.0
        TERMS = 1000 #Loops are iterated for 10^3 times to get pi=3.14159265356 (correct to 11 decimal digits)

        for n in range(1,TERMS,1):
            positiveSum += 1/(n*((4*n)-1.0)*((4*n)-2.0)) # Generates the first partial sum
        for n in range(1,TERMS,1):
            negativeSum += 1/(n*((4*n)+1.0)*((4*n)+2.0)) #Generates the second partial sum

        piEstimate=(3+(positiveSum-negativeSum)) #Subtract the two summations and add 3 to get pi approximation
        return piEstimate #returns approximated value of pi
