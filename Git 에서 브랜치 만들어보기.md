# Git 에서 브랜치 만들어보기

> 독립적인 개발환경을 제공하여 동시에 다양한 작업을 진행 할 수 있도록 만들어준다.
>
> 일반적으로 브랜치의 이름은 해당 작업을 나타낸다. 

## 0. 브랜치 만들기

```bash
$git branch testbranch  # 브랜치 생성하기

$git branch   # 브랜치 목록 확인
* master
  testbranch

```

## 1. 브랜치 이동하기

```bash
$git checkout testbranch   # 이동하기 
Switched to branch 'testbranch'

$ git checkout master
Switched to branch 'master'


```

## 2 . 이제 독립적인 환경이 되어서 작업하면 된다.

## 3. 작업을 완료한 후

* 마스터로 돌아와서 가지고 오고 싶다. 
* 이때 입력하는 명령어

```bash
$git merge testbranch  # 마스터 브랜치로 테스트 브랜치에 있는 것들 가져오기
```

* 다쓴 브랜치 삭제하기

```bash
$git branch -d {브랜치 이름}

$git branch -b {브랜치 이름}
```







