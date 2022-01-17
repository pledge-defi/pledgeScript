FROM python:3.6
MAINTAINER skyscraper <skyscraper@yikaixiong.com>
ENV TZ=Asia/Shanghai


ENV FLASK_ENV=PRODUCTION

# BSC wallet
ENV PLEDGE_CONTRACT_ADDRESS=0x78CE5055149Dc30755612209f9d9A98f36fb022E
ENV BEP20_CHAIN_ID=56
ENV BEP20_GAS_LIMIT=800000
ENV BEP20_GAS_PRICE_LIMIT=50000000000
ENV BEP20_NODE=https://bsc-dataseed.binance.org
ENV FINANCE_ADDRESS=0x2035F495e69FC970d8916E18Fc977F0Cb09883d0
ENV FINANCE_ADDRESS_SERECT=...

RUN mkdir -p /code
RUN mkdir -p /logs
ADD . /code
WORKDIR /code

RUN pip install --upgrade pip setuptools==45.2.0
RUN pip install -r requirements.txt 
RUN chmod +x start_service.sh
EXPOSE 58482

CMD ["./start_service.sh"]
