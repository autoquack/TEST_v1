Contents of the.gitlab - ci.yml file:

image: python:3.8

test:
    script:
        - pip install django
        - python manage.py test

Committing the.gitlab - ci.yml file:

git add.gitlab - ci.yml
git commit - m "added gitlab-ci"
git push

Committing changes to the Gitlab project:

git add - u
git commit - m "Made test to fail to demonstrate failed pipeline"
git push