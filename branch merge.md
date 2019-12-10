### 상황 1. fast-foward

1. feature/test branch 생성 및 이동

   ```bash
   $ git checkout -b feature/test
   Switched to a new branch 'feature/test'
   ```

   

2. 작업 완료 후 commit

   ```bash
   $ touch test.txt
   $ git add .
   $ git commit -m '브랜치 test 기능개발실습 완료'
   $ git log --oneline
   5c459f0 (HEAD -> feature/test) 브랜치 test 기능개발실습 완료
   64220ce (origin/master, master) Testbranch switch
   748e198 두번째 실습
   172653b 실습
   d9bf65e 다른 경로
   7ed17e6 연습
   b2f3076 멀캠에서 만든거
   
   ```
   
   


3. master 이동

   ```bash
   $ git checkout master
   $ git log --oneline
   64220ce (HEAD -> master, origin/master) Testbranch switch
   748e198 두번째 실습
   172653b 실습
   d9bf65e 다른 경로
   7ed17e6 연습
   b2f3076 멀캠에서 만든거
   
   ```
   
   


4. master에 병합

   ```bash
   $git merge feature/test
   Updating 64220ce..5c459f0
   ## Fast-forward 여기가 포인트
    test.txt | 0
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 test.txt
   
   ```
   
   


5. 결과 -> fast-foward (단순히 HEAD를 이동)

   그냥 단순하게 옮겨서 붙였다.

   

6. branch 삭제

   ```bash
   $git branch -d feature/test
   ```
   
   

---

### 상황 2. merge commit

> feature 브랜치에서 작업하고 있는동안,
>
> 마스터 브랜치에서 이력이 추가적으로 발생한 경우

1. feature/signout branch 생성 및 이동

   ```bash
   $ git checkout -b feature/signout
   Switched to a new branch 'feature/signout'
   
   ```

   

2. 작업 완료 후 commit

   ```bash
   $ touch signout.txt
   $ git add .
   $ git commit -m '컴플릿 사인아웃'
   [feature/signout 5ae18ba] 컴플릿 사인아웃
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 signout.txt
    
   $ git log --oneline
   5ae18ba (HEAD -> feature/signout) 컴플릿 사인아웃
   5c459f0 (origin/master) 브랜치 test 기능개발실습 완료
   64220ce Testbranch switch
   748e198 두번째 실습
   172653b 실습
   d9bf65e 다른 경로
   7ed17e6 연습
   b2f3076 멀캠에서 만든거
   
   
   ```

   

   

3. master 이동

   ```bash
   $ git checkout master
   Switched to branch 'master'
   Your branch is up to date with 'origin/master'.
   $ touch master.txt
   
   
   ```

   

4. *master에 추가 commit 이 발생시키기!!*

   * **다른 파일을 수정 혹은 생성하세요!**

   ```bash
   $ git log --oneline
   7c8c102 (HEAD -> master) 업데이트 마스터
   5c459f0 (origin/master) 브랜치 test 기능개발실습 완료
   64220ce Testbranch switch
   748e198 두번째 실습
   172653b 실습
   d9bf65e 다른 경로
   7ed17e6 연습
   b2f3076 멀캠에서 만든거
   ```

   

   

5. master에 병합

   ```bash
   $git merge feature/signout
   ```

   * vim 편집기화면이 나타난다 

      Enter + wq 로 나온다.

6. 결과 -> 자동으로 *merge commit 발생*

   

7. 그래프 확인하기

   ```bash
   $ git log --oneline --graph
   *   ae1b48e (HEAD -> master) Merge branch 'feature/signout'
   |\
   | * 5ae18ba (feature/signout) 컴플릿 사인아웃
   * | 7c8c102 업데이트 마스터
   |/
   * 5c459f0 (origin/master) 브랜치 test 기능개발실습 완료
   * 64220ce Testbranch switch
   * 748e198 두번째 실습
   * 172653b 실습
   * d9bf65e 다른 경로
   * 7ed17e6 연습
   * b2f3076 멀캠에서 만든거
   
   
   
   ```

   ![image-20191210135531206](images/image-20191210135531206.png)

branch를 먼저 가는 이유는 브랜치를 나중에 붙이면 마스터가 커밋했다는것을 브랜치에 저장해야 된다

그런데 브랜치를 먼저 커밋하면 한번에 된댄다

```bash
$ git branch -d feature/signout
Deleted branch feature/signout (was 5ae18ba).
```





---

### 상황 3. merge commit 충돌

1. feature/board branch 생성 및 이동

   ```bash
   $ git checkout -b hotfix/test
   
   ```

   

2. 작업 완료 후 commit

   > 텍스트 파일 hotfix.txt 직접만들고 수정
   
   그 이후 커밋까지 


3. master 이동

   ```bash
   $ git checkout master
   ```
   
   


4. *master에 추가 commit 이 발생시키기!!*

   * **동일 파일을 수정 혹은 생성하세요!**

   > 마스터 루트로 간후 폴더에 hotfix.txt 새로 생성

5. master에 병합

   ```bash
   $git merge hotfix/test
   ```
   
   


6. 결과 -> *merge conflict발생*

   ```bash
   $ git merge hotfix/test
   CONFLICT (add/add): Merge conflict in hotfix.txt
   Auto-merging hotfix.txt
   Automatic merge failed; fix conflicts and then commit the result.
   
   student@M160423 MINGW64 ~/Desktop/연습/멀캠/web (master|MERGING) ## 여기 뒤가 다르게 나옴
   ## 충돌 확인 
   
   ```
   
   


7. 충돌 확인 및 해결

   ```bash
   $ git status
   On branch master
   Your branch is ahead of 'origin/master' by 1 commit.
     (use "git push" to publish your local commits)
   
   You have unmerged paths.
     (fix conflicts and run "git commit")
     (use "git merge --abort" to abort the merge)
   
   Unmerged paths:
     (use "git add <file>..." to mark resolution)
           both added:      hotfix.txt
   
   no changes added to commit (use "git add" and/or "git commit -a")
   
   ```
   
   ![image-20191210144816427](images/image-20191210144816427.png)






8. merge commit 진행

    ```bash
    $ git add .
    $ git commit
```
   
   * vim 편집기 화면이 나타납니다.
   
   * 자동으로 작성된 커밋 메시지를 확인하고, `esc`를 누른 후 `:wq`를 입력하여 저장 및 종료를 합니다.
      * `w` : write
      * `q` : quit
      
   * 커밋이  확인 해봅시다.
   
9. 그래프 확인하기

    ```bash
   $ git log --oneline --graph
   *   0931db0 (HEAD -> master) Merge branch 'hotfix/test'
   |\
   | * 0024b07 (hotfix/test) 핫픽스파일 수정
   * | f49033a master hotfix
   |/
   *   ae1b48e (origin/master) Merge branch 'feature/signout'
   |\
   | * 5ae18ba 컴플릿 사인아웃
   * | 7c8c102 업데이트 마스터
   |/
   * 5c459f0 브랜치 test 기능개발실습 완료
   * 64220ce Testbranch switch
   * 748e198 두번째 실습
   * 172653b 실습
   * d9bf65e 다른 경로
   * 7ed17e6 연습
   * b2f3076 멀캠에서 만든거
   
    ```
   
   


10. branch 삭제

    
