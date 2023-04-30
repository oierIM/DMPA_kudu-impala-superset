import os

# Your App secret key
SECRET_KEY = '+qaVsPUErjRfpxobQXS+Fnw83ZwsG4XtZhtlfV4VqctSXmkhF+UfJfDK'

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# superset metadata (slices, connections, tables, dashboards, ...).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI
# SQLALCHEMY_DATABASE_URI = 'sqlite:////var/lib/superset/superset.db'
#SQLALCHEMY_DATABASE_URI = 'impala://kudu-impala:21050'
SQLALCHEMY_DATABASE_URI = 'impala://kudu-impala:21050'
# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = True
# Add endpoints that need to be exempt from CSRF protection
WTF_CSRF_EXEMPT_LIST = []

# Set this API key to enable Mapbox visualizations
MAPBOX_API_KEY = os.environ.get("MAPBOX_API_KEY", "")
