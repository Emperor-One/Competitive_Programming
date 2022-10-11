class Solution:
    def sortSentence(self, s: str) -> str:
        alist = s.split(' ')

        for i in range(len(alist)-1):
            for j in range(len(alist)-i-1):
                if alist[j][-1] > alist[j+1][-1]:
                    alist[j], alist[j+1] = alist[j+1], alist[j]

        for k in range(len(alist)):
            alist[k] = alist[k][:-1]
            
        s = ''
        s = ' '.join(alist)
        return s
