FROM python:3.6
MAINTAINER skyscraper <skyscraper@yikaixiong.com>
ENV TZ=Asia/Shanghai


ENV FLASK_ENV=PRODUCTION

# BSC wallet
ENV PLEDGE_CONTRACT_ADDRESS=..
ENV BEP20_CHAIN_ID=56
ENV BEP20_GAS_LIMIT=800000
ENV BEP20_GAS_PRICE_LIMIT=10000000000
ENV BEP20_NODE=https://bsc-dataseed.binance.org
ENV FINANCE_ADDRESS=..
ENV FINANCE_ADDRESS_SERECT=...

RUN mkdir -p /code
RUN mkdir -p /logs
ADD . /code
WORKDIR /code

RUN pip install --upgrade pip setuptools==45.2.0
RUN pip install -r requirements.txt 
RUN chmod +x start_service.sh
EXPOSE 58480

CMD ["./start_service.sh"]
