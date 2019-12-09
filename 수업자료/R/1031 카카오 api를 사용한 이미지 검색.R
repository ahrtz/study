## 1031 데이터 수집과 구축

## KAKAO API 이미지 검색(키워드로 이미지 검색) + 찾은 이미지 파일로 저장
## 셀레니움을 이용한 동적 데이터 크롤링
## 공공데이터 포탈 (www.data.or.kr)이용


######################################
#카카오 API를 이용해서 찾고 저장해보기

# 사용하는 패키지는
# 네트워크 연결을 통해 서버에 접속한후 결과를 받아올때 사용하는 
install.packages("httr")
library(httr) # jjsonlite 은 httr 을 이용해 만든 상위 패키지 (더 좋은 더 편리한 )
library(stringr)
# open api의 주소를 알아야 호출한다
# 검색창에 카카오 디벨로퍼
url <- "https://dapi.kakao.com/v2/search/image"

keyword <- "query=아이유" # 한글 처리를 위해선 인코딩이 필요하다

request_url <- str_c(url,
                     "?",
                     keyword)
request_url <- URLencode(request_url)
request_url#  API호출 주소를 만들엇다네 
# open api를 사용할때 거의 대부분 인증절차를 거쳐야 사용할 수 있다.
apikey <- "bd13a831df7e6f4e281e13ac68318df1"
#웹에서 클라이언트가 서버쪽 프로그램을 호출할때 호출방식이라는것이 존재한다.
#4가지 방식이 존재 
# GET POST PUT DELETE <- 다 이용하면REST라고한다
# 우리는 두개 GET,POST만 이용한다
# GET 방식 : 서버 프로그램을 호출할때 전달 데이터를 URL뒤에 붙여서 전달
# POST 방식: 서버 프로그램을 호출할때 전달 데이터가 request header에 붙어서 전달
result <- GET(request_url,
    add_headers(
      Authorization=paste("KakaoAK",
                          apikey)))
#stackoverflow 나 어디서 잘 검색해보세요
http_status(result)     # 썸네일 검색해보기 
result_data <- content(result)
View(result_data)
length(result_data$documents)
img_url <- vector()
for (idx in 1:length(result_data$documents)) {
  img_url[idx] <- result_data$documents[[idx]]$thumbnail_url
}
for (idx in 1:length(result_data$documents)) {
  img_url <- result_data$documents[[idx]]$image_url
  sav_img <- GET(img_url)  # 이미지 데이터 바이너리 형태로 들어온다
  imgData <- content(sav_img,"raw") #결과로 받은 이미지를 raw형태로 추출 그림형태
  writeBin(imgData,
           paste("C:/R_EXER/imgdata/img",idx,".png")
  )
  }
