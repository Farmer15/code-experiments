## 1. RabbitMQ_Work_Queues

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
3. docker 를 이용해서 RabbitMQ를 실행시켜줍니다.
    - 중간에 메세지를 관리해주어야 하기 때문에 별도의 서버로써 띄워주어야 합니다.
    - RabbitMQ는 메시지 브로커 역할을 하는 별도의 서버(서비스)이기 때문에 항상 실행되고 있어야 메시지를 주고받을 수 있습니다.
    - docker-compose.yml 에서 이미지 작성한 후 실행
      ```
      docker-compose up -d
      ```

### 실험 과정
1. new_task.py 와 worker.py를 만들어줍니다.
    - new_task.py : 작업을 RabbitMQ에 등록하는 생산자
    - worker.py : 작업을 RabbitMQ에서 소비해서 사용하는 소비자

2. new_task.py 을 실행하여 해당 작업(task)을 RabbitMQ에 task_queue 라는 작업 큐에 넣어줍니다.

3. worker.py 을 실행하여 RabbitMQ에 task_queue에 저장된 작업(task)를 하나씩 꺼내서 수행해줍니다.
    - 예시에서는 메세지로 보낸 '.' 개수 만큼 쉼으로써 작업을 하는것을 표현
    - worker.py 를 실행 한 상태로 두면 지속적으로 꺼내서 작업을 수행합니다.
    - 여러개의 worker.py 를 실행 하면 앞선 worker 에서 꺼낸 작업 뒤로 이어서 꺼내 작업합니다.



