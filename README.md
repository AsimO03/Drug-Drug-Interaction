# drug-drug-interaction

This project needs a CSV that lists drug interactions as a database.  
You can download the one used in development here:  
https://samwald.info/res/CombinedDatasetConservative.csv.zip  
Please download it and place it into the root of the project.

## Install required package(s)
```
pip install -r requirements.txt
```

## Configure the environment and start the Flask app

Bash:
```
    export FLASK_APP=hello
    export FLASK_ENV=development (optional)
    flask run
```
CMD:
```
    set FLASK_APP=hello
    set FLASK_ENV=development (optional)
    flask run
```
Powershell:
```
    $env:FLASK_APP = "hello"
    $env:FLASK_ENV = "development" (optional)
    flask run
```


## Docker
Build the Image:
```
docker build --tag ddi .
```

Run the Image
```
docker run -d -p 5000:5000 ddi
```