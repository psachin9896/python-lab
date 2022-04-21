""" creating to do class"""


class TODOreminder:
    def __init__(self, do_list=[]):
        self.do_list = do_list

    def List_todo(self):
        for index, new_do in enumerate(self.do_list):
            print("Index : {} do : {}".format(index,new_do))

    def new_todo(self,new_do):
        self.do_list.append(new_do)
        print("the new activity added to the list")

    def remove_todo(self, index):
        if 0 <= index <= len(self.do_list):
            self.do_list.pop(index)
            print("activity deleted from the list")
        else:
            print("invalid index")

if __name__ == "__main__":
    do = TODOreminder(["get fresh","workout","breakfast","work","lunch"])
    do.List_todo()
    do.new_todo("holiday sunday")
    do.List_todo()
    do.remove_todo(3)
    do.List_todo()