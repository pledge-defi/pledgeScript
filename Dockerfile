FROM python:3.6
MAINTAINER skyscraper <skyscraper@yikaixiong.com>
ENV TZ=Asia/Shanghai


ENV FLASK_ENV=PRODUCTION

# BSC wallet
ENV PLEDGE_CONTRACT_ADDRESS=0x55d398326f99059fF775485246999027B3197955
ENV BEP20_CHAIN_ID=56
ENV BEP20_GAS_LIMIT=200000
ENV BEP20_GAS_PRICE_LIMIT=50000000000
ENV BEP20_NODE=https://bsc-dataseed.binance.org
FINANCE_ADDRESS=0x0ff66Eb23C511ABd86fC676CE025Ca12caB2d5d4
FINANCE_ADDRESS_SERECT=

RUN mkdir -p /code
RUN mkdir -p /logs
ADD . /code
WORKDIR /code

RUN pip install --upgrade pip setuptools==45.2.0
RUN pip install -r requirements.txt 
RUN chmod +x start_service.sh
EXPOSE 58480

CMD ["./start_service.sh"]
