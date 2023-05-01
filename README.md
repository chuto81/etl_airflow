# Data Engineer Challenge

This repository builds an Airflow ETL for a CSV file using Python.

## 1. Requirements to Install Airflow

Follow these steps to install **Docker** and **Docker Compose**, if you have not already done so.

1. Install [Docker](https://docs.docker.com/engine/install/) version 23.0.5 on your workstation.
2. Install [Docker Compose](https://docs.docker.com/compose/install/) version 2.17.3 or newer on your workstation.

## 2. Run on your Linux Terminal

Run the following command in your CLI:

`$ docker compose up`

## 3. Open your port 8080 in your web browser to use Airflow

Wait a few minutes until **Docker Compose** build the Airflow container

When it is ready, open your browser  and go to this address:

`http://localhost:8080/`

That opens the Airflow application, as seen in the following image:
![Airflow Application](https://user-images.githubusercontent.com/43504731/235488613-afd057b4-beb4-4dcc-b61b-d9e7e1fb5cf7.png)

Use these credentials to enter:
- login = *airflow*
- password = *airflow*

## 4. Run the DAG

The Dag is schedule to run every day at midnight. But, you could run ti by press on play icon at Actions menu in DAG's.

Like this image:
![Airflow DAG](https://user-images.githubusercontent.com/43504731/235488761-c3af4bf0-4be8-4e4e-bd8b-441076b646b4.png)

Make sure all your dags have succeeded

# FAQ

## Change permissions on your "exports" folder

If your last dag have failed, maybe you have to chance the permissions of your "exports" folder

Run the following command in your CLI:

`sudo chown $USER:root exports`

## About the data input

The csv file *Traffic_Flow_Map_Volumes.csv* does not have accident or weather information.

However, the following line would calculate the total number of accidents by type of weather on a dataframe with the right data.

`accidents_by_weather = data_clean.groupby("WEATHER")["OBJECTID"].count().reset_index(name="accidents_count")`
