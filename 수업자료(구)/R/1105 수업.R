## reshape2 package 
# 데이터의 형태를 바꿀 수 있다.
# 가로로 되어 있는 데이터를 세로로 바꿀 수 있다.
# 컬럼으로 저장되어 있는 데이터를 row 형태로 
# row 형태의 데이터를 column 형태로 전환 
library(ggplot2)
library(stringr)
# melt_mpg.csv
# sample_mpg.csv
sample_mpg <- read.csv(file = "C:/Users/student/Documents/R/sample_mpg.csv",sep = ",",header = T,fileEncoding = "UTF-8")

melt_mpg <- read.csv(file = "C:/Users/student/Documents/R/melt_mpg.csv",sep = ",",header = T,fileEncoding = "UTF-8")
sample_mpg
melt_mpg 
## 두개의 데이터 프레임에 대해서 평균 도시 연비 
sample_mpg %>% summarise(mean_cty = mean(cty))
melt_mpg %>% filter(variable == "cty") %>% summarise(mean_cty = mean(value))
 
# 두개의 데이터 프레임에 대해서 평균연비를 구해서 표시 # 두번째의 경우는 너무 힘들다
reshape(melt_mpg,idvar="trans", direction = "wide")
sample_mpg %>% mutate(avg_rate = (cty+hwy)/2)
## reshape2 package 는 수집한 데이터를 분석하기 편한 형태로 가공할때 사용하는 대표적인 패키지 
# 두개의 대표적인 함수 1. melt -> column 을 row 형태로 바꾸어서 가로로 긴 데이터를 세로로 길게 전환하는 함수
# melt 의 기본돈작은 numeric을 포함하고 있는 모든 column 을 row 로 변환한다 
a <- melt(melt_mpg)
df <- airquality
reshape(a,direction = "wide",timevar ="value",idvar = c("model","manufacturer","trans" ))
a
help("melt")
df
melt_df <- melt(df,id.vars = c("Month","Day"),measure.vars = "Ozone",variable.name = "item",value.name = "num") ## 먼스와 데이를 기준으로 녹이세요 , 그 이후 오존이 들어간 컬럼만 녹이세요 
View(df)

## cast 는 melt 의 반대 
# dcast 데이터프레임이래 data 프레임에 대한 캐스트 작업 row로 되어있는 데이터를 column형태로 변환
# acast는 벡터나 매트릭스 등등
## 겹치는 값이 없을때 캐스트 작업이 가능 
dcast(melt_df,
      formula = Month + Day ~ ... ,fun=mean, na.rm=T)#formula 에는 기준이 되는 컬럼을 명시 ~ 은 원상복귀 시키라는것 ...은 나머지전부다를 의미함
dcast(melt_df,
      formula = Month  ~ item ,fun=mean, na.rm=T)
## 처음에 받은 csv파일의 내용을 원상 복구 시켜보자
melt_mpg
dcast(melt_mpg,formula = manufacturer + model + class + trans + year ~ variable,value.var = "value") ## 이거 대로 하면 오류가 남 왜? 뒤에는 멜트된 부분이고 앞부분은 같은 것들이 잇다 1,3번 2,4번
#mpg 멜트 시켜서 새로 만들어보자
df <- as.data.frame(mpg)
audi_df <-  df %>% filter(manufacturer == "audi",model == "a4")  
audi_df
melt_audi_df <- melt(audi_df,
                     id.vars = c("manufacturer","model", "year","cyl","trans"),
                     measure.vars = c("displ","cty","hwy"))
melt_audi_df
dcast(melt_audi_df,formula = manufacturer + model + year + cyl + trans ~ ...)
dcast(melt_audi_df,formula = manufacturer + model + year + cyl + trans ~ variable,value.var = "value") # 두개가 같다
