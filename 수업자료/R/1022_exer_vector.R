var1 = c(1,4,57,8)
var1
mode(var1)
str(var1)
var2 = c(4,3,TRUE)
var3 = c(var1,var2)
var3
a = [1:10]
var4 <- 1:10
var4
var5 <- 10:1
var5
var6 <- 3.4:10
var6
a=rep(1:3,times=5)
a
a=rep(1:3, each=5)
a
length(a)
length(var3)
var1= seq(1,100,length =3)
var1
var1[length(var1)]
var1[c(1,5)]
var1[-c(1:3)]
names(var1)
names(var1) <- c("등수","나이","총인원","상금")
var1["나이"]
var3 + var6
var3 %% var6
var3*2
var1+var2
var2+var1
a <- 1:3
b <- 6:10
a+b
var2 <- 1:3
var1 <- 1L:3L
var1 == var2
identical(var1,var2)
var3 <- c(1,3,3,2)
identical(var1,var3)
setequal(var1,var3)
c <- vector(mode <- "character",20)
c
