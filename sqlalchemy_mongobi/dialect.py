from sqlalchemy import pool
from sqlalchemy.dialects.mysql.pymysql import MySQLDialect_pymysql


class MongoBIDialect(MySQLDialect_pymysql):
    name = 'mongobi'

    @classmethod
    def get_pool_class(cls, url):
        return pool.NullPool

    def do_commit(self, dbapi_connection):
        """Execute a COMMIT."""
        return

    def do_rollback(self, dbapi_connection):
        """Execute a ROLLBACK."""
        return
