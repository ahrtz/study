No <-  c(1,2,3,4)
Name <- c("김","이","박","최")
age <- c(13,68,52,14)

data1 <- data.frame(Num=No,F_Name=Name,age)
data1

data1[3,2]

Mat1 <- matrix(1:12,4,3,T)

df_mat <- data.frame(Mat1)
df_mat
data.frame(Mat1,row.names = c("1번","2번","3번","4번"))
str(data1)
str(Mat1)
str(df_mat)

summary(data1)

Mat1
df_mat
apply(X=df_mat,2,sum)

df1 <- data.frame(x=c(1:5),y=seq(2,10,2),z=c("a","b","c","d","e"),stringsAsFactors = F)
df1[1]
df2 <- df1[-3]
str(df1)
df2
apply(X=df2,2,FUN=sum)
apply(X=df1[,c(1:2)],MARGIN = 2,FUN=sum)
apply(X=df1[-3],2,FUN=sum)

df1
subset(df1,x>3 | y>4)

a <- c(4,6,5,7,10,9,4);a

#벡터의 연산 
x1 <- c(3,5,6,8)
x2 <- c(3,3,4)
x1+x2
x1[1]
x1[-4]+x2
length(x2)
x1[1:length(x2)]+x2
x1[1:length(x2)]
#데이터 프레임 만들기
Age <- c(22,25,18,20)
Name <- c("James","Mathew","Olivia","Stella")
Gender <- c("M","M",'F','F')
data1 <- data.frame(Age,Name,Gender)
data1
data1[1:2,]
subset(data1,Gender =="M"&Age>23)
!T
c=c(1,4,9,16,25)*c(F,F,T,T,T)
c
c[c(F,F,T,T,T)]
x <- c(2,4,6,8)
y <- c(T,T,F,T)
sum(x[y])

# 제공된 vector에서 NA가 몇개가 있는지 ?

var1 <- c(34,55,89,45,NA,22,12,NA,99,NA,100)
sum(is.na(var1))
mean(!is.na(var1)*var1)
b=!is.na(var1)
mean(var1*b)
c <- var1[b]
mean(c)

x1 <- c(1,2,3)
x2 <- c(4,5,6)
rbind(x1,x2)
cbind(x1,x2)
df1

