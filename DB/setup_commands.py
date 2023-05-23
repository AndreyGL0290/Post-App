from dotenv import load_dotenv
load_dotenv()

import sys
from os import getenv
sys.path.append(getenv('WORKING_DIRECTORY'))

from DB.connection import SQLiteConnection

def create():
    with SQLiteConnection() as sql:
        sql.cur.execute('CREATE TABLE posts (id integer primary key autoincrement, post_text varchar(65536))')

def delete():
    with SQLiteConnection() as sql:
        sql.cur.execute('DROP TABLE posts')

def refresh():
    try:
        delete()
        create()
    except:
        create()

def initial_data():
    with SQLiteConnection() as sql:
        sql.cur.execute('INSERT INTO posts (post_text) VALUES ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam et ex eros. Donec condimentum id nulla et pharetra. Phasellus et blandit massa. Donec elit tellus, maximus nec pretium ut, suscipit a mi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean egestas vehicula commodo. Nullam rutrum arcu aliquet nisl consectetur tincidunt vel a enim. Curabitur eu lacus ac nulla egestas tristique nec vitae tellus. Quisque et risus molestie, blandit dolor id, egestas velit. Donec tempor eget velit id suscipit. Duis eleifend lectus purus, nec commodo est blandit a.")')
        sql.cur.execute('INSERT INTO posts (post_text) VALUES ("Etiam auctor nisl at odio blandit egestas et sed eros. Aliquam erat volutpat. Vivamus iaculis nisi ut dui bibendum, nec hendrerit nisi mattis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vestibulum et nunc pellentesque lacus porta convallis. Vivamus pellentesque ultrices lorem. Ut metus massa, iaculis sed turpis a, semper semper urna. Sed ac elementum dui. Quisque bibendum orci elit, quis efficitur lectus dictum at. Curabitur odio mauris, blandit eget iaculis id, placerat sed nisl. Cras a libero dignissim, euismod nunc id, euismod sapien. Phasellus lorem velit, consectetur ac diam ut, cursus tempor velit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Etiam nisi dui, blandit at justo in, commodo ultricies tellus. Phasellus nec eros enim.")')
        sql.cur.execute('INSERT INTO posts (post_text) VALUES ("Mauris eu ligula a sapien varius finibus non vitae metus. Nullam vitae augue ultrices, condimentum justo a, condimentum risus. Curabitur eleifend ullamcorper vulputate. Nunc tincidunt nulla dolor, sed auctor ex efficitur id. Donec ac ex ac ipsum convallis congue ac ultricies nunc. Nam ut lorem congue, ultricies mauris in, suscipit sapien. Praesent molestie efficitur dolor at lobortis. Donec euismod ex est, eget mattis nisi efficitur vel. Quisque sem nulla, blandit nec tortor et, ultricies sodales metus. Sed et est luctus, elementum ipsum ac, sodales nunc. Integer eu justo at nisi euismod euismod.")')