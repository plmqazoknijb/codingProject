# 1.letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
letters = 'python'
print(letters[0],letters[2])

# 2.자동파 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
license_plate = "24가 2210"
print(license_plate[-4:])

# 3.아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
phone_number = "010-1111-2222"
a = phone_number.replace("-"," ") #원본을 남기고 새로운 변수에 바꿔주는 게 좋음
print(a)

# 4.url에 저장된 웹 페이지 주소에서 끝 글자만 출력하시오.
url = "http://sharebook.kr"
print(url[-2:])

# 5.변수에 다음과 같은 문자열이 바인딩되어 있습니다. 변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요
t1 = 'python'
t2 = 'java'
print((t1+" "+t2+" ")*4)

# 6.삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 수 이를 정수 타입으로 변환해보세요.
상장주식수 = "5,969,782,550"
a = 상장주식수.replace(',','')
print(int(a))

# 7.다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
ticker = "btc_krw"
a = ticker.split('_')
print(a)

# 8.movie_rank 리스트에 "배트멘"을 추가하라.
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
movie_rank.append("배트멘")
print(movie_rank)

# 9.movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다.
#"슈퍼맨"을 "닥터 스트레인지"와 "스플릿"사이에 추가하라.
movie_rank = ["닥터 스트레인지", "스플릿", "럭키","배트멘"]
movie_rank.insert(1,"슈퍼맨")
print(movie_rank)

# 10.movie_rank 리스트에서 '럭키'를 삭제하라.
movie_rank = ["닥터 스트레인지", "슈퍼맨","스플릿", "럭키","배트멘"]
movie_rank.remove("럭키")
print(movie_rank)

# 11.다음 리스트의 합을 출력하라.
nums = [1,2,3,4,5]
print(sum(nums))

# 12.다음 리스트에 저장된 데이터의 개수를 화면에 구하라.
# 1) 중복을 허용했을때의 갯수
cook = ["피자","김밥","만두","양념치킨","족발","피자","김치만두","쫄면","쏘세지","라면","팥빙수","김치전"]
print(len(cook))
# 2) 중복을 허용하지 않았을때의 갯수
a = set(cook)
print(len(a))

# 13.다음 리스트의 평균을 출력하라.
nums = [1,2,3,4,5]
a = sum(nums)/len(nums)
print(a)

# 14.슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라. # reverse() 원본이 바뀜
nums = [1, 2, 3, 4, 5]
nums.reverse()
print(nums)

# 14-2. 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
nums2 = [10,2,3,40,5]
#방법 1
nums2.reverse()
#방법 2
nums3 = [10,2,3,40,5]
a = list(reversed(nums3)) #원본이 바뀌지 않음
#방법 3
nums4 = [10,2,3,40,5]
b = nums4[::-1]
print(nums2)
print(a)
print(b)

# 15.interest 리스트에는 아래의 데이터가 바인딩되어 있다.
#interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
#출력 예시 : 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우
interest = ['삼성전자', 'LG전자', 'Naver','SK하이닉스','미래에셋대우']
# print(interest[0]+'/'+interest[1]+'/'+interest[2]+'/'+interest[3]+'/'+interest[4])
# 방법1
a = '/'.join(interest) #join은 문자열을 합해주는 것(원본유지)
print(a)

# 16.회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.
# 이를 interest 이름의 리스트로 분리 저장하라.
string = "삼성전자/LG전자/Naver"
interest = string.split('/')
print(interest)

# 17.리스트에 있는 값을 오름차순으로 정렬하세요,
data = [2,4,3,1,5,10,9]
# 방법 1 (원본 변경)
data.sort()
print(data)
#방법 2 (원본 유지)
data = [2,4,3,1,5,10,9]
a = sorted(data)
print(a)

# 18. 사용자로부터 입력 받은 시간이 정각인지 판별하라.
time = input("현재시간 입력(00:00): ")
# if time[-2:] == "00":
#     print("정각 입니다.")
# else:
#     print("정각이 아닙니다.")
result = time.split(":")
if result[-1] == "00":
    print("정각 입니다.")
else:
    print("정각이 아닙니다.")

# 19. 파일 이름이 저장된 리스트에서 확장하자 .h인 파일 이름을 출력하라.
f_list = ['intra.h', 'intra.c', 'define.h', 'run.py']
for a in f_list:
    split = a.split(".")
    if split[1] == "h":
        print(a)

# 20. for문을 사용해서 아래와 같이 출력하라
# for num in range(10):
#     print(num/10)
#다른 방법
for i in range(9+1):
    print(str(0.1*i)[:3])

# 21.리스트에 저장된 데이터를 아래와 같이 출력하라.
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
    for col in row:
        print(col,"호")

# 22.숫자로 구성된 하나의 리스트를 입력받아,
# 짝수들을 추출하여 리스트를 반환하는 pickup_even 함수를 구현하라.
def pickup_even(items):
    result = []
    for item in items:
        if item % 2 == 0:
            result.append(item)
    return result

