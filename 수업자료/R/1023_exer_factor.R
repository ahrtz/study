var1 <- c("A","B","AB","O","A","O")
factor_var1 <- factor(var1)
factor_var1

nlevels(factor_var1)
levels(factor_var1)
is.factor(factor_var1)


var1 <- c("Male","Female","Male","Male","Female","Female","Female","Female")
factor_gender <- factor(var1,levels = c("Male",'Female'))
factor_gender
table(factor_gender)
plot(factor_gender)
example("factor")
var_scalar <- 100
var1 <- c("Male","Female","Male","Male","Female","Female","Female","Female")
var2 <- matrix(1:30,6,5)
var3 <- array(1:32,dim=c(2,4,2,2))

var_df <- data.frame(id=1:3,score = seq(30,50,10),name = c("고양이","냐옹이","야옹이"))

list_a <- list(var_scalar,var1,var2,var3,var_df)
list_a[2:3]

myList <- list(name=c("홍길동","김길동"),age=c(25,43),address = c("서울","부산")) 
myList[1]
myList$name
myList[['name']]
example("factor")
