### 데이터 정제 
## 오류가 있는데이터를 없애서 내가 분석할수 있는 데이터로 만드는 작업 
## 우리가 얻는 raw data 는 항상 오류를 포함하고 있다. 
## 분석하기 전에 오류를 수정해 주어야 한다 
## 1. NA 결측치 처리
# 결측치는 누락된 값을 지칭 비어있는 값을 지칭 결측치가 있으면 함수적용이 잘못될수 있다. 
# 분석자체가 잘 못 될 수 있다. 

# 결측치를 찾아야한다. 
# is.na 함수 
# 간단하게 결측치가 있는 데이터셋 하나 만들자

df <- data.frame(id=c(1,2,NA,5,7,4,3,NA),score=c(10,20,90,NA,63,NA,85,NA))

df
is.na(df)
sum(is.na(df)) ## na 확인 법 
table(is.na(df$id)) ## 테이블은 개수 세는 함수 
## 결측치를 제거하려 한다 
# => 데이터 프레임이기 때문에 결측치를 가지고 있는 행을 삭제 
df
df %>% filter(id != "NA" , score!= "NA" )
na.omit(df) ## 아예 해당 행을 삭제하는 함수도 있습니다. 그러나 이건 아주 위험할수 있습니다. 전체적인 표본값이 적어질수도 있고 결측치를 제외한 나머지 값은 문제가 되는것이 아니기 때문이야 
avg <- mean(df$score,na.rm = T)  # NA가 들어있는 값의 연산결과는 NA이기 때문에 이렇게 계산  

# 결측치가 포함된 행을 삭제하기에는 부담이 있다. 
## score안에 있는 결측치 값을 다른 값으로 대치해서 평균을 구해보자 
## NA를 제외한 평균을 구해서 그값으로 NA를 대체

df$score[is.na(df$score)] <- avg
mean(df$score)
df$score
df$score[4] 

# 결측치 (NA)

# 이상치 존재할수 없는값이 포함된 경우
# 극단치 정상치에서 너무 벗어난 값이 들어온 경우 (정상적인 범위 설정은 어떻게 하지?)

df <- data.frame(id=c(1,2,NA,5,7,4,3,NA),score=c(10,20,90,NA,63,NA,85,NA),gender = c("M","F","M","F","M","F","M","^^"),stringsAsFactors = F) # factor 처리 가 된다 기본적으로 gender 처럼 한글자 잇는건 ? 일단 무언가는 저게 됨 

# 일반적으로 이상치가 존재하면 결측치로 바꿔준다.
df$gender <- ifelse(df$gender %in% c("M","F"),df$gender,"NA") ## in 연산자 (값이 저거 뒤에 나오는거 안에 있으면) 
df$gender <- ifelse(df$gender =="M"|df$gender=="F",df$gender,"NA")
df$gender

### 극단치 : 이상치중에 값이 극단적으로 크거나 작은값을 의미; 기준을 정해야한다 
# 기준을 정해야 한다 => 보통 기준이 있음 
# 극단치를 분류하기준 IQR을 이용한다 
#interquantile range ;4 분위부터 알아보도록 하자 

# 극단치를 알아보기 위한 sample 작성
data = c(2,3,4,5,6,7,8,9,10,11,12,13,22)
quantile(data)
summary(data)
IQR(data)*1.5
# IQR은 데이터 중간 위쪽의 미드포인트 - 데이터 중간 아래쪽의 미드포인트를 뺀다

lower_ <- c(2,3,4,5,6,7,8)
upper_ <- c(8,9,10,11,12,13,22)

iqr_val <- median(upper_) - median(lower_)
# 극단치를 결정하는 기준값 : IQR * 1.5 
deter_val <- iqr_val*1.5
deter_val

# 1사분위값-기준값,3사분위값 +기준값 을 넘어가면 극단치로 생각하고 제거 
# 계산을 통해 극단치를 판단하는 방법 

# 그래프를 이용하면 극단치를 눈으로 확인
boxplot(data)
boxplot(data)$stats

