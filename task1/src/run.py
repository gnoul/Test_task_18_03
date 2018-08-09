import config
from app import app

app.run(debug=config.DEBUG, host='0.0.0.0')
