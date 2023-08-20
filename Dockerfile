FROM python:3.8.9

RUN pip3 install pyyaml
COPY /src /src

EXPOSE 80
ENTRYPOINT ["/usr/local/bin/python3","/src/monitor.py"]
CMD ["default.yaml"]