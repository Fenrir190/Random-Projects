class BubbleSort:
    list

    def sort(self, list):
        if len(list) > 1:
            for j in range( len(list)-1, 0, -1):
                for i in range (j):
                    if list[i] > list[i+1]:
                        list[i], list[i+1]=list[i+1], list[i]

            self.deepCopy(list)

    def getList(self):
        return self.list

    def deepCopy(self, list):
        self.list = [None] * len(list)
        for i in range(len(list)):
            self.list[i] = list[i]
