FROM python:3.8.9

RUN pip3 install pyyaml requests
COPY /src /src

ENTRYPOINT ["/usr/local/bin/python3","-u","/src/monitor.py"]
CMD ["src/default.yaml"]