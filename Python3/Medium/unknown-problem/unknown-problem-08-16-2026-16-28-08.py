class Solution:
    def findPages(self, nums, m):
        
        if m > len(nums):
            return -1

        def isPossible(maxPage, nums, m):
            currPage = 0
            studentsCount = 1

            for num in nums:
                if (currPage + num) > maxPage:
                    studentsCount += 1
                    currPage = num
                else:
                    currPage += num

                if studentsCount > m:
                    return False

            return True

        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = left + (right - left) // 2

            if isPossible(mid, nums, m):
                right = mid
            else:
                left = mid + 1

        return left
