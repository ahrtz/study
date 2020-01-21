install.packages("devtools")

library(devtools)
install_github("pbiecek/PISA2012lite")
library(PISA2012lite)
help("PISA2012lite")
View(student2012)
df <- student2012
인도네시아 페루 브라질 터키 멕시코
싱가폴  ireland 캐나다 홍콩 재팬
library(dplyr)
ST28Q01
a <- df %>% group_by(CNT) %>% count(ST28Q01)
View(a)
