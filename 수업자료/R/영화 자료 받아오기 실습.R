
#연습문제 2018년 10월 30일 박스오피스 순위를 알아내서 제목과 누적관람객수를 CSV파일로 저장

library(jsonlite)
library(stringr)
library(ggplot2)
request_url <- "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=d93a43233a59ba9e241e833c89126e87&targetDt=20191029"

df <- fromJSON(request_url)
df
df_new
df_new <- df[[1]][[3]] ##1
View(df_new)
c_Name <- c()
c_aud <- c()
for (idx in 1:nrow(df_new)) {
  c_Name <- append(c_Name,df[[1]][[3]]$movieNm[idx])
  c_aud <- append(c_aud,df[[1]][[3]]$audiAcc[idx])
}

c_Name
c_aud
report <- rbind(c_Name,c_aud)
report
str(report)
write.csv(report,file = "report.csv",quote = F)
########################
df_nnew <- df$boxOfficeResult$dailyBoxOfficeList ##1 
df_nnew
str(df_nnew)
df_nnew$audiCnt[4]
newdf <- data.frame(2,1:nrow(df_nnew))
for (idx in 1:nrow(df_nnew)) {
  newdf[[1]][[idx]] <-  df_nnew$movieNm[idx]
  newdf[[2]][[idx]] <- df_nnew$audiCnt[idx]
  }
names(newdf)
names(newdf)[1]
names(newdf)[1] <- "영화명"
names(newdf)[2] <- "누적관객"
str(newdf)
View(newdf)
newdf

