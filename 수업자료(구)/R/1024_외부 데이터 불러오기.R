getwd
getwd()
setwd("C:/R_EXER/data")

student_midterm <- read.table(file = "student_midterm.txt",sep = ",",fileEncoding = "UTF-8",header = T)

student_midterm <- read.table(file.choose(),sep = ",",fileEncoding = "UTF-8")
student_midterm


write.table(data_ex,file ="C:/users/student/documents/R/data_ex.txt" )

df = read.csv(file="student_midterm.csv",fileEncoding = "UTF-8")
help("read.csv")
df
install.packages("xlsx")
library(xlsx)

Sys.setenv(JAVA_HOME="C:\\Program Files\\Java\\jre1.8.0_231")
student_midterm <- read.xlsx(file.choose(),sheetIndex = 1,encoding = "UTF-8")
student_midterm
class(summary(student_midterm))

cat("처리된 결과는 :","\n","\n",summary(student_midterm),file="c:/users/student/documents/R/report.txt",append = T)

write.table(summary(student_midterm),file = "c:/users/student/documents/R/report.txt", append = T,row.names = F,quote=F)

capture.output(summary(student_midterm),file = "c:/users/student/documents/R/report.txt", append = T)

library(stringr)
df <- data.frame(x=c(1:5),y=seq(1,10,2),z=c("a","b","c","d","e"), stringsAsFactors=F)
df
write.xlsx(df,file ="c:/users/student/documents/R/report.xlsx" )
