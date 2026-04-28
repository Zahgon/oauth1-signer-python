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
import json
from enum import Enum

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

import oauth1.coreutils as util


class SignatureMethod(str, Enum):
    """Signature methods supported by the API gateway."""

    RSA_SHA256 = "RSA-SHA256"
    RSA_PSS_SHA256 = "RSA-PSS"


DEFAULT_SIGNATURE_METHOD = SignatureMethod.RSA_SHA256


class OAuth:
    EMPTY_STRING = ""

    @staticmethod
    def _signature_method_type_error(signature_method) -> ValueError:
        pass

    @staticmethod
    def _validate_signature_method(signature_method: SignatureMethod):
        pass

    @staticmethod
    def get_authorization_header(uri, method, payload, consumer_key, signing_key,
                                 signature_method: SignatureMethod = DEFAULT_SIGNATURE_METHOD):
        pass

    @staticmethod
    def get_oauth_parameters(uri, method, payload, consumer_key, signing_key,
                             signature_method: SignatureMethod = DEFAULT_SIGNATURE_METHOD):
        pass

    @staticmethod
    def get_base_string(url, method, oauth_parameters):
        pass

    @staticmethod
    def sign_message(message, signing_key, signature_method: SignatureMethod = DEFAULT_SIGNATURE_METHOD):
        pass


class OAuthParameters(object):
    """
    Stores the OAuth parameters required to generate the Base String and Headers constants
    """

    OAUTH_BODY_HASH_KEY = "oauth_body_hash"
    OAUTH_CONSUMER_KEY = "oauth_consumer_key"
    OAUTH_NONCE_KEY = "oauth_nonce"
    OAUTH_KEY = "OAuth"
    AUTHORIZATION = "Authorization"
    OAUTH_SIGNATURE_KEY = "oauth_signature"
    OAUTH_SIGNATURE_METHOD_KEY = "oauth_signature_method"
    OAUTH_TIMESTAMP_KEY = "oauth_timestamp"
    OAUTH_VERSION = "oauth_version"

    def __init__(self):
        self.base_parameters = {}

    def put(self, key, value):
        pass

    def get(self, key):
        pass

    def set_oauth_consumer_key(self, consumer_key):
        pass

    def get_oauth_consumer_key(self):
        pass

    def set_oauth_nonce(self, oauth_nonce):
        pass

    def get_oauth_nonce(self):
        pass

    def set_oauth_timestamp(self, timestamp):
        pass

    def get_oauth_timestamp(self):
        pass

    def set_oauth_signature_method(self, signature_method):
        pass

    def get_oauth_signature_method(self):
        pass

    def set_oauth_signature(self, signature):
        pass

    def get_oauth_signature(self):
        pass

    def set_oauth_body_hash(self, body_hash):
        pass

    def get_oauth_body_hash(self):
        pass

    def set_oauth_version(self, version):
        pass

    def get_oauth_version(self):
        pass

    def get_base_parameters_dict(self):
        pass
