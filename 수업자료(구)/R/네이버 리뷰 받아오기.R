##web crawling: 인터넷 상에 있는 필요한 정보를 읽어와서 수집하는 일련의 작업 과정

## web scraping
##  하나의 웹페이지에서 내가 원하는 부분을 추출하는 행위 

## web crawling(web spidering)
## 자동화 봇인 크롤러가 정해진 규칙에 따라 복수개의 web page를 browsing 하는 행위 


## scraping 을 할때 CSS(jquery) selector를 이용해서 필요한 정보를 추출 
## selector를 이용해서 추출하기 힘든놈들도 있다. 
## 추가적으로 xpath도 이용해본다

## 특정사이트에서 해보자
#- naver 영화 댓글
# url: https://movie.naver.com/movie/point/af/list.nhn?&page=1
## 1. 서버로 부터 받은 흐트믈 태그로 구성된 문자열을 자료구조화 시키는 패키지를 이용해야한다.
  install.packages("rvest")
library(rvest)
  library(stringr)
## 2.url을 준비 
  
url <- "https://movie.naver.com/movie/point/af/list.nhn"
page <- 'page='
request_url <- str_c(url,"?",page,1)
request_url
## 3. 준비된 url로 서버에 접속해서 HTML을 읽어온후 자료 구조화 시킨ㄷㅏ.
html_page <- read_html(request_url)
html_page
## selector 를 이용해서 추출하기 원하는 요소(element) 선택

nodes = html_nodes(html_page,"td.title>a.movie")## a 는 anchor 
nodes
## 요소 사이에 들어있는 텍스트를 추출
title <-  html_text(nodes)        
title    

nodess = html_nodes(html_page,"td.title")
txt <- html_text(nodess,trim = T) ## trim 맨앞과 맨뒤의 공백 날리기 
txt
txt1 <- str_replace_all(txt,c("\n","\t"),"")
txt1
txt2 <- str_remove_all(txt,"\t")
txt3 <- str_remove_all(txt2,"\n")
review <- str_remove_all(txt3, "신고")

## 영화 제목과 리뷰에 대한 내용을 추출
df <- cbind(title,review,review1)
df
View(df)
review1 <- str_replace(review,title,"") ## 리뷰에 있는 제목부분 없애기
review2 <- str_remove(review,title)
review2

