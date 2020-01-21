options(digits = 7) # digits 5가 기본값
sprintf("%.7f",100/3) # 결과값 형식 설정 가능 결과값을 문자로 출력함 주의 

#데이터 타입의 종류
# 1.numeric 2.character 3.logical 4.complex
mode(a)
# 단축키 ctrl + 1 : 스크립트창 이동
#        ctrl + 2 : 콘솔창 이동
#        alt  + - : <- 
#        ctrl + L : 콘솔창 clear
# 데이터 타입의 우선순위 
  # character > complex > numeric > logical
# 데이터 타입 변경하기 
# as 계열 함수 이용하기 
# as.numeric(a) 0 은 False 0 이외의 숫자는 TRUE
a= matrix(c(1:12),3,4)
a[2:3,1:2]
a <-  list(3,c(2,3,4),2)
a
b <- data.frame(a)
