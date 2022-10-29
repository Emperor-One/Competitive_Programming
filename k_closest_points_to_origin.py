class Solution:
    def kClosest(self, points, k):
        distance = lambda point: sqrt(point[0]**2 + point[1]**2)
        return sorted(points, key=distance)[:k]
