FROM    python:3.10
WORKDIR /project
COPY    ./app ./app 
COPY    ./run.py .
COPY    ./requirements.txt .
COPY    ./.env .
COPY    ./cert ./cert
COPY    ./docs ./docs
RUN     pip install --no-cache-dir -r requirements.txt 
EXPOSE  <THE PORT FOR WEBHOOK HERE>

ENTRYPOINT ["python", "run.py", ">", "/dev/null"]
