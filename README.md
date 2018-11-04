# safeurl

The safeurl project is a URL lookup service that maintains a database of blacklisted URLs accessible by an API. 
It follows RESTful principles and uses JSON as its data interchange format.

## Technical Specifications

The API is implemented in Python's Flask-RESTful framework connecting to a Flask-SQLAlchemy sqllite backend. 
Flask-RESTful removes tedious boilerplate code for specifying request and response format.
Flask-SQLAlchemy provides tidy ORM that ties in well with Flask API calls.
Both of these frameworks allow for relative ease of deployment to AWS. 
SQLALchemy provides extensions, such as a BloomFilter, that may be useful for future development.

## TODO

1. Determine the Python frameworks to use and select a DB
1. Research a hashed solution for quicker selects than simple LIKE query
1. Integration test on skeleton framework to sanity test the connections
1. Unit test coverage
2. Index the database on the domain column
2. Performance test coverage with large datasets
2. API 
2. Sharding improvements, eg. geographically and/or by popularity of domain
3. Create a deployable version and host it (note geo-sharding is not in AWS free tier)
