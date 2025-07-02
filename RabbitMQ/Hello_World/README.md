## 1. RabbitMQ_Hello_World

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
1. send.py 와 receive.py를 만들어줍니다.

2. send.py 를 실행하여 설정한 메세지 큐에 작업을 넣어줍니다.

3. receive.py 를 켜서 저장된 메세지 큐 task 작업들을 꺼내서 처리해줍니다.
  - 켜 놓은 상태로 send.py 를 실행 할 경우 즉각 적으로 send.py 실행할때 마다 처리됩니다.



