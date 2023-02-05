echo " BUILD START"
python3.2.5 -m pip install -r requirements.txt
python3.2.5 manage.py collectstatic --noinput --clear
echo " BUILD END"
