# 자연어 처리 이용하기 
# NLP natural language process
# KoNLP 패키지 이용
# 총 3가지의 사전 1 시스템사전28만개 2 세종사전32만개 3 NIADIC사전 98만개
# java기능을 이용한다 시스템에 JRE가 시스템에 설치되어있어야 한다 !!!!!! 
# JRE 설치하긴 햇는데 R 패키지가 이걸 찾아서 쓸수 잇음? 어디에 있는지 알아야 찾아서 쓸수 있다. 
# R 패키지가 찾을수 있게 알려줘야대 

#참고로 영문 NLP openNLP, Snowball 패키지 이용 
install.packages("rJava")
library(rJava)
install.packages("KoNLP")
library(KoNLP)
useNIADic()
## 


## 데이터 불러들이기 
txt <- readLines("C:/Users/student/Documents/exer/hiphop.txt",encoding = "UTF-8")
head(txt)

## 특수문자 지우기
library(stringr)
txt <- str_replace_all(txt,"\\W", " ")
tail(txt)
## 혀태소를 분석할 준비가 되었다. 

## 함수를 이용해서 명사만 뽑아보자 
nouns <- extractNoun(txt)
head(nouns)
## 명사를 추출해서 리스트 형태로 저장 
# list 형태를 처리하기 쉬운 벡터형태로 변환
words <- unlist(nouns) # 우선 리스트를 풀어 
length(words)
#많이 등장하는 명사만 추출
wordcloud <- as.data.frame(table(words),stringsAsFactors = F) # 확인해보니 팩터로 들어가있어서 이거 해줘야 댄다
class(wordcloud)
View(wordcloud)
# 빈도수가 높은 상위 20개 단어들만 추출 한글자 짜리는 의미가 없다 .
wordcloud[50,1]
library(dplyr)
class(wordcloud$words)
word_df <- wordcloud %>% filter(nchar(words)>=2) %>% arrange(desc(Freq))

df
df <- head(word_df,30)
## 워드 클라우드 만들기
install.packages("wordcloud")
library(wordcloud)
## 워드 클라우드에서 사용할 색상에 대한 팔레트를 설정
# Dark2라는 색상목록에서 8개의 색상을 추출
pal <- brewer.pal(8,"Dark2")
#워드클라우드는 만들때마다 랜덤하게 만들어진다. 
# 재현성을 확보 할수 없다 
# 랜덤함수의 시드값을 고정시켜서 항상 같은 워드 클라우드가 만들어지게 설정
set.seed(111)
wordcloud::wordcloud(words = df$words,freq = df$Freq,min.freq = 2,max.words = 50,random.order = F,
                     rot.per = 0.3,scale = c(4,0.3),colors = pal) # 고빈도 단어를 중앙 배치 랜덤오더 rotper 전체갯수중에 비율로 몇개를 돌릴까 스케일은 글자 크기 벡터 범위 칼라는 팔레트








