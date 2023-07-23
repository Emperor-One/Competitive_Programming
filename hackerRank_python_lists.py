class Lists:
    def __init__(self):
        self.interal_list = []

    def __repr__(self):
        return f"{self.interal_list}"

    def insert(self, i, e):
        left = []
        right = []
        new = [e]
        is_found = False

        if i < 0 and i > -1 * len(self.interal_list):
            i = len(self.interal_list) + i
        
        elif i < 0 and i < -1 * len(self.interal_list):
            i = 0

  
        for j in range(len(self.interal_list)):
            if i == j:
                is_found = True
            
            if is_found:
                right.append(self.interal_list[j])

            else:
                left.append(self.interal_list[j])

        self.interal_list = left + new + right

    def remove(self, e):
        left = []
        right = []
        is_found = False
        found_count = 0
        for num in self.interal_list:
            if num == e and found_count < 1:
                is_found = True
                found_count += 1
                continue

            if is_found:
                right.append(num)
            
            else:
                left.append(num)

        self.interal_list = left + right

    def append(self, e):
        length = len(self.interal_list)
        new_list = [1] * (length + 1)
        for i in range(length):
            new_list[i] = self.interal_list[i]

        new_list[len(new_list) - 1] = e
        self.interal_list = new_list

    def sort(self):
        def merge(a, b):
            sorted_list = []
            i = j = 0

            while i < len(a) and j < len(b):
                if a[i] <= b[j]:
                    sorted_list.append(a[i])
                    i += 1
                else:
                    sorted_list.append(b[j])
                    j += 1

            while i < len(a):
                sorted_list.append(a[i])
                i += 1
            
            while j < len(b):
                sorted_list.append(b[j])
                j += 1
            
            return sorted_list

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            return merge(left, right)
        
        self.interal_list = merge_sort(self.interal_list)
                

    def pop(self):
        length = len(self.interal_list)
        new_list = [1] * (length - 1) if length > 1 else []
        for i in range(len(new_list)):
            new_list[i] = self.interal_list[i]

        self.interal_list = new_list

    def reverse(self):
        left = 0
        right = len(self.interal_list) - 1

        while left <= right:
            self.interal_list[left], self.interal_list[right] = self.interal_list[right], self.interal_list[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    N = int(input())
    lame_list = Lists()

    for _ in range(N):
        argv = input().split()
        
        if argv[0] == "insert":
            lame_list.insert(int(argv[1]), int(argv[2]))

        elif argv[0] == "print":
            print(lame_list)

        elif argv[0] == "remove":
            lame_list.remove(int(argv[1]))

        elif argv[0] == "append":
            lame_list.append(int(argv[1]))

        elif argv[0] == "sort":
            lame_list.sort()

        elif argv[0] == "pop":
            lame_list.pop()

        elif argv[0] == "reverse":
            lame_list.reverse()
        
        else:
            print("Invalid command.")
            break
