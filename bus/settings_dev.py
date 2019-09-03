User_Agent = ['Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45',
              'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
              'Chrome/55.0.2883.87 UBrowser/6.2.4094.1 Safari/537.36']

BUS_URL_SEARCH = 'http://bm.eyuyao.com/bus/mobile/lineList.php?k=pp&q={}'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bus',
        'USER': 'root',
        'PASSWORD': '13486059134chen',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'isolation_level': 'repeatable read',
        },
        'CONN_MAX_AGE': 60,
        'ATOMIC_REQUESTS': True
    }
}