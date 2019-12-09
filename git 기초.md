# git 기초

> git은 분산형 버전관리시스템(DVCS)이다.
>
> 소스코드의 이력을 확인하고, 협업 단계에서 활용 가능하다

## 0. 기본설정

윈도우에서 git을 활용하기 위해서는 `git bash`가 필요하다

[설치링크](https://gitforwindows.org/)

맥에서는 깃이 기본적으로 설치되어 있기 때문에 바로 활용 할 수 있다.

설치 이후에 `commit`을 작성하는 `author`설정이 필요하다 

```bash
$ git config --global user.name{github username}
$ git config --global user.email{github email}

```

설정 내용을 확인하기 위해서는 아래의 명령어를 입력한다. 

```bash
$git config --global -l
user.name=ahrtz
user.email=ahrtzzinn@gmail.com

```

## 로컬저장소에서 활용하기

### 1. git 저장소 설정

특정 프로젝트 폴더에서 `git`을 활용하기위해서는 아래의 명령어를 입력한다

```bash
$git init
Initialized empty Git repository in C:/Users/student/Desktop/git_exer/.git/

```

* 해당디렉토리내에 `.git`라는 숨김폴더가 생성되며 모든 `git`과 관련된 동작은 해당폴더에 기록된다.
* git bash 에서 `(master)`라는 브랜치 정보가 표기된다.

### 2. add

`git`에서 커밋할 대상 파일을 `staging area`로 이동시키는 명령어 이다. 

```bash
$git add a.txt # 특정파일을 stage
$git add images/ # 특정 폴더를 stage
$git add . # 모든 디렉토리 파일 혹은 폴더를 stage
```

* `add` 전 상태

```bash
On branch master

No commits yet

Untracked files:## git 이력에 담기지 않은 파일
  (use "git add <file>..." to include in what will be committed) 
  ## add를 사용해서 커밋될 곳에 추가해라 
        a,txt
        b.txt

nothing added to commit but untracked files present (use "git add" to track)

```



* `add` 후 상태 

```bash
# a,txt만 애드 했을때
Changes to be committed:  ## 커밋될 변경사항 
  (use "git rm --cached <file>..." to unstage)
        new file:   a,txt  # a.txt 새로운 파일 생성

Untracked files: ## 트래킹 되고 있지 않은 파일들
  (use "git add <file>..." to include in what will be committed)
        b.txt

```



* 둘다 `add`한 후

```bash
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   a,txt
        new file:   b.txt


```

**다 된후엔 항상 `git status`를 통해 현재 상황을 확인해 보는 버릇을 들이자**

### 3. commit

`git`에서 이력을 남기기 위해서는 `commit`을 통해서 진행한다

`commit`을 남길 때에는 항상 커밋메세지를 작성한다. 

메세지는 해당 이력에 대한 정보를 담는다.

```bash
$git commit -m '커밋메세지'
[master (root-commit) dfc3afe] 커밋메세지
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 a,txt
 create mode 100644 b.txt


```

커밋 이력을 확인 하기 위해서는 아래의 명령어를 활용한다.

```bash
$git log
commit dfc3afec3b20240b16995e7a3941c702f0f77b7a (HEAD -> master)
Author: ahrtz <ahrtzzinn@gmail.com>
Date:   Mon Dec 9 14:25:50 2019 +0900

    커밋메세지
#이상태에서 
$git status
On branch master
nothing to commit, working tree clean

```

왜냐하면 모든 작업이력이 저장되었기 때문에 워킹 트리가 클린해진다. 

이후 변경사항이 발생하게 된다면, `add`->`commit`

이제부터 작업하다가 에러가 발생하면 과거 저장된 버전을 불러와서 작업할수 있게 된다. 

`add`: 커밋할 대상 파일 선정

`commit`: 이력의 확정 (스냅샷을 찍는다.)



## 원격저장소 (remote repository) 활용하기

> 원격저장소를 제공해주는 서비스는 다양하다. 
>
> 우리는 깃허브를 기준으로 활용해 보자 

### 0. 기본설정

Github에 비어있는 저장소 (repository) 생성

### 1. 원격 저장소 설정

```bash
$git remote add origin https://github.com/ahrtz/TIL
```

원격 저장소(`remote`)를 `origin`이라는 이름으로 `https://~url~`로 설정한다.

```bash
$git remote -v
origin  https://github.com/ahrtz/TIL (fetch)
origin  https://github.com/ahrtz/TIL (push)

# 이방법을 통해 저장된 원격 저장소 목록을 확인할 수 있다.
```



혹시 잘못 설정했다면 삭제가능하다

```bash
$git remote rm origin
```

### 2. push

원격 저장소에 업로드 하기 위해서는 `push`명령어가 필요하다.

```bash
$ git push origin master
```

`origin` 으로 설정된 저장소에 `push`한다.