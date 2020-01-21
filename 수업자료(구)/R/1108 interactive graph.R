# 회사에 있으면 모든 데이터는 데이터 베이스에 축적된다

# 데이터 베이스 access하기 
# mysql !!!!   <-  요기 중요 

###############

#EDA (Exploratory Data Analysis)
# => 탐색적 데이터 분석 

# 구글지도 서비스를 이용해 보자
# Google map platform 을 사용하기 위해서는 
# 특정 패키지가 있어야 한다 
# 이 패키지가 크랜에 등록이 안되어 있다. 
# github에 공유 되어 있다. 

# VCS(Version Control System)
# 공유 폴더의 덮어쓰기 문제를 해결하기 위해서 나온것이 VCS

# 초기에는 CVCS를 이용 (Centraliized version control system )
# 소스원본을 중앙서버가 1개 들고있고 나머지 사람이 복사본을 가져다가 작업
# 문제점 중앙서버가 죽어버리면 데이터가 유실된다

## 그래서 분산 서버 형식으로 바뀜 
# DVCS Distributed version control system
# 소스 원본으 여러군데에 보관하기 때문에 유실염려가 없다
# 가장 대표적인 것이 깃 
# git을 이용하면 공동처리가 쉬워진다. <-  이건 필수 

# Git repository (저장소)
# 이런 깃 저장소를 서비스해주는곳이 있다네 => Github

# 1. Github에 공유되어있는 ggmap패키지(구글맵)를 설치해야한다. 
# 주의: R 버전 특성을 탄다.
# package들은 dependency(의존성)에 신경 써야합니다. 특정버전에서만 돌아가는 패키지가 있슴니다
#3.5.1 버전에서만 돌아감 저 패키지 
# 현재 버전은 3.6.1 입니다 
# 그러므로 우리는 다운 그레이드를 해야합니다. 
# 3.5.1 깔고 스튜디오 재부팅하면 댐 

# 버전을 맞췃으니 필요한 패키지를 깃 허브에서 받자
# install.package 는 크랜에서 받는거다 그래서 못씀
# install_github() 쓰면 되는데 저 함수를 이용하기 위한 패키지를 설치해야한다.
install.packages("devtools")
library(devtools)
install_github("dkahle/ggmap")
library(ggmap)
# 여기 들어가서 https://cloud.google.com/maps-platform/terms 동의하고 키 생성하세요 
# 생성한 구글 API KEy
apikey = 
  "AIzaSyD_F7t0a0ncNi9ym9ATXzEnyQBP3SkiKQs"

# 구글 api 키를 이용해서 인증을 받는다
register_google(key=apikey)
gg_seoul <- get_googlemap("garakdong",maptype = "roadmap")
ggmap(gg_seoul)
library(dplyr)
library(ggplot2)
geo_code=geocode(enc2utf8("오금역")) # 인코딩하는 함수임 
geo_code 
# google map 을 그리려면 위도 경도가 숫자형태의 벡터로 되어있어야한다
geo_data <-  as.numeric(geo_code)
geo_data
ggmap(get_googlemap(geo_data,maptype = "roadmap"))
get_googlemap(center = geo_data,maptype = "roadmap",zoom = 18) %>% ggmap() + geom_point(data=geo_code,aes(x=lon,y=lat),size = 8 ,color = "red")
## 디플라이r 이랑 지지 플롯은 만든 사람이 같아서 뭐 되긴한다 
# 맵에서 두개 찍어서 연결하기
addr <- c("공덕역","역삼역")
gc <- geocode(enc2utf8(addr)) 

df <- data.frame(lon=gc$lon,lat=gc$lat)
df

cen <- c(mean(df$lon),mean(df$lat))
gg <- get_googlemap(center = cen,maptype = "roadmap",zoom=13,markers = df) %>% ggmap() + geom_line(data = df,color = "red")



# 지하철역 주변 아파트 정보: 서울열린 데이터 광장
# 아파트 실 거래 금액 데이터: 국토부 실거래가 공개시스템 

####################################################

# 패널데이터 실습 정형
# movielens 정형
# 로튼토마토 실습 (반정형) 
# 카카오 api 반정형
# 네이버 댓글크롤링 워드클라우드 비정형 

# interactive map <-  지금 지도 같은거 생각하면댐 
# 패키지를 설치해서 할 수 있다. 
install.packages("plotly")
library(plotly)



df <- as.data.frame(mpg)
head(df)
g <- ggplot(data = df,
       aes(x= displ,y= hwy)) + geom_point(size=3,color="blue")
ggplotly(g)

ggplotly(gg)
############################ 확대 , 값 확인 

### 시계열 그래프 
## 확대의 개념이 아니라 그 간격 내의 것을 자세하게 보여주어야 한다 
# dynamic 그래프 라는 것을 이용한다 

## 특정 구간에 대해서 자세한 사항을 보기 위해서는 
## 다른 패키지를 이용한다
install.packages("dygraphs")
library(dygraphs)
library(xts)

# 예제로 사용할 데이터 셋은 economics를 이용 
economics
# 시계열은 살짝 특이하게 데이터를 xts라는 형식으로 변환시켜줘야 한다 
# 시간에 따른 개인 저축률 변환 추이를 선 그래프로 그린다

save_rate <- xts(economics$psavert,
                 order.by=economics$date )
unemp_rate <- xts(economics$unemploy/1000,
                 order.by=economics$date )
head(save_rate)
dygraph(save_rate) %>% dyRangeSelector()

# 두 그래프 한번에 표현하기
a <- cbind(save_rate,unemp_rate)
a
dygraph(a) %>% dyRangeSelector()

#################


