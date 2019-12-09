### 네이버 영화 댓글 사이트 특정 영화에 대한 리뷰를 크롤링해서 워드클라우드 만들자 
library(rvest)
library(stringr)

url <-"https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=182205&target=after"
page <- 'page='
df=c()
for (i in 1:10) {

  request_url <- str_c(url,"&",page,i)
  request_url <- URLencode(request_url)
  html_page <- read_html(request_url,encoding = "CP949")


  nodes = html_nodes(html_page,"td.title>a.movie")
  nodes
  title <-  html_text(nodes)        
  title    


  nodess = html_nodes(html_page,"td.title")
  txt <- html_text(nodess,trim = T) 

  txt1 <- str_replace_all(txt,c("\n","\t"),"")

  txt2 <- str_remove_all(txt,"\t")
  txt3 <- str_remove_all(txt2,"\n")
  review <- str_remove_all(txt3, "신고")
  review <- str_remove_all(review,title)
  
  df <- rbind(df,review)
  
  }

df

df1 <- as.data.frame(df,stringsAsFactors = F)

nouns1 <- unlist(df1)
View(nouns1)
nouns2 <- extractNoun(nouns1)
View(nouns2)
movie_df <- unlist(nouns2)
movie_df <- as.data.frame(table(movie_df),stringsAsFactors = F)
View(movie_df)
movieword_df <- movie_df %>% filter(nchar(movie_df)>=2) %>% arrange(desc(Freq))
head(movieword_df,30)

wordcloud::wordcloud(words = movieword_df$movie_df,freq = movieword_df$Freq,min.freq = 2,max.words = 50,random.order = F,
                     rot.per = 0.3,scale = c(4,0.3))
