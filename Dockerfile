FROM python

WORKDIR /src

COPY . .

RUN pip install flask

EXPOSE 7070

CMD python app.py

