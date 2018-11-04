# safeurl

The safeurl project is a URL lookup service that maintains a database of blacklisted URLs accessible by an API.
It follows RESTful principles and uses JSON as its data interchange format.

## Request Format
GET requests include a URL that can be sent along as plain text; the service performs the URL encoding internally.

If you are running the service locally, serviceip:port is by default 127.0.0.1:5000


### GET urlinfo

`curl serviceip:serviceport/urlinfo/www.ismyurlblocked.com/tellmeplease`


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
### Dependencies
The latest version of Python3 is recommended.

`pip install Flask`

`pip install flask-restful`

`pip install Flask-SQLAlchemy`

### Populate DB table
`python3 test/populate.py`

### Startup
`python3 service.py`


## Technical Specifications

The API is implemented in Python's Flask-RESTful framework connecting to a Flask-SQLAlchemy sqllite backend.
Flask-RESTful removes tedious boilerplate code for specifying request and response format.
Flask-SQLAlchemy provides tidy ORM that ties in well with Flask API calls.
Both of these frameworks allow for relative ease of deployment to AWS.
SQLALchemy provides extensions, such as a BloomFilter, that may be useful for future development.

## TODO

1. ~~Determine the Python frameworks to use and select a DB, integration test~~
1. ~~Hash solution for quicker selects for improvement over simple LIKE query~~
1. ~~Unit test coverage~~
2. Index the database on the domain column
2. Performance test coverage with large datasets
2. API Key? Additional requests parameters?
2. Sharding improvements, eg. geographically and/or by popularity of domain
3. Create a deployable version and host it (note geo-sharding is not in AWS free tier)

## Issues

1. Old DB instance was corrupted - workaround is to create a new one. I will take a deeper look at this during performance testing.
2. Double check the GET API call format as per the specs -- this may not fit into the restful API design (oops!).
