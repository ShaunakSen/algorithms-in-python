class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        myList = nums
        for i in range(len(myList) - 1):
            if myList[i] == 0:
                myList.append(myList[i])
                myList[i] = ''

        for x in range(0, len(myList)):
            if myList[x] == '':
                myList.pop(x)

        return


def main():
    soln = Solution()
    myList = [0,0]
    soln.moveZeroes(myList)
    print myList


main()
