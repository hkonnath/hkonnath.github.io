# -*- coding: utf-8 -*-

"""
Tarbell project configuration
"""

# Short project name
NAME = "harvometer"

# Descriptive title of project
TITLE = "Harv-O-Meter"

# Google spreadsheet key
SPREADSHEET_KEY = "0ApHL_D7XCTZBdFFRNVBRMmowMHh6TTVBdmJTLU1adGc"

# Exclude these files from publication
EXCLUDES = ["*.md", "requirements.txt"]

# Create JSON data at ./data.json, disabled by default
# CREATE_JSON = True

# S3 bucket configuration
#S3_BUCKETS = {
    # Provide target -> s3 url pairs, such as:
    #     "mytarget": "mys3url.bucket.url/some/path"
    # then use tarbell publish mytarget to publish to it
#}

# Default template variables
DEFAULT_CONTEXT = {
    'name': 'harvometer',
    'title': 'Harv-O-Meter'
}