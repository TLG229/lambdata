FROM debian

WORKDIR /usr/src/app

COPY example_module.py .

###So logging/io works reliably w/ Docker
ENV PYTHONUNBUFFERED=1

###Need to explicitly set this so 'pipenv shell' works
ENV SHELL=/bin/bash

###Basic Python dev dependencies
RUN apt-get update && apt-get upgrade -y && \
apt-get install python3-pip curl nano -y && \
pip3 install pipenv

### install via pip or pipenv:
RUN pip3 install pandas numpy 
#RUN pipenv install pandas

CMD ["python", "./example_module.py"]
