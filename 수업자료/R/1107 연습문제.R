# 한국 복지 패널 데이터를 이용 

# 한국 보건 사회 연구원 ＝＞　2006년　부터　１０년간
#7000여　가구에　대한　경제활동，　생활　실태　복지욕구　등등

# 파일을 로컬하드로 카피 
# 제공된 데이터 파일은 spss파일임 Koweps_hpc10_2015_beta1
# 외부 패키지가 필요하다 

install.packages("foreign")
library(foreign)
# 필요한 패키지를 미리 로드
library(stringr)
library(dplyr)
library(ggplot2)
library(readxl)

# 사용할 raw data를 불러온다 
raw_data_file = "C:/R_EXER/data/Koweps_hpc10_2015_beta1.sav"
raw_welfare <- read.spss(file = raw_data_file,to.data.frame = T)
welfare <- raw_welfare
View(welfare)

#데이터 분석에 필요한 컬럼은 컬럼명을 변경해 줄것
welfare <- rename(welfare,gender = h10_g3,birth = h10_g4,marriage = h10_g10,
                  religion = h10_g11,code_job = h10_eco9,avg_inc = p1002_8aq1,
                  code_region = h10_reg7)
#####################################
#세팅 끝 
# 1. 성별에 따른 월급 차이 
table(welfare$gender) # 이상치 확인
# 1은 male로 변경 2는 female로 변경

welfare$gender <-  ifelse(welfare$gender == 1 ,"male","female")
class(welfare$avg_inc)
summary(welfare$avg_inc)
qplot(welfare$avg_inc) + xlim(0,1000) +geom_vline(xintercept = mean(welfare$avg_inc,na.rm = T)) ## 확인 용도

# 월급에 대한 이상치부터 처리 NA로 변환 
welfare$avg_inc <- ifelse(welfare$avg_inc == "0"|welfare$avg_inc == "9999",NA,welfare$avg_inc)
welfare$avg_inc <- ifelse(welfare$avg_inc %in% c(0,9999),NA,welfare$avg_inc)
table(is.na(welfare$avg_inc))
# 전처리 끝 
View(welfare)
gender_income <-welfare %>% filter(!is.na(avg_inc))%>% group_by(gender)%>% summarise(mean_income = mean(avg_inc))  # 정석
gender_income

welfare %>% group_by(gender)%>% summarise(income=mean(avg_inc,na.rm = T) )

welfare %>%  group_by(gender)%>% summarise(mean_income = mean(avg_inc,na.rm = T))
#그래프로 보여주기 캡션이랑 타이틀 행렬 이름 주는거 잘 보기 
ggplot(gender_income,aes(x=gender,y=mean_income))+geom_col(width = 0.3)+ labs(x="성별",y=" 평균월급",title = "성별에 따른 월급",subtitle = "설명설명명",caption = "example 1 Fig")
### 2. 나이와 월급의 관계 파악 
# 몇살때 월급을 가장 많이 받을가 ? 
#나이에 따른 월급을 선 그래프로 표시 
table(welfare$birth)


welfare$age <- 2016 - welfare$birth
#welfare <- welfare %>% mutate(age = 2015+1-birth) 이게 정석

##age_income <- welfare %>% filter(!is.na(avg_inc)) %>% group_by(age)%>% summarise(birth_income=mean(avg_inc)) 정석
age_income <- welfare %>% group_by(age) %>% summarise(birth_income=mean(avg_inc,na.rm = T))
head(arrange(age_income,desc(birth_income)))

ggplot(age_income,aes(x=age,y=birth_income))+geom_line()+labs(x="나이",y= "평균 월급", title = " 나이에 따른 월급 분포",caption = "example 2 Fig")

#max(age_income$birth_income,na.rm = T)
#View(age_income)
#ifelse(age_income$birth_income ==max(age_income$birth_income,na.rm = T),select(age_income$age))

#age_income$age[age_income$birth_income ==max(age_income$birth_income,na.rm = T)]
#age_income[52,]  
  
###### 3. 연령대에 따른 월급 차이 
## 30대 미만 : 초년생(young)
## 30~59 : 중년 (middle)
## 60~ : 장년 (old)
# 위의 범주로 연령대에 따른 월급차이 

welfare$older <- ifelse(welfare$age<30,"young",
                        ifelse(welfare$age<60,"middle","old"))
#welfare <- welfare %>% mutate(older = ifelse(welfare$age<30,"young",
#정석                                            ifelse(welfare$age<60,"middle","old")))
table(welfare$older)

group_income <- welfare %>% group_by(older) %>% summarise(mean_income = mean(avg_inc,na.rm = T))
#group_income <- welfare %>% filter(!is.na(avg_inc)) %>% group_by(older) %>% summarise()
group_income <- as.data.frame(group_income)
group_income
ggplot(group_income,aes(x=older,y=mean_income))+geom_col(width = 0.3)+ labs(x="연령별",y=" 평균월급",title = "연령대별 월급",caption = "example 3 Fig")
# ggplot은 막대그래프 그릴때 기본적으로 알파벳 오름차순으로 정렬한다 
# 막대그래프 크기순으로 정렬하려면? 
ggplot(group_income,aes(x=reorder(older,mean_income),y=mean_income))+geom_col(width = 0.3)+ labs(x="연령별",y=" 평균월급",title = "연령대별 월급",caption = "example 3 Fig")
#리오더 두번째 var로 설정 
## x축 순서를 내가 원하는 순서로 바꾸려면 어떻게 해야함?
ggplot(group_income,aes(x=reorder(older,mean_income),y=mean_income))+geom_col(width = 0.3)+ scale_x_discrete(limits=c("young","middle","old"))+labs(x="연령별",y=" 평균월급",title = "연령대별 월급",caption = "example 3 Fig")
########### 정확하게는 알파벳 순으로 레벨을 정하기 때문에 레벨을 바꿔주면 위 처럼 하지 않아도 x축을 변환할 수 있다. 
welfare$older <- factor(welfare$older,levels = c("young","middle","old"))
help("factor")
factor(welfare$older)
##################
##############   4.연령대 및 성별의 월급차이 

gender_age_income <- welfare %>% group_by(older,gender) %>% summarise(mean_income = mean(avg_inc,na.rm = T))
gender_age_income <- as.data.frame(gender_age_income)
gender_age_income

######## 그래프 2개 겹쳐 그리기 
ggplot(gender_age_income,aes(x=gender,y=mean_income,fill=older))+geom_col(width = 0.3)+ labs(x="연령별",y=" 평균월급",title = "연령대별 월급",caption = "example 4 Fig")
ggplot(gender_age_income,aes(x=older,y=mean_income,fill=gender))+geom_col(width = 0.3)+ labs(x="연령별",y=" 평균월급",title = "연령대별 월급",caption = "example 4 Fig")
######## 차트를 분리해서 표시해보기 geomcol 안에 포지션= 포지션 닷지 해줘야 댄다  
ggplot(gender_age_income,aes(x=older,y=mean_income,fill=gender))+geom_col(width = 0.3,position=position_dodge ())+ labs(x="연령별",y=" 평균월급",title = "연령대별 월급",caption = "example 4 Fig")
ggplot(gender_age_income,aes(x=gender,y=mean_income,fill=older))+geom_col(width = 0.3,position=position_dodge ())+ labs(x="연령별",y=" 평균월급",title = "연령대별 월급",caption = "example 4 Fig")


########################## 5 나이 및 성별에 따른 월급 차이 분석 
gender_age1_income <- welfare %>% group_by(age,gender)%>% summarise(mean_income = mean(avg_inc,na.rm = T))

ggplot(gender_age1_income,aes(x=age,y=mean_income,fill=gender,color=gender))+geom_line(position = position_dodge(width = 0.5))+labs(x="나이",y= "평균 월급", title = " 나이와 성별 따른 월급 분포",caption = "example 5 Fig")

################### 6. 직업별 월급의 차이를 분석해보자 
jobdf <- read_excel("C:/R_EXER/data/Koweps_Codebook.xlsx",sheet = 2)
jobdf <- as.data.frame(jobdf)
jobdf
exp <- left_join(welfare,jobdf)
help("left_join")
exp$job
jobinc <-
  exp %>% filter(!is.na(job))%>% group_by(job)%>% summarise(mean_income = mean(avg_inc,na.rm = T))
jobinc <- as.data.frame(jobinc)
head(jobinc %>% arrange(mean_income),1)
head(jobinc %>% arrange(desc(mean_income)),1)
jobinc
exp2 <- rbind(head(jobinc %>% arrange(mean_income),1),head(jobinc %>% arrange(desc(mean_income)),1))
exp2


ggplot(jobinc,aes(x=job,y=mean_income))+geom_col(width = 0.3,position=position_dodge ())+coord_flip()

###################### 7. 종교유무에 따른 이혼률

a <- table(welfare$marriage)
welfare$religion <- ifelse(welfare$religion == 1,"yes","no")

m_rate
# 이거 틀려welfare %>% group_by(religion) %>%   summarise(m_rate=marriage[4]/marriage[2])
table(welfare$marriage)
m_status <- welfare %>% group_by(religion,marriage) %>%summarise(numb=n())
m_status <- as.data.frame(m_status)

m_status

marriagenum <- m_status %>% group_by(religion)%>% filter(marriage %in% c(1,2,3,4)) 
#%>% sum(numb)
marriagenum

marriagenum1 <- marriagenum %>% group_by(religion) %>% summarise(sum = sum(numb))  
marriagenum1 <- as.data.frame(marriagenum1)
marriagenum1

divorce <- m_status%>% group_by(religion)%>% filter(marriage == 3) %>% summarise(sum = sum(numb))
divorce <- as.data.frame(divorce)
divorce

exp1 <- left_join(marriagenum1,divorce,c("religion"))

exp1 <- rename(exp1,marriage=sum.x,divorce = sum.y)
exp1$rate <- 100* exp1$divorce/exp1$marriage
exp1
divorce/marriagenum1

divorce1/marriagenum2
#%>% filter(marriage == 1|marriage == 4) %>% group_by(religion)
# 1234/3

################정답지 풀이

welfare <- welfare %>% mutate(group_marriage = ifelse(marriage %in% c(1,2,4),"marriage",ifelse(marriage==3,"divorce",NA))) 
table(welfare$group_marriage)

welfare%>%filter(!is.na(group_marriage)) %>% group_by(religion,group_marriage)%>% tally() %>% mutate(total_n= sum(n)) %>% mutate(pct = round(n/total_n*100,1))
