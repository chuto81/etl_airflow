# Data Engineer Challenge for TalentPitch
Airflow ETL for a CSV file in Python


Server: Docker Engine - Community
 Engine:
  Version:          23.0.5

  Docker Compose version v2.17.3



El archivo csv *Traffic_Flow_Map_Volumes.csv* no tiene información de accidentes, ni de clima
No obstante la siguiente linea calcularía el número total de accidentes por tipo de clima
accidents_by_weather = data_clean.groupby("WEATHER")["OBJECTID"].count().reset_index(name="accidents_count")


sudo chown $USER:root exports

