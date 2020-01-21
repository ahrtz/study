## 20191104  3주차 데이터 조작 제이터 정리 시각화에 대한 내용 시작
## mpg data set을 이용해서 데이터 조작 정제에 대한 내용을 학습해보자 

## 특정 패키지에 데이터 셋이 존재 
## 

mpg
datast <- as.data.frame(mpg)
str(datast)
class(datast)
##tbl_df() 데이터 프레임을 테이블 형식으로 만들어주는것  프린팅을 이쁘게 할 목적 

ls(datast)
help(mpg)
head(datast)
tail(datast)
head(datast,80) # 갯수지정가능
View(datast)
dim(datast) ## 행과 열의 갯수를 한번에 뽑아내는 함수 
length(datast) ## 컬럼의 갯수를 구한다// 매트릭스의 렝스는 원소의 갯수 
str(datast)
a <- c()
datast$audi <-ifelse(datast$manufacturer == "audi","Y","N") ## 제조사가 아우디면 Y 인 열 추가 
summary(datast) # 기본적인 통계 데이터 추출 
rev(datast)   # 벡터에 대해 데이터를 역순으로 변화하는 기능
###################
## 데이터 조작 
datast %>% filter(datast$cty>=19)
## dplyr 데이터 프레임을 조작할때ㅑ 가장 많이 사용되는 패키지 
## 속도에 강점이 있다 C++로 구현되어있음 
## chaining 이 가능하다 %>% 

df <- tbl_df(datast) ## 테이블 데이터 프레임으로 변환
df <- as.data.frame(datast)
df
str(df)
##2. rename() column 의 이름을 변경할수 잇디.
## raw data를 이용할 경우 컬럼 명이 없을때 
## 컬럼명을 새로 명시해서 사용해야 한다
## 컬럼명에 대소문자가 있을때 모두 대문자 혹은 소문자로 바꾸면 편하다
## 모든 컬럼명을 소문자로 혹은 대문자로 바꿔보자
df <- rename(df,MODEL = model) # 한개 바꾸기
names(df)=toupper(names(df)) # 전부 바꾸기
head(df)
df

### 3. 조건을 만족하는 행을 추출하는 함수 
## filter 함수 filter(dataframe,조건1,조건2,조건3)
## 2000년도에 생산된 차량이 몇개 있는지 추출
ex1 <- filter(df,df$year == 2008)
ex1
nrow(ex1)
## 모든 차량에 대해 평균 도시 연비보다 도시연비가 높은 차량의 모델명을 출력하세요 
ex1 <- filter(df,cty>=mean(cty,na.rm = T))  ## NA 값이 있으면 지우고 평균내라는 코드 
filter(df,cty>mean(cty))$model    # <- 이거 자체가 데이터프레임이기 때문에 달러 표시로 빼기 가능 
unique(filter(df,cty>mean(cty))$model) ## 제목 겹치는거 빼기 

b <- ex1$model
factor(b) ## 단순하게 팩터로 받아오기 

df %>% filter(cty>=mean(cty))

######## 고속도로 연비가 상위 75%인 차량을 제조하는 제조사는 몇개인지 추출
ex1 <- filter(df,hwy>=quantile(df$hwy)[4])$manufacturer
unique(ex1)
quantile(df$hwy,c(0.1,0.3,0.5,0.7,0.9,1)) # 분위수 연습해보기 
summary(df$hwy) # 이걸로도 분위수 가능

################### 오토 차량중 배기량이 2500 이상인 차량수는? 
library(stringr)

select(df$trans,starts_with("auto"))
ex1 <- filter(df,displ>=2.5 ,str_detect(trans,"auto")) ## str_detect로 찾기 

nrow(ex1)

## arrange 함수 <-  정렬하는거 
## arrange (dataframe,column,desc(컬럼명)) column으로 오름차순 컬럼명으로 내림차순 정리 
## 모델명을 오름차순으로 정리 같은 모델에 대해서는 생산연도가 빠른순으로 정리
ex1 <- filter(df,cty>=mean(cty,na.rm = T))
ex1$model
unique(arrange(ex1,model,year)$model)

df %>% filter(cty >= mean(cty)) %>% select(model) %>% unique() %>% arrange(model)
#########5. select 데이터 프레임에서 원하는 column만 추출하는 함수 
## select(data frame , column1, column2,....)

## 6. 새로운 컬럼을 생성하려면 어케 하니 
## 도시 연비와 고속도로 연비를 하벼서 평균 연비를 만들어보세요
df
df$avg <- (df$cty+df$hwy)/2
df$avg
df
## 기본 R 의 기능을 이용해서 column을 만들수 있다. 
new_df <- df %>% mutate(mean_rate = (cty+hwy)/2)
new_df
## 통계량을 구해서 새로운 컬럼으로 생성하는 함수 summarise
#model 명이 a4이고 배기량이 2000 이상인 차들에 대해 평균 연비

a <- df %>% filter(model == "a4",displ >=2.0) 
a
mean(c(a$cty,a$hwy))

a <- df %>% filter(model == "a4",displ >=2.0) %>% mutate(avg_rate = (cty+hwy)/2) %>% select(avg_rate)
a
mean(a$avg_rate)
## summarise 쓰기
c <- df %>% filter(model =="a4",displ >=2.0) %>% summarise(avg_rate = mean(c(cty,hwy)),hahaha = max(cty))
## 함수를 연산한 값이 avg rate 에 들어가는거다 
c

### group by 범주형 변수에 대한 그룹핑 
df%>% filter(displ >=2.0) %>% group_by(manufacturer)%>% summarise(avg_rate = mean(c(cty,hwy)))

## left_join right_join inner조인 아우터 조인등등 데이터 프레임을 결함 시키는것 
## 앞의 것은 기준을 나타냄 열단위 결함 
df <- as.data.frame(mpg)
df

