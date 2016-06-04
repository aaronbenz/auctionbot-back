# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
from flask import flash


def flash_errors(form, category='warning'):
    """Flash all errors for a form."""
    for field, errors in form.errors.items():
        for error in errors:
            flash('{0} - {1}'.format(getattr(form, field).label.text, error), category)

from flask import json
from datetime import datetime

def jsonify(dictionary):
    def default(o):
        # if o is None:
        #     return ""
        if hasattr(o, "to_dict"):
            return o.to_dict()
        elif hasattr(o, "serialize"):
            return o.serialize()
        # elif hasattr(o, "hex"):
        #     return o.hex
        # convert all datetime objects to unix on way out
        elif isinstance(o, datetime):
            return int((o - datetime.utcfromtimestamp(0)).total_seconds())
        return str(o)

    out = json.dumps(dictionary, default=default, use_decimal=True, ensure_ascii=False)
    return out