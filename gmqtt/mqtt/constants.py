import enum

import logging

# Message types

class MQTTCommands(enum.IntEnum):
    CONNECT = 0x10
    CONNACK = 0x20
    PUBLISH = 0x30
    PUBACK = 0x40
    PUBREC = 0x50
    PUBREL = 0x60
    PUBCOMP = 0x70
    SUBSCRIBE = 0x80
    SUBACK = 0x90
    UNSUBSCRIBE = 0xA0
    UNSUBACK = 0xB0
    PINGREQ = 0xC0
    PINGRESP = 0xD0
    DISCONNECT = 0xE0

# CONNACK codes
CONNACK_ACCEPTED = 0
CONNACK_REFUSED_PROTOCOL_VERSION = 1
CONNACK_REFUSED_IDENTIFIER_REJECTED = 2
CONNACK_REFUSED_SERVER_UNAVAILABLE = 3
CONNACK_REFUSED_BAD_USERNAME_PASSWORD = 4
CONNACK_REFUSED_NOT_AUTHORIZED = 5


# Error values
MQTT_ERR_AGAIN = -1
MQTT_ERR_SUCCESS = 0
MQTT_ERR_NOMEM = 1
MQTT_ERR_PROTOCOL = 2
MQTT_ERR_INVAL = 3
MQTT_ERR_NO_CONN = 4
MQTT_ERR_CONN_REFUSED = 5
MQTT_ERR_NOT_FOUND = 6
MQTT_ERR_CONN_LOST = 7
MQTT_ERR_TLS = 8
MQTT_ERR_PAYLOAD_SIZE = 9
MQTT_ERR_NOT_SUPPORTED = 10
MQTT_ERR_AUTH = 11
MQTT_ERR_ACL_DENIED = 12
MQTT_ERR_UNKNOWN = 13
MQTT_ERR_ERRNO = 14
MQTT_ERR_QUEUE_SIZE = 15


# MQTT protocol versions
MQTTv311 = 4
MQTTv50 = 5


class PubAckReasonCode(enum.IntEnum):
    SUCCESS = 0
    NO_MATCHING_SUBSCRIBERS = 16
    UNSPECIFIED_ERROR = 128
    IMPLEMENTATION_SPECIFIC_ERROR = 131
    NOT_AUTHORIZED = 135
    TOPIC_NAME_INVALID = 144
    PACKET_IDENTIFIER_IN_USE = 145
    QUOTA_EXCEEDED = 151
    PAYLOAD_FORMAT_INVALID = 153


class PubRecReasonCode(enum.IntEnum):
    SUCCESS = 0
    NO_MATCHING_SUBSCRIBERS = 16
    UNSPECIFIED_ERROR = 128
    IMPLEMENTATION_SPECIFIC_ERROR = 131
    NOT_AUTHORIZED = 135
    TOPIC_NAME_INVALID = 144
    PACKET_IDENTIFIER_IN_USE = 145
    QUOTA_EXCEEDED = 151
    PAYLOAD_FORMAT_INVALID = 153


class ConnAckReasonCode(enum.IntEnum):
    SUCCESS = 0
    UNSPECIFIED_ERROR = 128
    MALFORMED_PACKET = 129
    PROTOCOL_ERROR = 130
    IMPLEMENTATION_SPECIFIC_ERROR = 131
    UNSUPPORTED_PROTOCOL_VERSION = 132
    CLIENT_IDENTIFIER_NOT_VALID = 133
    BAD_USERNAME_OR_PASSWORD = 134
    NOT_AUTHORIZED = 135
    SERVER_UNAVAILABLE = 136
    SERVER_BUSY = 137
    BANNED = 138
    BAD_AUTHENTICATION_METHOD = 140
    TOPIC_NAME_INVALID = 144
    PACKET_TOO_LARGE = 149
    PAYLOAD_FORMAT_INVALID = 153
    RETAIN_NOT_SUPPORTED = 154
    QOS_NOT_SUPPORTED = 155
    USE_ANOTHER_SERVER = 156
    SERVER_MOVED = 157
    CONNECTION_RATE_EXCEEDED = 159


class SubAckReasonCode(enum.IntEnum):
    QOS0 = 0
    QOS1 = 1
    QOS2 = 2

    UNSPECIFIED_ERROR = 128
    IMPLEMENTATION_SPECIFIC_ERROR = 131
    NOT_AUTHORIZED = 135
    TOPIC_FILTER_INVALID = 143
    PACKET_IDENTIFIER_IN_USE = 145
    QUOTA_EXCEEDED = 151
    SHARED_SUBSCRIPTIONS_NOT_SUPPORTED = 158
    SUBSCRIPTION_IDENTIFIERS_NOT_SUPPORTED = 161
    WILDCARD_SUBSCRIPTIONS_NOT_SUPPORTED = 162

class DisconnectReasonCode(enum.IntEnum):
    NORMAL_DISCONNECTION = 0
    DISCONNECT_WITH_WILL_MESSAGE = 4

    UNSPECIFIED_ERROR = 128
    MALFORMED_PACKET = 129
    PROTOCOL_ERROR = 130
    IMPLEMENTATION_SPECIFIC_ERROR = 131
    NOT_AUTHORIZED = 135
    SERVER_BUSY = 137
    SERVER_SHUTTING_DOWN = 139
    KEEP_ALIVE_TIMEOUT = 141
    SESSION_TAKEN_OVER = 142
    TOPIC_FILTER_INVALID = 144
    RECEIVE_MAXIMUM_EXCEEDED = 147
    TOPIC_ALIAS_INVALID = 148
    PACKET_TOO_LARGE = 149
    MESSAGE_RATE_TOO_HIGH = 150
    QUOTA_EXCEEDED = 151
    ADMINISTRATIVE_ACION = 152
    PAYLOAD_FORMAT_INVALID = 153
    RETAIN_NOT_SUPPORTED = 154
    QOS_NOT_SUPPORTED = 155
    USE_ANOTHER_SERVER = 156
    SERVER_MOVED = 157
    SHARED_SUBSCRIPTIONS_NOT_SUPPORTED = 158
    CONNECTION_RATE_EXCEEDED = 159
    MAXIMUM_CONNECT_TIME = 160
    SUBSCRIPTION_IDENTIFIERS_NOT_SUPPORTED = 161
    WILDCARD_SUBSCRIPTIONS_NOT_SUPPORTED = 162

UNLIMITED_RECONNECTS = -1

DEFAULT_CONFIG = {
    'reconnect_delay': 6,
    'reconnect_retries': UNLIMITED_RECONNECTS,
}
