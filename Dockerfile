FROM python:3.8
#Create a Env for virtual environment
# ENV VIRTUAL_ENV=/opt/venv
# RUN python3 -m venv $VIRTUAL_ENV
# ENV PATH="$VIRTUAL_ENV/bin:$PATH"
#Copying project files to the usr/src/app directory
COPY . /usr/src/app
#Defining the directory where the CMD will run and copying the requirements file
WORKDIR /usr/src/app
COPY requirements.txt ./
# Installing requirements with PIP
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
# Exposing the APP port
EXPOSE 5000
# Executing the command to run the application
CMD [ "python", "./manage.py" ]
