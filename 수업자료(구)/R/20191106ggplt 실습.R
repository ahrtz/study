## 데이터 시각화 
## ggplot 
## 형태소 시각화 

## R 그래프
## 숫자나 문자로 표현하는 것보다는 그림으로 표현하면 더 쉽게 파악할 수있다 

#ggplot 2 dplyr reshape2
# 해들리 위컴이 만듬

# 산점도 scatter - 변수간의 관계를 파악
# 막대그래프 - 집단간의 비교를 할대 
# 선그래프 - 시계열 데이터를 표현 
# 박스 그래프 -데이터의 분포를 파악

# ggplot2 는 3단계로 그래프를 그린다

# 1단계 축을 정한다 <-  배경을 설정
# 2단계 그래프를 추가한다 
# 3단계 축 범위 배경설정 
library(ggplot2)
library(dplyr)
mpg

df <- as.data.frame(mpg)
# 1. 배경 설정 
# data 설정 : 그래프를 그리는데 필요한 데이터 
# aes(x= , y= ) : 축을 설정한다
# #############################################산점도
ggplot(data = df,aes(x=displ,y=hwy )) ## 이건 축만 설정
ggplot(data = df,aes(x=displ,y=hwy )) + geom_point()# 얘가 산점도 그리는 함수 
ggplot(data = df,aes(x=displ,y=hwy )) + geom_point(size=3,color = "red")  + xlim(3,5)+ylim(20,30) # x축 y 축 

plot.new()        ## 그래프 초기화 
###################################################막대그래프 그리기 
################### 막대그래프를 그리기 위해 데이터를 준비해야 한다 
result <- df %>% group_by(drv) %>% summarise(avg_hwy = mean(hwy))
result    
result <-  as.data.frame(result)   

ggplot(data=result,aes(x= drv, y= avg_hwy))+ geom_col(width=0.1)# 컬럼 두께를 width로 조절 가능

# 막대그래프에 대해서 순서를 다시 잡아줄 경우  
ggplot(data=result,aes(x= reorder(drv,avg_hwy), y= avg_hwy))+ geom_col(width=0.1)
# 기본은 오름차순 
ggplot(data=result,aes(x= reorder(drv,-avg_hwy), y= avg_hwy))+ geom_col(width=0.1)
# 이러면 내림차순

################################################################ 빈도 막대 그래프 
# 사용하는 함수는 geom_bar()
# raw data frame 을 직접 이용해서 처리 
ggplot(data=df,aes(x= drv))+ geom_bar()  # bar 는 빈도를 구할때 쓰는 막대그래푸

# 빈도 막대 그래프 구할대 사용하는 함수와 사용방법 

# 재밋는 그래프
ggplot(data=df,aes(x= drv))+ geom_bar(aes(fill=factor(manufacturer)))
## 빈도그래프를 factor 별로 채워서 이쁘게이쁘게 그리낟.

######################################################### 히스토그램 
ggplot(data=df,aes(x= hwy))+ geom_histogram()
  
################################################### 선그래프 (시계열 데이터)
# 일반적으로 환율 쥬식 경제동향
#시간에 대한 데이터가 필요

#economics 데이터 이용
economics
tail(economics)
help("economics")# date 의 데이터 타입을 보자 
ggplot(economics,aes(x=date, y=unemploy))+ geom_line()+geom_abline()
# line은 꺽은선 그래프 abline 추세선 
ggplot(economics,aes(x=date, y=unemploy))+ geom_point(color="red")
########################################
# 정리 산점도 (변수간의 관계 , 데이터 경향)
# 선 그래프 (시계열 데이터 표현)
# 박스 그래프 (데이터의 분포)
ggplot(data=df,aes(x= drv,y= hwy))+ geom_boxplot()
######################

# 4가지의 그래프를 그릴수 있다 
# 여기에 추가적인 객체를 포함시켜서 
# 그래프를 좀더 이해하기 쉬운 형태로 만들어보자 
head(economics)
# 날짜별 개인 저축률에 대한 선 그래프를 그려보자 # abline 으로 기울기와 절편을 줌으로써 일반적인 직선을 그릴수 있다. 
ggplot(economics,aes(x=date ,y= psavert))+ geom_line() + geom_abline(intercept = 12.11,slope = -0.000352) 
# 수평선 라인 그리기
ggplot(economics,aes(x=date ,y= psavert))+ geom_line() +  geom_abline(intercept = mean(economics$psavert),slope = 0) 
ggplot(economics,aes(x=date ,y= psavert))+ geom_line() +  geom_hline(yintercept = mean(economics$psavert)) 
## geom hline 도 잇고 그냥 line 도 있고 h= horeizontal line 
## 수직선 그리기 가장 개인 저축률이 낮은 날짜에 다가 
# 우선 날짜 뽑고
tmp <-  economics %>% filter(psavert == min(psavert)) %>% select(date)
tmp <- as.data.frame(tmp)
tmp <- tmp$date
ggplot(economics,aes(x=date ,y= psavert))+ geom_line() +  geom_vline(xintercept = tmp) 
# 만약 날짜를 직접 받으려면 ?
ggplot(economics,aes(x=date ,y= psavert))+ geom_line() +  geom_vline(xintercept = as.Date("2005-05-01"))


# + stat_smooth()   추세선 그리기 


########################## 그래프 안에서 txt 를 표현하려면??  
###########제목넣기이이
ggplot(economics,aes(x=date,y=psavert))+ geom_point()+ xlim(as.Date("1990-1-1"),as.Date('1992-12-1'))+ ylim(7,10)+geom_text(aes(label=psavert,vjust = -0.5,hjust=-0.3))

####################################
# 만약 그래프에서 특정영역을 하이라이팅 하려면??  annotate <- 덧씌운다는 거임 alpha는 투명도
ggplot(economics,aes(x=date,y=psavert))+ geom_point()+annotate("rect", xmin = as.Date("1991-1-1"),xmax = as.Date("2005-1-1"),ymin = 4,ymax = 10,alpha=0.6,fill="red") + 
  annotate("segment",
           x= as.Date("1985-1-1"),xend = as.Date("1995-1-1"),y= 7.5,yend = 8.5,arrow=arrow(),color="blue")+ annotate("text",x= as.Date("1985-1-1"),y=15,label="뭐 임마")+
  labs(x="가로축",y="세로축",title="제목목")+ theme_linedraw()


## 추가적인 기느은 여기까지

