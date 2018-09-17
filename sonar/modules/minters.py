# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 RERO.
#
# Swiss Open Access Repository is free software; you can redistribute it
# and/or modify it under the terms of the MIT License; see LICENSE file for
# more details.

"""Persistent identifier minters."""

from __future__ import absolute_import, print_function, unicode_literals


def id_minter(record_uuid, data, provider, pid_key='pid', object_type='rec'):
    """SONAR minter."""
    if pid_key in data:
        return data[pid_key]

    provider = provider.create(
        object_type=object_type,
        object_uuid=record_uuid)
    pid = provider.pid
    data[pid_key] = int(pid.pid_value)

    return pid
