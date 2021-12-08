# pledgeScript
pledge v2 script


####  Timed task script

**Introduce**

- Language
  - python
- Frame
  - Flask
- Node Info
  - bsc test network
  - bsc main network
- Deploy
  - docker deploy
- Effect
  - Timed monitoring


**Deployment command**
- Development：
  - development:
    - Images：docker build -t script:1.0  -f DockerfileTest .
    - Container：docker run --name pledgescript -p 58480:58480  -v/home/docker/logs/pyservice_log:/logs/pyservice_log   -v /home/docker/logs/segmentation_log:/logs/segmentation_log  --privileged=true   -d script:1.0
