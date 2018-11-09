# safeurl

The safeurl project is a URL lookup service that maintains a database of blacklisted URLs accessible by an API.
It follows RESTful principles and uses JSON as its data interchange format.

## Technical Details

The API is implemented in Python's Flask-RESTful framework connecting to a Flask-SQLAlchemy sqllite backend for development.
Flask-RESTful removes tedious boilerplate code for specifying request and response format.
Flask-SQLAlchemy provides tidy ORM that ties in well with Flask API calls.

There are multiple slave DB instances (views) in AWS accessible via secret password.
These are load balanced using 2-choice randomized algorithm (Power-of-d-choices (Pod)) located in core/util.py (see reference 1).
The DB urls are hashed and indexed by hashed domain to speed up comparisons in the DB select statement.

## Request Format
GET requests include a URL that can be sent along as plain text; the service performs the URL encoding internally.

If you are running the service locally, serviceip:port is by default 0.0.0.0:5000


### GET urlinfo

`curl serviceip:serviceport/urlinfo/1/www.ismyurlblocked.com/tellmeplease`

Example:

`curl 0.0.0.0/urlinfo/1/https://docs.googo.com/document/u/0/1`

## Response Format

### GET urlinfo
Successful calls return a JSON response with the `exists` boolean object that indicates whether or not the URL exists in the database.

`{
    "exists": false
}`

or

`{
    "exists": true
}`


## Run the Service locally
### Through Docker

#### Docker Compose

`docker-compose build`

`docker-compose up`

#### Docker SSH

`docker build -t safe-url:latest .`

`docker run -d -p 5000:5000 safe-url`

`docker ps -a`

`docker exec -it {container_name} bash`

Tests can be run from inside the /test folder.

### Testing

`python3 test/integration.py` -- test the connection to the database and model

`python3 test/db.py` -- test the load balancer

`python3 test/unit.py` -- test the core functions

`python3 test/api.py` -- test the API calls Note: may require running `python3 test/populate.py` once.

### Test it by curling the service

`curl 0.0.0.0:5000/urlinfo/1/https://docs.googo.com/document/u/0/1`

`curl 0.0.0.0:5000/urlinfo/1/http://www.capreve.jp/2236W/biz/Smallbusiness/`

Both of these curl commands should work out of the box. If they return false, you may need to populate the DB table.

### Populate DB table

To wipe the DB, delete the safeurl.db file. If you receive unique constraint errors when running these files, it means that the DB is already populated.

`python3 test/populate.py` for a very small test set of uninteresting data

eg. `curl 0.0.0.0:5000/urlinfo/1/https://docs.googo.com/document/u/0/1`

`python3 test/populate_urlhaus.py test/urlhaus_malware_small` for a more interesting set of data

eg. `curl 0.0.0.0:5000/urlinfo/1/http://www.demicolon.com/dvrguru_revoerror/image/3930OUOELXK/com/Business/`

WARNING: The sites in the urlhaus files are real malware sites. More information at https://urlhaus.abuse.ch/

### Start the service without Docker

#### Dependencies
The latest version of Python3 is recommended.
(Depending on your installation setup, you may need to install with pip3.)
`pip install Flask`

`pip install flask-restful`

`pip install Flask-SQLAlchemy`

`pip install requests`

`pip install pytest`

#### Startup the service
`python3 service.py`


### Production
Modify the variable `is_prod` in `config.py`, set to True to connect to AWS.
Set as False for the local dev database.


## TODO

1. ~~Determine the Python frameworks to use and select a DB, integration test~~
1. ~~Hash solution for quicker selects for improvement over simple LIKE query~~
1. ~~Unit test coverage~~
2. ~~Index the database on the domain column~~
2. ~~Load balancing~~
2. ~~Unit test additions~~
2. Performance test coverage with large datasets~ in progress
2. Deployable service, possibly with API Keys
2. Dockerize with exposed port through yml config
2. Sharding improvements, eg. geographically and/or by popularity of domain

## Issues


## References

1. Richa, A. W., Mitzenmacher, M., & Sitaraman, R. (2001). The power of two random choices: A survey of techniques and results. Combinatorial Optimization, 9, 255-304.
