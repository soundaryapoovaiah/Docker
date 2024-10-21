# Use a lightweight base image like python:3.9-slim or ubuntu
From python:3.9-slim 

#set working directory in the container 
WORKDIR /home/data

#copy the text files and the python script into the container 
COPY IF.txt AlwaysRememberUsThisWay.txt /home/data/
COPY scripts.py /home/data/

#Install necessary packages for handling text or contractions
RUN pip install --no-cache-dir contractions

#Run the Python script when the container starts 
CMD ["python3", "/home/data/scripts.py"]
