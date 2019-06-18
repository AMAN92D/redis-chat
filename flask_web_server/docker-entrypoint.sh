python3 --version &
chmod 644 ./chatServer.py &
echo $(sleep 3)
python init_db.py &
python ./chatServer.py