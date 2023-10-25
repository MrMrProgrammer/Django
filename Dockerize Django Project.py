# ===========================================================
# Terminal

# 1. Create an image :

    # docker build -t image-name .


# 2. Create a container :

    # docker run -d -p 8000:8000 -v /path/to/project/directory:/app image-name python manage.py runserver 0.0.0.0:8000

    # (Give the address of your project instead of /path/to/project/directory)


# ===========================================================