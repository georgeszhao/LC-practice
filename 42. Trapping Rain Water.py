class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) == 0:
            return 0
        left, right = [height[0]] * len(height), [height[-1]] * len(height)
        ans, cur_max = 0, height[0]
        for i in range(1, len(height)):
            left[i] = max(cur_max, height[i])
            cur_max = max(cur_max, height[i])
        cur_max = height[-1]
        for i in range(len(height) - 2, -1, -1):
            right[i] = max(cur_max, height[i])
            cur_max = max(cur_max, height[i])
        for i in range(1, len(height) - 1):
            trapped_water = min(left[i], right[i]) - height[i]
            if trapped_water:
                ans += trapped_water
        return ans

def execute() -> object:
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    sol = Solution()
    print(sol.trap(height))

if __name__ == "__main__":
    execute()

    
    
# # Javascript solution.    
# var trap = function(height) {
#     if (height === null || height.length === 0 || height.length < 3) return 0;

#     let max = 0,
#         leftmax = 0,
#         rightmax = 0,
#         left = 0,
#         right = height.length - 1;

#     while (left < right) {
#         leftmax = Math.max(leftmax, height[left]);
#         rightmax = Math.max(rightmax, height[right]);

#         if (leftmax < rightmax) {
#             max += leftmax - height[left];
#             left++;
#         } else {
#             max += rightmax - height[right];
#             right--;
#         }
#     }
#     return max;
# };
