# Git 추가 설명

## 1. commit

> commit을 통해 이력을 확정하면 hash 값이 부여되며 이 값을 통해 동일한 커밋인지를 확인한다.

WD변화 X, staging area 비어있을때

변경사항 x 

```bash
$ git commit
nothing to commit, working tree clean

```

WD 변화 O, staging area 비어있을때

```bash
$ git commit
On branch master
Your branch is ahead of 'origin/master' by 3 commits.
  (use "git push" to publish your local commits)

Untracked files:
        qwe.txt

nothing added to commit but untracked files present
```

## commit 메세지 작성하기 

> vim활용법

```bash
$ git commit 
```

vim 에는 두가지 모드가 있다

* 편집모드(단축키 i)

> 문서 편집가능

* 명령모드(esc로 나가기)

  * > dd : 해당 줄 삭제

    > :wq 저장 및 종료

    > :q! 강제 종료 

## log 활용하기

```bash
$ git log
$ git log --oneline
$ git log -1 
$ git log -1 --oneline
```

* HEAD : 현재 작업하고 있는 커밋 이력 및 브랜치에 대한 정보 

~~~bash
0931db0 (HEAD -> master) Merge branch 'hotfix/test'
# 나는 현재 마스터 브랜치에있고
#0931 커밋한 상태
~~~

* 예시)

```bash
$ git log --oneline
0931db0 (HEAD -> master) Merge branch 'hotfix/test'
f49033a master hotfix
0024b07 (hotfix/test) 핫픽스파일 수정

# 나는 마스터 브랜치에서 커밋했고 
# 앞의 숫자는 해쉬
```



## 직전 커밋 메세지 수정

> 아래의 명령어는 ***커밋 이력을 변경*** 하기 때문에 조심해야 한다.
>
> 공개된 저장소에 이미 push된 이력이라면 ***절 대*** 해서는 안된다.

```bash
$ git commit --amend ## vim에디터에서 커밋 메모 변경가능
# 잘 쓰지 않는다 로컬로 할때에만 사용
```

## commit시 특정 파일을 빠뜨렸을때 

> 만약 staging area 에 특정 파일(omit.txt)을 올리지 않아서 커밋이 되지 않았을 때!

```bash
$ git add omit.txt
$ git commit --amend
```

## 2. staging area

이미 커밋이 있는 파일이 수정되었을때

```bash
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   omit.txt

no changes added to commit (use "git add" and/or "git commit -a")

```

커밋이력이 없는 파일이 추가 되었을때 

```bash
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   omit.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        alpha.txt

no changes added to commit (use "git add" and/or "git commit -a")

```



```bash
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   omit.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        alpha.txt

```

### add 취소하기

```bash
$ git restore --staged <file>

```

* 구버전 git 에서는 아래의 명령어를 사용해야 한다.

```bash
$ git reset HEAD <file>

```

### working directory 변화 삭제하기

```bash
$git restore <file>
#구버전
$ git checkout -- <file>
```

# 주의

> git 에서는 모든 commit 된 내용은 되돌릴수 있다. 
>
> 다만 WD내용을 삭제하는 것은 되돌릴수 없다. 

# stash?

특정상황에 발생합니다. 이럴땐 stash하세여

> stash 란?
>
> 변경사항을 임시로 저장 해놓는 공간이다. 

## 예시상황

> 1. feature branch 에서 a.txt를 변경후 커밋
> 2. 마스터 브랜치에서 a.txt를 수정 (add/commit 하지않음)
> 3. merge





```bash
$ git merge test
# merge 명령으로 인해 덮어쓰기 오류 발생 
error: Your local changes to the following files would be overwritten by merge:
        a.txt
Please commit your changes or stash them before you merge.

# commit 하거나 --> 이력 확정해서 머지 충돌 시퀀스로
# stash 하거나 --> 워킹디렉토리 잠시 비워놓고 진행

Aborting
Updating cf66703..ac2a815

```







```bash
$ git stash
Saved working directory and index state WIP on master: cf66703 txt생성
# 쟁여놓기
$ git stash list
stash@{0}: WIP on master: cf66703 txt생성
# stash 리스트 보여주기
$ git stash pop
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   a.txt

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (e58711fc3de70e909e9c10843f959797445fd74f)
#stash 에 있는거 꺼내오기
```

어떻게 쓰냐

```bash
$ git merge test
error: Your local changes to the following files would be overwritten by merge:
        a.txt
Please commit your changes or stash them before you merge.
Aborting
Updating cf66703..ac2a815

$ git stash
Saved working directory and index state WIP on master: cf66703 txt생성

$ git merge test
Updating cf66703..ac2a815
Fast-forward
 a.txt | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)

$ git stash pop
Auto-merging a.txt
CONFLICT (content): Merge conflict in a.txt
The stash entry is kept in case you need it again.

# 그후에 작업해서 수정
```

> 첫번째 내용!
> <<<<<<< Updated upstream
> test branch 내용
> =======
> 으앙
> 난 수정중
>
> >>>>>>> Stashed changes







# reset vs revert

> commit 이력을 되돌리는 작업을 한다

리셋은 혼자 할때만 사용 (원격저장소에는 쓰지 말라이말이야)

* `reset` : 이력을 삭제한다.
  * `--mixed`: 기본 옵션, 해당 커밋 이후 변경사항 staging area 에 보관  
  *  `--hard`: 해당 커밋 이후 변경사항 모두 삭제
  * `--soft`: 해당 커밋 이후 변경사항 및 working directory 내용까지 모두 보관
* `revert`: 되돌렸다는 이력을 남긴다.







