#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `sqlalchemy_mongobi` package."""


import unittest
from unittest.mock import MagicMock

from sqlalchemy import pool

from sqlalchemy_mongobi.dialect import MongoBIDialect


class TestSqlalchemyMongoBI(unittest.TestCase):
    """Tests for `sqlalchemy_mongobi` package."""

    def setUp(self):
        self.dialect = MongoBIDialect()

    def test_pool_class(self):
        pool_class = self.dialect.get_pool_class('any://url')
        self.assertEqual(pool.NullPool, pool_class)

    def test_ignore_rollback(self):
        dbapi_connection = MagicMock()
        self.dialect.do_rollback(dbapi_connection)
        dbapi_connection.rollback.assert_not_called()

    def test_ignore_commit(self):
        dbapi_connection = MagicMock()
        self.dialect.do_rollback(dbapi_connection)
        dbapi_connection.commit.assert_not_called()
