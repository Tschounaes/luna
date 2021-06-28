FROM continuumio/miniconda3:latest

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

#wget for frontend
RUN apt-get update && apt-get upgrade -y && apt-get install wget -y

#frontend
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - && apt-get install -y nodejs && apt-get install -y npm


RUN mkdir -p /backend
#frontend
RUN mkdir -p /frontend
RUN mkdir -p /frontend_tmp
RUN mkdir -p /script
RUN mkdir -p /static-files

COPY ./backend /backend
RUN /opt/conda/bin/conda env create -f /backend/requirements.yml
ENV PATH /opt/conda/envs/luna/bin:$PATH

RUN echo "source activate luna" >~/.bashrc

COPY ./script /script
RUN chmod +x ./script*

WORKDIR /backend

# frontend
WORKDIR /frontend_tmp
COPY ./frontend/package.json /frontend_tmp/
#COPY ./frontend/package-lock.json /frontend/
RUN npm install
COPY ./frontend /frontend_tmp
RUN npm run build

# for gunicorn to connect to backend directory instead of frontend
WORKDIR /backend