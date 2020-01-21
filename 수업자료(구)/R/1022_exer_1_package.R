install.packages("ggplot2")
library(ggplot2)
require(ggplot2)
############# 예시 #############
v1 = c("a","b","c","d","b","a")
qplot(v1)
remove.packages("ggplot2")

.libPaths()

help("qplot")
args(qplot)
example(qplot)

getwd()
