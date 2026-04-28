# -*- coding: utf-8 -*-
#
# Copyright 2019-2021 Mastercard
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are
# permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this list of
# conditions and the following disclaimer.
# Redistributions in binary form must reproduce the above copyright notice, this list of
# conditions and the following disclaimer in the documentation and/or other materials
# provided with the distribution.
# Neither the name of the MasterCard International Incorporated nor the names of its
# contributors may be used to endorse or promote products derived from this software
# without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT
# SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
# TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
#
"""
Utility file having common functions
"""
import base64
import hashlib
import time
import urllib
from random import SystemRandom
from urllib.parse import urlparse, parse_qsl


def normalize_params(url, params):
    """
    Combines the query parameters of url and extra params into a single queryString.
    All the query string parameters are lexicographically sorted
    """
    pass


def encode_pair(must_encode, key, value):
    pass


def normalize_url(url):
    """
    Removes the query parameters from the URL
    """
    pass


def sha256_encode(text):
    """
    Returns the digest of SHA-256 of the text
    """
    pass


def base64_encode(text):
    """
    Base64 encodes the given input
    """
    pass


def percent_encode(text):
    """
    Percent encodes a string as per https://tools.ietf.org/html/rfc3986
    """
    pass


def get_nonce(length=16):
    """
    Returns a random string of length=@length
    """
    pass


def get_timestamp():
    """
    Returns the UTC timestamp (seconds passed since epoch)
    """
    pass
