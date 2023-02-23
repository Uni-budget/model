# ocr 
This is a repository for implementing image/text value transfer through get/post method between Android studio and flask server using python.

### How to run?
![image](https://user-images.githubusercontent.com/66208800/206129058-ac2b549d-a02d-4380-9bb3-f6ebb2b50f6c.png)

+ In cmd..
  1) ngrok 사이트 로그인 후 ngrok zip 파일 받아 압축해제
  2) open cmd 
  3) cd 압축해제된 파일 폴더명
  4) ngrok config add-authtoken {토큰 입력} ex) 2HnBIcpGUbZ1pdR5RaTNTlBURmO_4npSCfYrDTJu1PQ83YC5w (Yujeong)
  5) ngrok http {port 주소}
  6) 생성된 주소 ctrl+c
+ In pycharm..
  1) pull ocr git repository
  2) enter "flask run" in terminal
+ In android studio..
  1) TestActivity.kt 109 line에서 val postUrl = "{복사한 서버 주소}/getpost" 중괄호 안에 주소 ctrl+v
  2) run android studio!

+ Reference: donut api🍩: Document Understanding Transformer
