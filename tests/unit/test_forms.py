
import unittest
from unittest.case import TestCase
from urllib import response

from flask import (
    render_template,
    redirect, request,
    flash, session,
    jsonify, current_app
)

from utils.forms import (
    LoginForm, SignUpForm,
    AddNoteForm, AddTagForm,
    ChangeEmailForm, ChangePasswordForm
)

class Test_LoginForm(TestCase):
    def tetestSystem(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
