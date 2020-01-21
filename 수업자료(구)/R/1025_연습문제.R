## 10-25 연습문제

# 입력으로 최대 100자의 문자열을 이용
#  입력으로 사용된 문자열에서 숫자만을 추출해서 출력하세요 
library(stringr)
#예> HI458756FADFCXEWFGACdfdsc8965132486fdsa8v6x8
# 이렇게 추출한 문자열에서 개수가 가장 많은 숫자를 찾아서 숫자와 출현빈도를 출력
# 만약 출현 빈도가 같은 숫자가 여러개인 경우 
#그 중 가장 작은 숫자와 출현 빈도를 출력하세요  

##myWord <- scan(what = character())
library(stringr)

var1 <- "H0I45558756FADFCXEWFGACdfdsc86965132486fdsa8v6x8"
ans1 <-  str_replace_all(var1,"[A-z]","")
ans1
var2 <- c()
i=1
for (i in 1:str_length(ans1)) { 
  var2 <-   append(var2,substr(ans1,i,i),after = i)  
};
var2
fac <- as.factor(var2)
fac
d <- summary(fac)
d

##ifelse(length(d[t])>=2, d[t][1],d[t])


t <- d == max(d)
t
if (length(d[t])>=2) {
  e <- d[t]
  e[1]
} else {d[t]} 

