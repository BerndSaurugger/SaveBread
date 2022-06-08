FROM python:3.10

COPY requirements.txt ./src/requirements.txt
RUN pip3 install -r ./src/requirements.txt
EXPOSE 8501
COPY ./src /src
ENTRYPOINT ["streamlit", "run"]
CMD ["src/streamlit_app.py"]