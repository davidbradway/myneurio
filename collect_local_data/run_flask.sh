echo "go to http://192.168.1.[PIIP]:5000/[LABEL]"
echo "   or http://192.168.1.[PIIP]:5000/r/[LABEL]"
FLASK_APP=app.py flask run --host=0.0.0.0
