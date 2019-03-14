# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase

print('hello 1')
class TestCourse(TransactionCase):
    print('hello 2')

    def test_action(self):
        record = self.env['openacademy.course'].search([('name', '=', 'Dragon Technical Training')])
        record.update({
            'description': 'Test1'
        })
        self.assertEqual(
            record.description, 'Test1')
