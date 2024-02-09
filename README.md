# imagePrinter

## 소개

`imagePrinter`는 파이썬 `openCV`를 활용한 터미널에 이미지를 출력하는 프로젝트 입니다. 터미널의 명령어로 사용하거나 모듈로 불러올 수 있습니다.

터미널

```
$ pimg.py <이미지 경로> <이미지 가로 크기>
```

모듈화

```python
from pimg import imagePrinter

image = imagePrinter('nyan.png', 30)
image.print()
```

## 사용예

```
$ pimg nyan.png 40
```

![image](https://user-images.githubusercontent.com/83404333/146379985-cf1017af-ef3a-4087-a449-9dc6f5fba1dd.png)

물론 웹에 올라가있는 이미지 역시 사용할 수 있습니다.

![cat](https://i.imgur.com/JYfJ2vr.jpg)

```
$ pimg.py https://i.imgur.com/JYfJ2vr.jpg 80
```

![image](https://user-images.githubusercontent.com/83404333/146389465-13941f11-0a5c-4475-a2cf-785aac258308.png)
