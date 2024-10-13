import os

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from hive_metastore import ThriftHiveMetastore

if __name__ == '__main__':
    use_kerbreos = False
    if use_kerbreos:
        # set up Kerberos environment variables
        # use kinit to init your kerbreos ticket
        os.environ['KRB5_CONFIG'] = './krb5.conf'
        os.environ['KRB5CCNAME'] = './krb5cc'

    hive_metastore_host = "localhost"
    hive_metastore_port = 9083
    socket = TSocket.TSocket(hive_metastore_host, hive_metastore_port)
    transport = TTransport.TBufferedTransport(socket)

    if use_kerbreos:
        transport = TTransport.TSaslClientTransport(transport, host=f"{hive_metastore_host}:{hive_metastore_port}", service="hive")

    protocol = TBinaryProtocol.TBinaryProtocol(trans=transport)
    client = ThriftHiveMetastore.Client(protocol)

    try:
        transport.open()
        database = client.get_all_databases()
        print("Databases:", database)
    except Thrift.TException as ex:
        print(f"Thrift exception: {ex.message}")

    finally:
        transport.close()