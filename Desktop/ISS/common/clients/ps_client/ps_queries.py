GET_USER_BY_ID = """
    SELECT
        id,
        name,
        access_key
    FROM users
    WHERE id=%d;
"""

GET_USER_BY_ACCESS_KEY = """
    SELECT
        id,
        name,
        access_key
    FROM users
    WHERE access_key='%s'
"""
