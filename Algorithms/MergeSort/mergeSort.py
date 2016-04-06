class mergeSort:
    items = []

    def sort(self, items):
        print("Begining split ", items)
        if len(items) > 1:
            mid = len(items)//2
            leftHalf = items[:mid]
            rightHalf = items[mid:]

            print("Sorting left side")
            self.sort(leftHalf)

            print("sorting right side")
            self.sort(rightHalf)

            i=0
            j=0
            k=0

            while i < len(leftHalf) and j < len(rightHalf):
                print("Comparing " + str(leftHalf[i]) + " < " + str(rightHalf[j]))
                if leftHalf[i] < rightHalf[j]:
                    items[k] = leftHalf[i]
                    i+=1
                else:
                    items[k] = rightHalf[j]
                    j+=1
                k+=1

            while i < len(leftHalf):
                print("adding remainder of left half: ", leftHalf)
                items[k] = leftHalf[i]
                i+=1
                k+=1
            while j < len(rightHalf):
                print("adding remainder of right half: ", rightHalf)
                items[k] = rightHalf[j]
                j+=1
                k+=1
        print("Merging ", items)

        self.items = items;

    def getItems(self):
        return self.items
