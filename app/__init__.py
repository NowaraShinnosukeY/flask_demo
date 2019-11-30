from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app.emp.views import emp_blue

app.register_blueprint(emp_blue)








'''
INSERT INTO `flask_db`.`employee`(`id`, `name`, `age`, `salary`) VALUES (1, 'Tom', 20, 1234.00);
INSERT INTO `flask_db`.`employee`(`id`, `name`, `age`, `salary`) VALUES (2, 'Jack', 22, 2345.00);
INSERT INTO `flask_db`.`employee`(`id`, `name`, `age`, `salary`) VALUES (3, 'CJP', 24, 3456.00);
INSERT INTO `flask_db`.`employee`(`id`, `name`, `age`, `salary`) VALUES (4, 'Ego', 23, 4567.00);
INSERT INTO `flask_db`.`employee`(`id`, `name`, `age`, `salary`) VALUES (5, 'HHH', 22, 5678.00);
INSERT INTO `flask_db`.`employee`(`id`, `name`, `age`, `salary`) VALUES (6, 'Dor', 18, 11111.00);
INSERT INTO `flask_db`.`employee`(`id`, `name`, `age`, `salary`) VALUES (7, 'ooo', 11, 12345.00);
'''