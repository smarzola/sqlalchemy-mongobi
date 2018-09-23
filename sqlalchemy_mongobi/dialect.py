from sqlalchemy import pool
from sqlalchemy.dialects.mysql.mysqldb import MySQLDialect_mysqldb
from sqlalchemy.dialects.mysql.pymysql import MySQLDialect_pymysql


class MongoBIDialectMixin:
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

    def get_isolation_level(self, connection):
        return "REPEATABLE READ"


class MongoBIDialect_mysqldb(MongoBIDialectMixin, MySQLDialect_mysqldb):
    pass


class MongoBIDialect_pymysql(MongoBIDialectMixin, MySQLDialect_pymysql):
    pass
