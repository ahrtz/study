# data : excel 파일(exec1105.xlsx)

# 만약 결측값이 존재하면 결측값은 결측값을 제외한 
# 해당 과목의 평균을 이용합니다.
library(xlsx)
# 만약 극단치가 존재하면 하위 극단치는 극단치값을 제외한
# 해당 과목의 1사분위 값을 이용하고 상위 극단치는
# 해당 과목의 3사분위 값을 이용합니다.
df_1 <- read_excel( "C:/Users/student/Documents/R/1105/exec1105.xlsx",sheet = 1,col_names = F)
df_2 <- read_excel("C:/Users/student/Documents/R/1105/exec1105.xlsx",sheet =2,col_names = F)


View(df_1)
View(df_2)
df_1_1 <- dcast(df_1,formula = ...1 ~...)

summary(df_1_1[2])[5]
min(df_1_1)
is.na(df_1_1)
df_1_1$math[is.na(df_1_1$math)] <- mean(df_1_1$math,na.rm = T)


quantile(df_1_1$eng)
quantile(df_1_1[,2])[4]

IQR(df_1_1[,2])

for (idx in 2:(length(ls(df_1_1))+1)) {
  df_1_1[idx] <- ifelse(min(df_1_1[,idx])==df_1_1[,idx],
                        quantile(df_1_1[,idx])[2]
                        ,df_1_1[,idx])
  
  df_1_1[idx] <- ifelse(max(df_1_1[,idx])==df_1_1[,idx],
                        quantile(df_1_1[,idx])[4]
                        ,df_1_1[,idx])
  
}
names(result)[2] <- c("name")

names(result)[3] <- c("gender")
result <- left_join(df_2,df_1_1)
result
df_2 <- rename(df_2, 3 = "gender")
result<- rename(result, ...3 = gender)
rename(df_2[3],gender)
df_2
#df_1_1[3] <- ifelse(min(df_1_1[3])==df_1_1[3],
#                      summary(df_1_1[3])[2],df_1_1[3])
#df_1_1[,2]
#df_1_1[2,2]
#for (idx in 1:length(df_1_1$eng)) {
#  ifelse(df_1_1$eng[idx]==min(df_1_1$eng),summary(df_1_1$eng)[2],df_1_1[idx])
#  }
# 1. 전체 평균이 가장 높은 사람은 누구이며 평균값은 얼마인가요? 연아 81.1
nrow(result)
result
result[1,length(result)]
result_mean <- c()
#for (idx in 1:nrow(result)){
#  result_mean <- c()
#    for (inx in 4:length(result)){
#  result_mean <-   mean(result[idx,inx])
#  }
#  result_mean1[idx] <- result_mean 
#}
#result_mean1
for (inx in 4:length(result)){
  result_mean[inx] <-   sum(result[1,inx])
}

result%>%group_by(name)%>% summarise(mean_result=(eng+kor+math)/3)%>% arrange(desc(mean_result))
# 2. 남자와 여자의 전체 평균은 각각 얼마인가요? 40.7 54.6
result %>% group_by(gender) %>% summarise(mean_result=(eng+kor+math)/3)
# 3. 수학성적이 전체 수학 성적 평균보다 높은 남성은 누구이며
#    수학성적은 얼마인가요?
c(result$name[result$math >=mean(result$math)] 
,result$math[result$math >=mean(result$math)] 
)
