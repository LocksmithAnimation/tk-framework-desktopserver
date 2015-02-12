# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import datetime

class Message():
    """
    Message Format
    {
        protocol_version: Number
        id: Number
        timestamp: Date

        [Optional]
        command:
            name: String (ShotgunAPI method)
            data: Any object

        [Optional]
        error: Boolean
        error_message: String
        error_data: Any object

        [Optional]
        reply: Any Object
    }
    """

    def __init__(self, id, protocol_version):
        """
        Message Constructor
        :param id: Number Message id
        """

        self.data = {}
        self.data["id"] = id
        self.data["timestamp"] = datetime.datetime.now()
        self.data["protocol_version"] = protocol_version

    def reply(self, data):
        """
        Set reply data for this message
        :param data: Dictionary Additional data to be sent back in reply
        """
        self.data["reply"] = data

    def error(self, error_message, error_data):
        self.data["error"] = True
        self.data["error_message"] = error_message
        if error_data: self.data["error_data"] = error_data
