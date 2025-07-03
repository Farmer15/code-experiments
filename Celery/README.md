## Celery
  - 작업(task)를 등록하고 메세지 브로커와 워커(worker) 간의 연결을 추상화하여 쉽게 구성할 수 있도록 도와주는 프레임 워크입니다.(참고: https://docs.celeryq.dev/en/stable/index.html)

### 역할
1. 작업을 적의하고 등록해 줍니다.
    ```python
        @app.task
        def add(x, y):
            return x + y
    ```

2. 작업을 메세지로 만들어 브로커에 전송해줍니다.
    ```python
        add.delay(7, 8)
    ```

3. 브로커에서 작업을 꺼내 워커(worker)가 실행하고 처리할 수 있도록 연결해줍니다.
    ```python
        # worker를 프로세스로 이용
        celery -A myapp worker --loglevel=info
    ```

4. 여러가지 부가적인 기능들 제공
    * 성공/실패 여부를 모니터링 하여 추적 할 수 있게 도와줍니다.
    * 작업 실패시 재시도 처리를 도와줍니다.
    * 작업 스케줄링 관련해서 도와줍니다.


### 기본 셋팅
1. 가상 환경을 만들어줍니다.
    ```javascript
    //만들기
    1. conda create --name [환경이름] python=[버전]

    // 실행하기
    2. conda activate [환경이름]

    // 끄기
    3. conda deactivate

    // 삭제
    4. conda remove --name [환경이름] --all
    ```
2. 프레임워크를 이용해서 간단한 서버 환경을 구축해줍니다.
    - 여기선 python 기반 fastAPI 이용해서 main.py 만들기 (참조: https://fastapi.tiangolo.com/#installation)
    - requirements.txt 목록과 dockerfile 이미지를 만들어줍니다.
    - docker-compose.yml 에 작성하여 컨테이너로 실행되게 해줍니다.
3. docker 를 이용해서 RabbitMQ를 실행시켜줍니다.
    - 중간에 메세지를 관리해주어야 하기 때문에 별도의 서버로써 띄워주어야 합니다.
    - RabbitMQ는 메시지 브로커 역할을 하는 별도의 서버(서비스)이기 때문에 항상 실행되고 있어야 메시지를 주고받을 수 있습니다.
    - docker-compose.yml 에서 이미지를 불러와 컨테이너 만들어 실행해줍니다.
      ```
      docker-compose up -d
      ```

### 실험 과정
1. tasks.py 를 만들어서 작업(task)을 브로커(RabbitMQ)로 보내줍니다.
2. 공식문서에서는 worker를 프로세스로 이용하여 터미널을 통해 실행시켜주었습니다.
    ```python
        # worker를 프로세스로 이용
        celery -A myapp worker --loglevel=info
    ```



