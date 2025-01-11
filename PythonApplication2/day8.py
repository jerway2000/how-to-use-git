# coding=utf-8
# 1、完成二叉树的建树，前序，中序，后序，层序遍历
class node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def build_tree_by_level(root, list1, depth=0):
    if depth >= len(list1):
        return
    root = node(list1[depth])
    root.left = build_tree_by_level(root.left, list1, 2*depth+1)
    root.right = build_tree_by_level(root.right, list1, 2*depth+2)
    return root

def print_tree_by_preorder(root):
    if root is None:
        return
    print(root.data)
    print_tree_by_preorder(root.left)
    print_tree_by_preorder(root.right)

def print_tree_by_inorder(root):
    if root is None:
        return
    print_tree_by_inorder(root.left)
    print(root.data)
    print_tree_by_inorder(root.right)

def print_tree_by_postorder(root):
    if root is None:
        return
    print_tree_by_postorder(root.left)
    print_tree_by_postorder(root.right)
    print(root.data)

def print_tree_by_levelorder(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop(0)
        print(node.data)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

# 2、完成sorted的练习

# 3、完成快速排序，堆排序
def quick_sort(list1):
    def partition(list1, low, high):
        i = low - 1
        pivot = list1[high]
        for j in range(low, high):
            if list1[j] < pivot:
                i += 1
                list1[i], list1[j] = list1[j], list1[i]
        list1[i+1], list1[high] = list1[high], list1[i+1]
        return i+1
    def quick_sort1(list1, low, high):
        if low < high:
            pi = partition(list1, low, high)
            quick_sort1(list1, low, pi-1)
            quick_sort1(list1, pi+1, high)
    quick_sort1(list1, 0, len(list1)-1)
    return list1

   
def heap_sort(list1):
    def heapify(list1, n, i):
        largest = i
        l = 2*i+1
        r = 2*i+2
        if l < n and list1[l] > list1[largest]:
            largest = l
        if r < n and list1[r] > list1[largest]:
            largest = r
        if largest != i:
            list1[i], list1[largest] = list1[largest], list1[i]
            heapify(list1, n, largest)
    n = len(list1)
    for i in range(n//2, -1, -1):
        heapify(list1, n, i)
    for i in range(n-1, 0, -1):
        list1[i], list1[0] = list1[0], list1[i]
        heapify(list1, i, 0)
    return list1


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6, 7]
    root = node(1)
    root = build_tree_by_level(root, list1)
    print_tree_by_preorder(root)
    print_tree_by_inorder(root)
    print_tree_by_postorder(root)
    print_tree_by_levelorder(root)
    tpuple1=[(1,2),(2,3),(3,4)]
    tpuple1.sort(key=lambda x:x[1])
    print(tpuple1)
    list2=[3,2,1,4,5,6,7]
    quick_sort(list2)
    print(list2)
    list3=[3,2,1,4,5,6,7]
    heap_sort(list3)
