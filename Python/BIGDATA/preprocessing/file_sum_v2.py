import pandas as pd

def event_file_sum():
    filename = ['accident.csv', 'construction.csv', 'etc.csv', 'event.csv', 'trafficJam.csv', 'weather.csv']
    # 디렉토리 개수 입력
    processed_data_v2 = pd.DataFrame(columns=['지역', 'ID', '날짜', '형태', '내용'])
    for i in range(3, 7):
        file_path_read = f"D:/practice/{i}/"
        for j in range(0, len(filename)):
            if j == 0:
                processed_data = pd.read_csv(file_path_read+filename[j], names= ['지역', 'ID', '날짜', '형태', '내용'], header=None, skiprows=[0], encoding='cp949')
            else:
                data = pd.read_csv(file_path_read+filename[j],names= ['지역', 'ID', '날짜', '형태', '내용'],header=None, skiprows=[0], encoding='cp949')
                processed_data = pd.concat([processed_data, data])
        processed_data_v2 = pd.concat([processed_data_v2, processed_data])
    processed_data_sorted = processed_data_v2.sort_values(by=['날짜'])
    processed_data_sorted.to_csv("D:/practice/yuna/event_merge.csv",index=False, encoding='cp949')


def message_file_sum():
    filename = 'message.csv'
    processed_data = pd.DataFrame(columns=['지역', 'ID', '날짜', '내용'])
    for i in range(4, 7):
        file_path_read = f"D:/practice/{i}/"
        data = pd.read_csv(file_path_read+filename,names= ['지역', 'ID', '날짜', '내용'],header=None, skiprows=[0], encoding='cp949')
        # 중복내용삭제
        data = data.drop_duplicates(['지역','ID', '날짜', '내용'])
        processed_data = pd.concat([processed_data, data])
    processed_data_sorted = processed_data.sort_values(by=['날짜'])
    processed_data_sorted.to_csv("D:/practice/yuna/message_merge.csv",index=False, encoding='cp949')



if __name__ == '__main__':
    event_file_sum()
    message_file_sum()
