==================
sqlalchemy-mongobi
==================


MongoDB connector for BI SQLAlchemy dialect.


.. image:: https://img.shields.io/pypi/v/sqlalchemy_mongobi.svg
        :target: https://pypi.python.org/pypi/sqlalchemy_mongobi

.. image:: https://img.shields.io/travis/smarzola/sqlalchemy-mongobi.svg
        :target: https://travis-ci.org/smarzola/sqlalchemy-mongobi


MongoDB connector for BI does not have support for transactions but SQLAlchemy DBAPI
layer uses ROLLBACKs after the connection initialization even if the connection pool is
configured with `reset_on_return=False`. This dialect ignores COMMITs and ROLLBACKs, and
uses the `NullPool` connection pool (which means no pooling, opens and closes the underlying
DB-API connection per each connection open/close).


Usage
-----
The DSN format is similar to that of mysql::

    engine = create_engine(
        "mongobi://user?source=auth_db:password@url:port/database",
        connect_args={
            "ssl": {
                "mode": "PREFERRED"
            }
        },
        pool_reset_on_return=False,
    )


DBAPI Support
-------------
The following DBAPI options are available:

* mysqlclient::

    mongobi+mysqldb://user?source=auth_db:password@url:port/database


* PyMySQL::

    mongobi+pymysql://user?source=auth_db:password@url:port/database

