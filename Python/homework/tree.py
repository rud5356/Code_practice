INT_MAX = 4294967296
INT_MIN = -4294967296


# 이진 트리 노드
class Node:
    # 새로운 노드를 만듦
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# 주어진 트리가 이진 트리이면 True 반환
def isBST(node):
    return isBSTUtil(node, INT_MIN, INT_MAX)


# 주어진 트리가 이진 탐색 트리이고 해당 값인 경우 True 반환
# >= min and <= max
def isBSTUtil(node, mini, maxi):
    # 빈 트리인 경우 True 반환
    if node is None:
        return True

    # 노드가 최소/최대 제약 조건을 위반하는 경우 False 반환
    if node.data < mini or node.data > maxi:
        return False

    # 위의 경우에 해당되지 않는다면 트리를 반복적으로 확인
    return (isBSTUtil(node.left, mini, node.data - 1) and
            isBSTUtil(node.right, node.data + 1, maxi))


# main
if __name__=='__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.left.right.left = Node(9)

    print("이진 탐색 트리가 맞습니다.") if isBST(root) else print("이진 탐색 트리가 아닙니다.")
