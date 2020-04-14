from LRU import LRUCache
class LRUTest:
    def __init__(self):
        pass
    def testingmethod(self):
        obj = LRUCache(4)
        a = [1,2,3,4,6,8]
        for i in a:
            obj.put(i)
        assert obj.get_cache()== [3,4,6,8], "testcase1 failed"
        print("Testcase 1 Passed")
        a = [4,1,2,8,6]
        for i in a:
            obj.put(i)
        assert obj.get_cache()== [1,2,8,6], "testcase2 failed"
        assert obj.get() == 1,"testcase2 failed"
        print("Testcase 2 Passed")
        a = [1,2,1,3,2,3,4,5,4]
        for i in a:
            obj.put(i)
        assert obj.get_cache()== [2,3,5,4], "testcase3 failed"
        assert obj.get() == 2, "testcase3 failed"
        print("Testcase 3 Passed")
        print("All Testcases Passed")

if __name__=="__main__":
    obj1 = LRUTest()
    obj1.testingmethod()

