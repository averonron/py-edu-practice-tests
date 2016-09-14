# py-edu-practice-tests

# To avoid prompt username and password
# 1.
# git remote set-url origin https://username:password@github.com/averonron/py-edu-practice-tests.git
#
# 2.
# git config --global credential.helper cache
# # git will cache password for 15 minutes
# git config --global credential.helper 'cache --timeout=3600'
# # set the cache to timeout after 1 hour (setting is in seconds)

The point of this helper is to reduce the number of times you must type your username or password. For example:

$ git config credential.helper store
$ git push http://example.com/repo.git
Username: <type your username>
Password: <type your password>

[several days later]
$ git push http://example.com/repo.git
[your credentials are used automatically]
