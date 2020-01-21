mul <- function(x) {x <- x^2;return(x)}

mul(3)
var1 <- c(1:10)
mul(var1)

mySum <- function(x){a=0
for (t in x) {
  a = a+t
}
return(a)
}
mySum(var1)

var1 = c(2,3,5,6,7,10) 
var2 = var1^2
sum(var2)
#데이터 추출
#5 이상인 것만 빼낼때
var3 = c(var1>5)   # mask 라고 이야기함 
var1[var3]
length(var1)
install.packages("UsingR")
library(UsingR)
# 데이터를 불러들일때 data함수 이용 1부터 2003 까지 의 숫자중 소수만 가지고있는 데이터
data("primes")
length(primes)
mean(primes)
head(primes) #데이터를 앞 뒤에서 6개 찍어준다
tail(primes)
#1부터 200 까지의 숫자중 prime number 의 개수는?
sum(primes<=200) #1안
var4 <- primes<201 # 2안
length(primes[var4])
#500 이상 1000이하의 소수로 구성된 벡터 만들기
var5 <-  500<=primes & primes <=1000  
var6 <- primes[var5]
var6

#다음과 같은 형태의 데이터를 이용하여 아래의 문제를 풀어보세요
x <- matrix(c(1:12),4,3)
t(x)
x %*% t(x)
