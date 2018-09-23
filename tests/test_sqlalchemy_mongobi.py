#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `sqlalchemy_mongobi` package."""


import unittest
from unittest.mock import MagicMock

from sqlalchemy import pool

from sqlalchemy_mongobi.dialect import MongoBIDialect_mysqldb
from sqlalchemy_mongobi.dialect import MongoBIDialect_pymysql


class TestSqlalchemyMongoBI(unittest.TestCase):
    """Tests for `sqlalchemy_mongobi` package."""

    def setUp(self):
        self.dialects = (MongoBIDialect_mysqldb(), MongoBIDialect_pymysql())

    def test_pool_class(self):
        for dialect in self.dialects:
            pool_class = dialect.get_pool_class('any://url')
            self.assertEqual(pool.NullPool, pool_class)

    def test_ignore_rollback(self):
        for dialect in self.dialects:
            dbapi_connection = MagicMock()
            dialect.do_rollback(dbapi_connection)
            dbapi_connection.rollback.assert_not_called()

    def test_ignore_commit(self):
        for dialect in self.dialects:
            dbapi_connection = MagicMock()
            dialect.do_commit(dbapi_connection)
            dbapi_connection.commit.assert_not_called()

    def test_get_isolation_level(self):
        for dialect in self.dialects:
            isolation_level = dialect.get_isolation_level(MagicMock())
            self.assertEqual("REPEATABLE READ", isolation_level)
