FROM hexacta/sklearn-predict-http-api:latest

RUN conda install scikit-learn

WORKDIR /var/www/server

CMD [ "python", "./server.py" ]