import queue

que = queue.Queue()
def put(data):
    que.put(data)
    return print("앞에 {}명의 사람이 있습니다.".format(que.qsize()))

def get():
    que.get()
    return print("앞에 {}명의 사람이 있습니다.".format(que.qsize()))

if __name__ == "__main__":
    for i in range(4):
        put(i)
    for j in range(4):
        get()
    put(5)
    get()

