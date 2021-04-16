with open("basic.txt", "r") as file:
    contents = file.read()
print(contents)


#데이터를 한줄씩 읽어들일 떄는 for 반복문을 다음과 같이 사용
# for 한 줄을 나타내는 문자열 in 파일객체:
#     처리

# 구문오류(SyntaxError)
# 프로그램 실행 전에 발생하는 오류
# 런타임 오류 (RuntimeError)/예외(Exception)
# 프로그램 실행 중에 발생하는 오류

list_input_a = ["52","273","32","스파이","183"]

list_number = []
for item in list_input_a:

    try:
        float(item) #예외가 발생하면 알아서 다음으로 진행은 안되겠지?
        list_number.append(item) #예외없이 통과했으면 리스트에 넣어줘

    except:
        pass
print("{} 내부에 있는 숫자는".format(list_input_a))
print("{} 입니다.".format(list_number))

# try:예외가 발생할 가능성이 있는 코드 
# except:예외가 발생했을때 실행할 코드
# else:예외가 발생하지 않았을떄 실행할 코드 (except 구문 뒤에 사용)
# finally: 무조건 실행할 코드
# try구문은 단독으로 사용할수 없으며 
# 반드시 except 구문  finally 구문과 함꼐 사용해야함





