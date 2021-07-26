# 텐서 공부



## model checkpoint 에 대해 (중요!)

최고의 accuracy 혹은 loss 가 나온 에포크를 임시 저장해준다. 

모델이 가지고 있는 weight 를 저장한다. 

그래서 최고로 fit 했던 녀석걸 뽑아온다. 

```python
checkpoint_path = "my_checkpoint.ckpt"
checkpoint = ModelCheckpoint(filepath = checkpoiont_path,
                            save_weights_only= True,
                            save_best_only = True,
                            monitor='val_loss',
                            verbose=1) # 로그 출력 관련 메세지 

history = model.fit(x_train,y_train,
                   validation_data = (x_valid,y_valid),
                   epochs=20,
                   callbacks=[checkpoint],)

# 모든 학습이 끝난 후 
model.load_weights(checkpoint_path)
```



# 원 핫 인코딩

봄 여름 가을 겨울 <- 숫자로 변환시켜줘야 파이썬이 이해할수잇다 

그러나 0,1,2,3 을 하다보면 

0+1은 1 이 되서 이렇게 넣으면 안된다. 

어케하냐? 

[1,0,0,0], [0,1,0,0] ... 이런식으로 해야된다.

# 활성함수란? 

dense layer 는 ax+b로 이루어진 선형함수로 생각해도 된다. 

선형함수만 깊게 쌓으면 선형*선형 으로 => 복잡한거 못푼다 

그래서 

선형

비선형

선형

비선형 이렇게 쌓는다

relu,sigmoid, softmax면 앵간한거 다된다. 

# 중요

( 이진 분류)  2개분류할때 

마지막 레이어가 sigmoid인경우  loss 는 binary_crossentropy 사용 

마지막 레이어가 softmax인경우  loss 는 categorical_crossentropy 혹은 sparse_catrgorical_crossentropy

원핫 인코딩이 되어있으면 categorical 

아니면 sparse 사용 



