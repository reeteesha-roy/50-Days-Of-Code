from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # The center appears in every edge
        first_edge = edges[0]
        second_edge = edges[1]
        
        # The common node between first two edges must be the center
        if first_edge[0] == second_edge[0] or first_edge[0] == second_edge[1]:
            return first_edge[0]
        else:
            return first_edge[1]
