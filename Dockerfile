FROM python:3.10

COPY slim_requirements.txt ./src/slim_requirements.txt
RUN pip3 install -r ./src/slim_requirements.txt
EXPOSE 8501
COPY ./src /src
ENTRYPOINT ["streamlit", "run"]
CMD ["src/streamlit_app.py"]