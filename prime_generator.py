# Large Prime Generation for RSA
import random


class PrimeGenerator:
    def __init__(self, n: int):
        # Pre generated primes
        self.first_primes_list: list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                                        31, 37, 41, 43, 47, 53, 59, 61, 67,
                                        71, 73, 79, 83, 89, 97, 101, 103,
                                        107, 109, 113, 127, 131, 137, 139,
                                        149, 151, 157, 163, 167, 173, 179,
                                        181, 191, 193, 197, 199, 211, 223,
                                        227, 229, 233, 239, 241, 251, 257,
                                        263, 269, 271, 277, 281, 283, 293,
                                        307, 311, 313, 317, 331, 337, 347, 349]
        self.n = n

    def generate(self):
        while True:
            prime_candidate = self.getLowLevelPrime()
            if not self.isMillerRabinPassed(prime_candidate):
                continue
            else:
                return prime_candidate

    def nBitRandom(self):
        return random.randrange(2 ** (self.n - 1) + 1, 2 ** self.n - 1)

    def getLowLevelPrime(self) -> int:
        """
        Generate a prime candidate divisible by first primes
        """
        while True:
            # Obtain a random number
            pc = self.nBitRandom()
            # Test divisibility by pre-generated
            # primes
            for divisor in self.first_primes_list:
                if pc % divisor == 0 and divisor ** 2 <= pc:
                    break
            else:
                return pc

    @staticmethod
    def isMillerRabinPassed(mrc: int) -> bool:
        """Run 20 iterations of Rabin Miller Primality test"""
        maxDivisionsByTwo = 0
        ec = mrc - 1
        while ec % 2 == 0:
            ec >>= 1
            maxDivisionsByTwo += 1

        def trialComposite(round_tester) -> bool:
            if pow(round_tester, ec, mrc) == 1:
                return False
            for i in range(maxDivisionsByTwo):
                if pow(round_tester, 2 ** i * ec, mrc) == mrc - 1:
                    return False
            return True

        # Set number of trials here
        numberOfRabinTrials = 20
        for i in range(numberOfRabinTrials):
            round_tester = random.randrange(2, mrc)
            if trialComposite(round_tester):
                return False
        return True
