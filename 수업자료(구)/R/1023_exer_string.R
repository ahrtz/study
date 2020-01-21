install.packages("stringr")
library(stringr)

var1 <- "Honggd1234Honge9032YOU25최길동2009"
str_length(var1)

class(str_locate(var1,"1234")
str_count(var1,"e")
str_sub(var1,3,8)
str_to_lower(var1)
b=str_to_upper(var1)

str_replace(var1,"Hong","Kim")
str_replace_all(var1,"Hong","Kim")

var1 <- "Honggd1234,leess9032,YOU25,최길동2009"
str_split(var1,",")
b=str_c(var1[]," ")
b
var1
paste(var1,collapse = " ")

var1 <- "Honggd1234,leess9032,YOU25,최길뚧2009"
str_extract_all(var1,"[a-z]{2,}")
str_extract_all(var1,"[0-9]{2,3}")
str_extract_all(var1,"[A-Z]{2}")
str_extract_all(var1,"gg")
str_extract_all(var1,"[^가-힣]")
a=str_extract_all(var1,"[^가-힣]")

paste(a[[1]],collapse = "")
str(a)
cbind(a)

help("paste")
myID <- "801112-1357862"

str_extract_all(myID,"[0-9]{6}-[1234]{1}[0-9]{6}")

myWord <- scan(what = character())
myWord

var1 <- data.frame()
df <- edit(var1)
df
edit(df)
