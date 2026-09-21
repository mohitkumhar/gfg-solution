class Solution:
    def floodFill(self, image, sr, sc, newColor):
        n = len(image)
        m = len(image[0])

        oldColor = image[sr][sc]

        if oldColor == newColor:
            return image

        def dfs(r, c):
            image[r][c] = newColor

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < n and 
                    0 <= nc < m and 
                    image[nr][nc] == oldColor):

                    dfs(nr, nc)

        dfs(sr, sc)

        return image