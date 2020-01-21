ID <- c("1","2","3","4","5")
MID_EXAM <- c(10,25,100,75,30)
CLASS <-c("1반","2반","3반","1반","2반")
example_test <- data.frame(ID,MID_EXAM,CLASS)
example_test
install.packages("readxl")
library(readxl)
DATA <- data.frame(ID,CLASS)
View(DATA)
excel_data_ex <-  ("C:/Users/student/Documents/R/data_ex.xls")

var1 <- c(1,2,3)
var2 <- seq(1:3)
identical(var1,var2)
data_ex <-  data.frame(ID,CLASS)
write.csv(data_ex,"C:/users/student/documents/R/data_ex.csv")

write.table(data_ex,file ="C:/users/student/documents/R/data_ex.txt" )
exdata1 <- read_excel("C:/users/student/documents/R/source/Sample1.xlsx")
exdata1
View(exdata1)
str(exdata1)
ls(exdata1)
install.packages("dplyr")
library(dplyr)
exdata1 <- rename(exdata1,Y17_AMT = AMT17,Y16_AMT = AMT16)

exdata1$AMT <- exdata1$Y17_AMT+exdata1$Y16_AMT
exdata1$CNT <- exdata1$Y17_CNT+exdata1$Y16_CNT
View(exdata1)
exdata1$AVG_AMT <- exdata1$AMT/exdata1$CNT
exdata1$AGE50_YN <- ifelse(exdata1$AGE>=50,"Y","N")
exdata1$AGECLSS <- ifelse(exdata1$AGE>=50,"A1,50++",
                          ifelse(exdata1$AGE>=40,"40-49",
                                 ifelse(exdata1$AGE>=30,"30-39",ifelse(exdata1$AGE>=20,"20-29","-20"))))
View(exdata1)
exdata1 %>% filter(AREA == '서울',Y17_CNT>=10)
exdata1 %>% select(ID,AREA,Y17_AMT)
exdata1 %>% arrange(desc(AGE))
exdata1 %>% arrange(AGE,desc(Y17_AMT))
exdata1 %>% summarise(sum=sum(Y17_AMT))                    
sum <- exdata1 %>% group_by(AREA) %>% summarise(area_sum=sum(Y17_AMT))                    
sum
