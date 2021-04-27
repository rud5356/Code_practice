class Stack(list):
    # 리스트 선언
    def __init__(self):
        self.stack = []

    # 이동할 페이지 담기
    def push(self, data):
        self.stack.append(data)
        print("{}번째 페이지로 이동합니다.".format(data))

    # 이전 페이지로 돌아가기
    def pop(self):
        if self.is_empty():
            return print("뒤로 갈 수 없습니다.")
        return print("{}번째 페이지에서 뒤로가기 버튼을 눌렀습니다.".format(self.stack.pop()))

    # 현재 페이지 확인
    def peek(self):
        return print("{}번째 페이지 입니다.".format(self.stack[-1]))

    # 리스트가 비었는지 확인
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()
    s.peek()
    s.push(4)
    s.pop()
    s.pop()
    s.pop()
    s.pop()

