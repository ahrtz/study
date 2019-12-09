## xpath는 좀더 세밀하게 할 수 있다. (셀렉터 사용한다고 이해하시면 편합니다.)
install.packages("rvest")
library(rvest)
library(stringr)

url <- "https://movie.naver.com/movie/point/af/list.nhn"
page <- 'page='
request_url <- str_c(url,"?",page,1)
html_page <- read_html(request_url)
nodes = html_nodes(html_page,"td.title>a.movie")# 셀렉터를 통해서 가져온거기 때문에 그대로 사용할겁니다.
#review 부분은 xpath 로 가져와 보자
nodesss = html_nodes(html_page,
                     xpath ='//*[@id="old_content"]/table/tbody/tr[1]/td[2]/text()') 
review3 <- vector(mode = "character",length = 10)
for (idx in 1:10) {
  mypath= str_c('//*[@id="old_content"]/table/tbody/tr[',idx,']/td[2]/text()') 
  nodesss = html_nodes(html_page,
                       xpath = mypath)
  review6 <- html_text(nodesss,trim = T)
  review3[idx] <- review6[3]
}

review6 <- html_text(nodesss,trim = T)
review3
####
result_df <- data.frame()
# 반복하여 page를 브라우징 하는 크롤링까지 해보자
extract_comment <- function(num){
  url <- "https://movie.naver.com/movie/point/af/list.nhn"
  page <- 'page='
  request_url <- str_c(url,"?",page,num)
  html_page <- read_html(request_url,encoding = "CP949")## cp949 는 옛날 한글 인코딩
  nodes = html_nodes(html_page,"td.title>a.movie")
  title <-  html_text(nodes)        
  
  review3 <- vector(mode = "character",length = 10)
  for (idx in 1:10) {
    mypath= str_c('//*[@id="old_content"]/table/tbody/tr[',idx,']/td[2]/text()') 
    nodesss = html_nodes(html_page,
                         xpath = mypath)
    review6 <- html_text(nodesss,trim = T)
    review3[idx] <- review6[3]
  }
  
  
  review6 <- html_text(nodesss,trim = T)
  review3
  df <-  cbind(title,review3)
  return(df)

}



for (i in 1:10){
  tmp <- extract_comment(i)
  result_df <- rbind(result_df,tmp)
  
}## 이유를 알수 없지만 40번까지만 가능


View(result_df)

