# pledgeScript
pledge v2 script


####  Timed task script

**介绍**

- 语言
  - python
- 框架
  - Flask
- 节点信息
  - bsc 测试网
  - bsc 主网
- 部署
  - docker部署


**部署命令**
- 开发环境：
  - development:
    - 构建镜像：docker build -t script:1.0  -f DockerfileTest .
    - 启动容器：docker run --name pledgescript -p 58480:58480  -v/home/docker_code/logs/pyservice_log:/logs/pyservice_log   -v /home/docker_code/logs/segmentation_log:/logs/segmentation_log  --privileged=true   -d script:4.0
