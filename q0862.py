"""
862. Shortest Subarray with Sum at Least K

https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.

"""



class Solution:
    def shortestSubarray(self, A: list, K: int) -> int:

        def shortest_sub(left, min_len):
            if left>=len(A):
                return min_len
            while A[left] <= 0:
                left += 1
                if left == len(A):
                    return min_len

            right, curr_sum = left, 0
            while right < len(A):
                curr_sum += A[right]

                if right - left + 1 >= min_len:
                    left = right - min_len + 2
                    return min(min_len, shortest_sub(left, min_len))

                if curr_sum >= K:
                    left, curr_sum_right = right, A[right]
                    while curr_sum_right < K:
                        left -= 1
                        curr_sum_right += A[left]
                    min_len = min(min_len, right - left + 1)
                    if min_len == 2:
                        return 2

                    left += 2
                    return min(min_len, shortest_sub(left, min_len))

                if curr_sum <= 0:
                    left = right + 1
                    return min(min_len, shortest_sub(left, min_len))

                right += 1

            return min_len

        if max(A) >= K:
            return 1
        min_len = shortest_sub(0, len(A)+1)
        if min_len>len(A):
            min_len = -1

        return min_len


import collections
class Solution1():
    def shortestSubarray(self, A, K):
        N = len(A)
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        #Want smallest y-x with Py - Px >= K
        ans = N+1 # N+1 is impossible
        monoq = collections.deque() #opt(y) candidates, represented as indices of P
        for y, Py in enumerate(P):
            #Want opt(y) = largest x with Px <= Py - K
            while monoq and Py <= P[monoq[-1]]:
                monoq.pop()

            while monoq and Py - P[monoq[0]] >= K:
                ans = min(ans, y - monoq.popleft())

            monoq.append(y)

        return ans if ans < N+1 else -1


class Solution2():
    def shortestSubarray(self, A, K):
        N = len(A)
        P = 0

        # Want smallest y-x with Py - Px >= K
        ans = N + 1  # N+1 is impossible
        monoq = collections.deque()  # opt(y) candidates, represented as indices of P
        monoq.append((-1,0))
        for y, Py in enumerate(A):
            P += Py
            # Want opt(y) = largest x with Px <= Py - K
            while monoq and P <= monoq[-1][1]:
                monoq.pop()

            while monoq and P - monoq[0][1] >= K:
                ans = min(ans, y - monoq.popleft()[0])

            monoq.append((y,P))

        return ans if ans < N + 1 else -1


A = [1,2,3,-1,-1,5]
A = [84, -37, 32, 40, 95]
A = [-34,37,51,3,-12,-50,51,100,-47,99,34,14,-13,89,31,-14,-44,23,-38,6]
A = [-28,81,-20,28,-29]
A, K = [39353,64606,-23508,5678,-17612,40217,15351,-12613,-37037,64183,68965,-19778,-41764,-21512,17700,-23100,77370,64076,53385,30915,18025,17577,10658,77805,56466,-2947,29423,50001,31803,9888,71251,-6466,77254,-30515,2903,76974,-49661,-10089,66626,-7065,-46652,84755,-37843,-5067,67963,92475,15340,15212,54320,-5286], 207007

# A, K = [48,99,37,4,-31], 140
A = [58701,23101,6562,60667,20458,-14545,74421,54590,84780,63295,33238,-10143,-35830,-9881,67268,90746,9220,-15611,23957,29506,-33103,-14322,19079,-34950,-38551,51786,-48668,-17133,5163,15122,5463,74527,41111,-3281,73035,-28736,32910,17414,4080,-42435,66106,48271,69638,14500,37084,-9978,85748,-43017,75337,-27963,-34333,-25360,82454,87290,87019,84272,17540,60178,51154,19646,54249,-3863,38665,13101,59494,37172,-16950,-30560,-11334,27620,73388,34019,-35695,98999,79086,-28003,87339,2448,66248,81817,73620,28714,-46807,51901,-23618,-29498,35427,11159,59803,95266,20307,-3756,67993,-31414,11468,-28307,45126,77892,77226,79433]
K = 1677903

# A = [-32663,-36605,66224,14387,51418,30434,18347,98126,-8323,-33339,36769,79109,-23194,-9896,67990,-11414,-4629,21792,46755,84877,69128,-49061,79216,28735,42774,92620,49628,77186,86172,87886,77863,90207,-8642,52710,-2221,-19651,68274,85289,50032,-20487,-21518,5867,76156,79318,58624,74509,47490,96533,63340,-26205,62570,43318,62258,65898,72308,-4536,85462,-22971,84011,40816,98631,73874,-44803,-1863,79146,64637,-31262,-37111,26479,15333,-6392,-42227,-4596,71074,98010,10609,88515,-36203,-6087,44768,25376,-11025,-32826,-6889,90927,-9759,39030,70514,-36421,-45273,-22980,62053,68468,31482,61252,-32358,96048,65501,262,32984,39182,89456,-37285,-26053,-47849,-45674,31648,-20823,29201,29363,70671,27055,-7152,87069,28713,20524,-16507,54688,59947,-34498,2709,12151,-1395,11753,37325,22406,25442,92564,27639,25404,76775,-31229,-29244,13736,29311,-3334,-43343,41178,-5592,79878,83255,23786,83600,92902,53247,68574,9199,94982,-36745,60559,22932,76757,49138,-31452,-13742,68171,3643,-46488,86521,77094,18059,994]
# K = 663610288
# A,K = [1],1
print(Solution2().shortestSubarray(A,K))
