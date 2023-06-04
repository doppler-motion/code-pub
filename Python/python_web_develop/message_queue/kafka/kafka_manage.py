import time

from loguru import logger
from kafka import KafkaProducer, KafkaAdminClient
from kafka.admin.new_topic import NewTopic

KAFKA_BOOTSTRAP_SERVERS = ""
SASL_PLAIN_USERNAME = ""
SASL_PLAIN_PASSWORD = ""
SSL_CAFILE = ""
SSL_CERTFILE = ""
SSL_KEYFILE = ""


def get_current_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def kafka_str_to_list(the_str):
    servers = str(the_str).replace('[', '').replace(']', '').replace('"', '').replace("'", '').split(',')
    return servers


def manage_kafka():
    """
    检查kafka topic，没有就创建
    :return:
    """
    partition_nums = 3
    topic = "test_topic"
    try:
        # 创建kafka管理端
        kafka_admin_client = KafkaAdminClient(
            bootstrap_servers=kafka_str_to_list(KAFKA_BOOTSTRAP_SERVERS),
            sasl_mechanism="PLAIN",
            security_protocol='SASL_SSL',
            sasl_plain_username=SASL_PLAIN_USERNAME,
            sasl_plain_password=SASL_PLAIN_PASSWORD,
            ssl_check_hostname=False,
            ssl_cafile=SSL_CAFILE,
            ssl_certfile=SSL_CERTFILE,
            ssl_keyfile=SSL_KEYFILE,
        )

        # 列出所有的topic
        topic_exist = kafka_admin_client.list_topics()

        # 创建topic
        kafka_admin_client.create_topics([NewTopic(name=topic,
                                                   num_partitions=partition_nums,
                                                   replication_factor=3)])

    except:
        logger.exception(f"manage kafka go wrong, at {get_current_time()}")
