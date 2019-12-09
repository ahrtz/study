## 셀레니움을 이용한 동적 데이터 크롤링
# 여태까지 실습한 것들과 차이점을 알아야 한다.
# 위에서 실습한 방법으로 데이터를 구축할 수 없는 상황이 있다.
# 우리가 작업한 상황은 -> 네이버 댓글 사이트 
# 클라이언트가 요청을 보내고 서버가 그 요청을 받아서 응답,결과 HTML페이지를 던져준다.
# 클라이언트는 셀렉터와 xpath를 이용해서 전달된 HTML내에 있는 필요한 데이터를 추출

# --> 카카오 이미지 검색 api (open api를 이용해서 데이터를 구축하는 방식), 영화진흥 위원회 openapi 
# 클라이언트가 request를 보내고 서버 프로그램이 요청을 받아 결과 JSON문자열을 생성해서 보내줌
# 이결과 데이터는 데이터 프레임으로 받는다 

# 이 두가지방식으로 해결 할 수 없는 상황 
## 클릭하면 프로그램을 돌리는 방식으로 데이터를 제공하는 것이라 클릭하기전에는 
## HTML 상에는 아무런 데이터도 존재하지 않아 데이터를 가져오기가 힘듬 

##--> OPEN aPI 를 사용하지 않는 (공개되지 않는 API 를 사용 )
## AJAX방식의 Web Page는 위의 방법으로 데이터를 가져올수 없다

### 이걸 하려면 셀리니움을 이용해서 크롤링을 해야한다

# 1. 셀레니움 서버 받기 
# 2. C:\Users\student\Documents\셀레니움 경로에 크롬 드라이버 받는다.
# 3. 내 컴퓨터 속성의 환경변수 에 path 에 새로운 환경 변수로 경로를 추가한다
# 4. 이 크롬 드라이버 프로그램을 셀레니움이 사용할 수 있도록 패스 환경변수에 경로를 설정 

###5. 셀레니움 서버 기동  <-  웹 서버라고 생각을 하면 편합니다. 
## Java -jar 파일명 -port 4445
## 셀레니움 기동 cmd 에서 셀레니움 있는 폴더로 경로 이동 한뒤 java -jar selenium-server-standalone-3.141.59.jar -port 4445
## 제공된 도서 검색 프로그램을 이용할 것
## MY SQL DBMS 시작 (mysqld)
## 이클립스 실행후 프로그램 웹에 deploy

## 셀레니움을 이용한 동적 페이지 스크래핑
## 셀레니움을 R에서 사용할수 잇도록 도와주는 패키지를 설치 
install.packages("RSelenium")
library(RSelenium)

# R프로그램이 셀레니움 서버에 접속한 후 리모트 드라이버 객체를 리턴ㄴ 받는다.
rem <- remoteDriver(remoteServerAddr="localhost",
             port=4445,
             browserName="chrome")

rem
## 접속이 성공하면 remoth driver를 이용해서
## chrome browser를 R code로 제어할수 있다.

rem$open()   # 크롬 브라우저 오픈 ## 가 끔 안되는 경우가 있는데 이땐 셀레니움 도스 창에서 엔터 쳐서 블락 풀어야 한다.
rem$navigate("http://localhost:8080/bookSearch/index.html")

inputBox <- rem$findElement(using = "css","[type=text]")
    # 입력상자를 찾기

inputBox$sendKeysToElement(list("여행"))
    # 찾은 입력상자에 검색어를 넣는다
    # 모르면 레퍼런스 에 다 나와있긴합니다.
#AJAX호출을 하기 위해 버튼을 먼저 찾아야 한다
btn <- rem$findElement(using = "css","[type=button]")

btn$clickElement()
# ajax호출이 발생해서 출력된 화면에서 필요한 내용을 추출
li_element <- rem$findElements(using = "css","li")

## 이렇게 얻어온 엘리먼트 각각에 대해서 함수를 호출
myList <- sapply(li_element,function(x){
  x$getElementText()
})
for (i in 1:length(myList)) {
  print(myList[[i]])
}
str(myList)


