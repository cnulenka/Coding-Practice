class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        def isCyclic(currCourse):
            nonlocal courseDict, checked, path
            
            if checked[currCourse]:
                return False
            
            if path[currCourse]:
                return True
            
            path[currCourse] = True
            
            for neigh in courseDict[currCourse]:
                if isCyclic(neigh):
                    return True
            
            path[currCourse] = False
            checked[currCourse] = True
            
            return False
        
        from collections import defaultdict
        courseDict = defaultdict(list)

        for relation in prerequisites:
            courseDict[relation[1]].append(relation[0])
            
        checked = [False] * numCourses
        path = [False] * numCourses
        
        for i in range(numCourses):
            if isCyclic(i):
                return False
        
        return True