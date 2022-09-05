class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [i for i in range (1,n+1)]
        for i in range(len(answer)):
            if answer[i] % 3 == 0  and answer[i] % 5 == 0:
                answer[i] = "FizzBuzz"
            elif answer[i] % 3 == 0:
                answer[i] = "Fizz"
            elif answer[i] % 5 == 0:
                answer[i] = "Buzz"
            else:
                answer[i] = str(i + 1)
        return answer
