FROM apache/airflow:2.6.0

USER root
RUN mkdir -p /opt/airflow/dags /opt/airflow/exports && \
    chown -R airflow:airflow /opt/airflow/dags /opt/airflow/exports
USER airflow

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
