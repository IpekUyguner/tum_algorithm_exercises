import  sys

class UnionFind(object):

    def __init__(self, N):
        self._id = list(range(2*N+1))   #For ith country in the set, represent the enemy of that country as i+N
        self._siz = [1] * (2*N+1)       #0th index is not used. 1.country in 1.st index...

    def find(self, x):
        p = self._id[x]
        while p != self._id[p]:
            q = self._id[p]
            self._id[p] = self._id[q]
            p = q
        return p

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return
        if self._siz[xroot] < self._siz[yroot]:
            self._id[xroot] = yroot
            self._siz[yroot] += self._siz[xroot]
        else:
            self._id[yroot] = xroot
            self._siz[xroot] += self._siz[yroot]


if __name__ == "__main__":
    total_case = sys.stdin.readline()
    for counter in range(int(total_case)):

        int_line = list(map(int, sys.stdin.readline().split()))
        uf = UnionFind(int_line[0])
        n = int_line[0]
        for i in range(int_line[1]):
            current_line = list(sys.stdin.readline().split())
            country_first = int(current_line[1])
            country_second = int(current_line[2])

            if(current_line[0] == "F"):                       #set friend
                uf.union(country_first,country_second)
                uf.union(country_first+n, country_second+n)    #my allience's enemy is my enemy
            else:                                             #set enemy
                uf.union(country_first,country_second+n)
                uf.union(country_first+n, country_second)          # common cause makes unities people.


        friends = 0
        for i in range(1, n+1):
            if((uf.find(1) == uf.find(i))):   #including Lea as first person count the alliances....
                friends = friends + 1
        if(n == 1):
            print('Case #{}: {}'.format(counter+1, 'yes'))
        elif friends > (n / 2):   #more than half
            print('Case #{}: {}'.format(counter+1, 'yes'))
        else:
            print('Case #{}: {}'.format(counter+1, 'no'))

        if(counter != (int(total_case)-1)):
            sys.stdin.readline()

