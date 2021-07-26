def is_id_valid(user_data):
    val=None
    for word in user_data['password']:
        try:
            int(word)

        except:
            val = False
        else:
            return True
    return val


        
#     # 여기에 코드를 작성합니다.
    
        
a= 'av21'

for i in a:
    if '0'<=i<='9':
        print("숫자")

# # 아래의 코드는 수정하지 않습니다.
# if __name__ == '__main__':
#     user_data1 = {
#         'id': 'jungssafy5',
#         'password': 'as',
#     }
#     print(is_id_valid(user_data1)) 
#     # True
    
#     user_data2 = {
#         'id': 'kimssafy!',
#         'password': '1q2w3e4r',
#     }
    
#     # False


a= '1234'
for i in a:
    print(type(i))