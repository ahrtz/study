var1 <- 100
var2 <- 20
  if(var1>var2) { 
    cat("참")} else { cat("구라")    
}
  

ifelse(var1>var2,cat("참\n"),cat("구라\n"))


  for (var1 in seq(1:5)) { print(var1)}
  

idx <- 1 
Ssum <- 0
while (idx < 10) {  Ssum <- Ssum + idx ; idx <- idx+1}
Ssum
idx
mod3=0
idx =1 
while( idx <100) { 
  ifelse(idx %% 3 == 0 ,print(idx),mod3=mod3+1)
  idx <- idx+1
}

for (var1 in 1:100) { 
  if(var1 %% 3 == 0)
  print(var1)
}
a=0
for (var2 in 1:100) {
  
  a = a+1
  print(a)
}
if (condition) {
  
}
#소수 만들기
a=0
3/2
a <- seq(1,100,1)

for (var1 in 1:100){
  a=0
  for (var2 in 1:var1) {
    
     if (var1%%var2 == 0){ 
       
       a = a+1
     }
    
  }
  if (a==2) {
    print(var1)
    
  } 
}
    
  

