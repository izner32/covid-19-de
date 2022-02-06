FROM puckel/docker-airflow:1.10.9 

ENV AIRFLOW_HOME=/usr/local/airflow
ENV PYTHONPATH "${PYTHONPATH}:${AIRFLOW_HOME}"

RUN pip install pandas 
RUN pip install python-dotenv
RUN pip install boto3 