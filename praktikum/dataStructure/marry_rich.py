import  sys

class UF:
    """An implementation of union find data structure.
    It uses weighted quick union by rank with path compression.
    """

    def __init__(self, N):
        self._id = list(range(N+1))
        self._rank = [0] * (N+1)

    def find(self, x):
        p = self._id[x]
        while p != self._id[p]:
            # path compression
            q = self._id[p]
            self._id[p] = self._id[q]
            p = q
        return p


    def union(self, p, q):
        id = self._id
        rank = self._rank

        i = self.find(p)
        j = self.find(q)
        if i == j:
            return

        if rank[i] < rank[j]:
            id[i] = j
        elif rank[i] > rank[j]:
            id[j] = i
        else:
            id[j] = i
            rank[i] += 1


if __name__ == "__main__":
    total_case = sys.stdin.readline()
    for counter in range(int(total_case)):

        int_line = list(map(int, sys.stdin.readline().split()))
        if(int_line[0] == 1):
            sys.stdin.readline()

            for i in range(int_line[1]):
                sys.stdin.readline()
            for i in range(int_line[2]):
                sys.stdin.readline()
            print('Case #{}: {}'.format(counter+1, 'impossible'))

        else:
            uf = UF(int_line[0])
            richness_list = list(map(int,sys.stdin.readline().split()))
            ranked_list = sorted(range(len(richness_list)), key=richness_list.__getitem__)

            every_married_person_list =  [None]*(int_line[0]+1)
            for i in range(int_line[1]):
                relatives = list(map(int, sys.stdin.readline().split()))
                uf.union(relatives[0],relatives[1])

            for i in range(int_line[2]):
                married_ones = list(map(int, sys.stdin.readline().split()))
                uf.union(married_ones[0],married_ones[1])
                every_married_person_list[married_ones[0]] = 1
                every_married_person_list[married_ones[1]] = 1

            check = False
            for i in range(len(ranked_list)-1,-1,-1):
                if((uf.find(ranked_list[i]+1) != uf.find(int_line[0])) and (every_married_person_list[ranked_list[i]+1] != 1)):
                    print('Case #{}: {}'.format(counter+1, richness_list[(ranked_list[i])]))
                    check=True
                    break
            if(check == False):
                print('Case #{}: {}'.format(counter+1, 'impossible'))



        if(counter != (int(total_case)-1)):
                sys.stdin.readline()


