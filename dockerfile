# ourbase image7
FROM alpine:latest
# Install python and pip
RUN apk add --update py3-pip
# upgrade pip
RUN pip install --upgrade pip
# install Python modules neededby the Python app
RUN pip install --no-cache-dir Flask
# copy files requiredfor the apptorun
COPY api-get.py /usr/src/app/
#COPY templates/index.html /usr/src/app/templates/
# tell the port numberthe container shouldexpose
EXPOSE 80
# runthe application
CMD ["python3" , "/usr/src/app/api-get.py"]
