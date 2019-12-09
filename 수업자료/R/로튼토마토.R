##https://www.rottentomatoes.com/top/bestofrt/?year=2019
## 2019 가장 인기 있는 영화 100 개 에 대해 
## 영화 제목, user rating ,Genre ,부분 추출해서 Data Frame 만들고 파일로 출력
library(rvest)
library(stringr)
url <- "https://www.rottentomatoes.com/top/bestofrt/?year=2019"
html_page <- read_html(url)
html_page
nodes_name  <-  html_nodes(html_page,"td>a.unstyled.articleLink")
nodes_name
title <-  html_text(nodes_name,trim = T) 
title
nodes_address <- html_attr(nodes_name,'href')
df <- data.frame()
##### 포문 준비
for (i in 1:length(title)) {
  
  

  url_det <- "https://www.rottentomatoes.com"
  request_url <- str_c(url_det,nodes_address[i])

  html_moviepage <- read_html(request_url)
  nodes_movie <- html_nodes(html_moviepage,"#topSection > div.col-sm-17.col-xs-24.score-panel-wrap > div.mop-ratings-wrap.score_panel.js-mop-ratings-wrap > section > section > div.mop-ratings-wrap__half.audience-score > div > strong")
  user_Rating <- html_text(nodes_movie,trim = T)
  user_Rating
  nodes_exp <- html_nodes(html_moviepage,"#movieSynopsis")
  nodes_exp
  nodes_genre <- html_nodes(html_moviepage,"div.meta-value")
  genre <- html_text(nodes_genre,trim = T)
  genre <- str_remove_all(genre[2],"\n")
  genre <- str_replace_all(genre," ","")
  genre
  df <- rbind(df,cbind(user_Rating,genre))
  
}
title<-as.data.frame(title)
df2 <- cbind(title,df)
View(df2)
