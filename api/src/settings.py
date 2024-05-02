#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu

import os
import uuid
import logging

import humanfriendly

logger = logging.getLogger(__name__)

DEFAULT_CPU = 3
DEFAULT_MEMORY = "1GiB"
DEFAULT_DISK = "1GiB"
DEFAULT_MAX_SIZE_LIMIT = 2**30 * 4
DEFAULT_MAX_TIME_LIMIT = 3600 * 2
ZIMFARM_API_URL = os.getenv(
    "INTERNAL_ZIMFARM_WEBAPI", "https://api.farm.zimit.kiwix.org/v1"
)
ZIMFARM_USERNAME = os.getenv("_ZIMFARM_USERNAME", "-")
ZIMFARM_PASSWORD = os.getenv("_ZIMFARM_PASSWORD", "-")
ZIMIT_IMAGE = os.getenv("ZIMIT_IMAGE", "openzim/zimit:1.2.0")
try:
    ZIMIT_SIZE_LIMIT = int(os.getenv("ZIMIT_SIZE_LIMIT", DEFAULT_MAX_SIZE_LIMIT))
except Exception as exc:
    logger.error(
        f"Unable to parse ZIMIT_SIZE_LIMIT: {os.getenv('ZIMIT_SIZE_LIMIT')}."
        f"Using {DEFAULT_MAX_SIZE_LIMIT}. Error: {exc}"
    )
    ZIMIT_SIZE_LIMIT = DEFAULT_MAX_SIZE_LIMIT

try:
    ZIMIT_TIME_LIMIT = int(os.getenv("ZIMIT_TIME_LIMIT", DEFAULT_MAX_TIME_LIMIT))
except Exception as exc:
    logger.error(
        f"Unable to parse ZIMIT_TIME_LIMIT: {os.getenv('ZIMIT_TIME_LIMIT')}."
        f"Using {DEFAULT_MAX_TIME_LIMIT}. Error: {exc}"
    )
    ZIMIT_TIME_LIMIT = DEFAULT_MAX_TIME_LIMIT

try:
    TASK_CPU = int(os.getenv("TASK_CPU", DEFAULT_CPU))
except Exception as exc:
    logger.error(
        f"Unable to apply custom TASK_CPU: {os.getenv('TASK_CPU')}. "
        f"Using {DEFAULT_CPU}. Error: {exc}"
    )
    TASK_CPU = DEFAULT_CPU
try:
    TASK_MEMORY = humanfriendly.parse_size(os.getenv("TASK_MEMORY", DEFAULT_MEMORY))
except Exception as exc:
    logger.error(
        f"Unable to apply custom TASK_MEMORY: {os.getenv('TASK_MEMORY')}. "
        f"Using {DEFAULT_MEMORY}. Error: {exc}"
    )
    TASK_MEMORY = humanfriendly.parse_size(DEFAULT_MEMORY)
try:
    TASK_DISK = humanfriendly.parse_size(os.getenv("TASK_DISK", DEFAULT_DISK))
except Exception as exc:
    logger.error(
        f"Unable to apply custom TASK_DISK: {os.getenv('TASK_DISK')}. "
        f"Using {DEFAULT_DISK}. Error: {exc}"
    )
    TASK_DISK = humanfriendly.parse_size(DEFAULT_DISK)
TASK_WORKER = os.getenv("TASK_WORKER")

# mailgun
MAILGUN_FROM = os.getenv("MAILGUN_FROM", "Zimit <info@zimit.kiwix.org>")
MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY", "")
MAILGUN_API_URL = os.getenv(
    "MAILGUN_API_URL", "https://api.mailgun.net/v3/mg.zimit.kiwix.org"
)
# notifications callback
PUBLIC_URL = os.getenv("PUBLIC_URL", "https://zimit.kiwix.org")
PUBLIC_API_URL = os.getenv("PUBLIC_API_URL", "https://zimit.kiwix.org/api/v1")
ZIM_DOWNLOAD_URL = os.getenv(
    "ZIM_DOWNLOAD_URL", "https://s3.us-west-1.wasabisys.com/org-kiwix-zimit/zim"
)
CALLBACK_BASE_URL = os.getenv("CALLBACK_BASE_URL", f"{PUBLIC_API_URL}/requests/hook")
HOOK_TOKEN = os.getenv("HOOK_TOKEN", uuid.uuid4().hex)
