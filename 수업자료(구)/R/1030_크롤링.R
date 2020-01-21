#R 에서 json 데이터 처리

# 네트워크를 통해서 데이터를 받아서 데이터 프레임으로 만들기 위해 
#패키지를 이용해보자 
install.packages("jsonlite") ## json 데이터이용하기 위한 라이브러리
install.packages("httr") ## curl 같은 인터넷 관련 명령어 라이브러리
library(jsonlite)
library(httr)
# 문자열 처리하기 위한 패키지
library(stringr)

#접속할 주소가 필요 

url <- "http://localhost:8080/bookSearch/search?keyword="

request_url <- str_c(url,
                     scan(what=character()))
request_url <-  URLencode(request_url)  # 한글처리
request_url
# 주소에서 데이터 프레임에 제이슨 데이터 넣기
df <- fromJSON(request_url)
df[1,2]
View(df)
str(df) # df의 구조를 파악
names(df) # column 의 이름을 알아보는 함수 
# 찾은 도서 제목만 콘솔에 출력 
c <- c()
for (idx in 1:nrow(df)) {
  c <- append(c,df[idx,2],idx)
## print(df$title[idx])            
}
c
substr(c[2],1,2)
## data frame 을 csv형식으로 file에 저장
write.csv(df,file = "C:/R_EXER/data/exercise.csv",row.names = F,quote = F
            ) # quote 는 따옴표 빼기 <- 문제가 생길 수 있다 (특정항목에 , 가 들어가 있을때 뒤의 것과 구분이 안댐)

#JSON 문자열을 직접 이용하고 싶을때 
#데이터 프레임을 JSON으로 변경하려면??
df_json <- toJSON(df)
df_json
prettify(df_json) ## 이쁜 제이슨
write(df_json,file = "C:/R_EXER/data/exercise.txt" )
write(prettify(df_json),file = "C:/R_EXER/data/exercise.txt" ) #이쁜 제이슨이 파일에 들어가게 된다


#연습문제 2018년 10월 30일 박스오피스 순위를 알아내서 제목과 누적관람객수를 CSV파일로 저장