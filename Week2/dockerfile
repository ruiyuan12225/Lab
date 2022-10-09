# as of 9/29/22 3.10.7 was latest 
FROM python:3.10.7 AS build
USER root
RUN apt-get update && apt-get install wget
RUN pip3 install jupyter
#run in Jupyter pip freeze > requirements.txt to get the requirment should include matplotlib, panadas, and seaborn
COPY requirements.txt .
RUN pip3 install -r requirements.txt
#RUN pip3 install pandas
ENV JUPYTER_USER our_user
RUN useradd -ms /bin/bash ${JUPYTER_USER}


EXPOSE 8888

USER ${JUPYTER_USER}
WORKDIR /home/notebook/

RUN wget https://raw.githubusercontent.com/mschermann/forensic_accounting/master/Introduction.ipynb

CMD jupyter notebook --ip=0.0.0.0 --port 8888 --allow-root

#docker build -t hw .  
#docker run -p8888:8888 hw
