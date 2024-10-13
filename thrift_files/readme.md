#### thrift files
hive_metastore.thrift from https://github.com/apache/hive/blob/rel/release-3.1.3/standalone-metastore/src/main/thrift/hive_metastore.thrift
share/fb303/if/fb303.thrift from https://github.com/apache/thrift/blob/master/contrib/fb303/if/fb303.thrift

#### how does hive_metastore directory comes from
thrift --gen py hive_metastore.thrift

#### how does fb303 directory comes from
1. thrift --gen py share/fb303/if/fb303.thrift

2. copy [FacebookBase.py](https://github.com/apache/thrift/blob/master/contrib/fb303/py/fb303/FacebookBase.py) 
3. copy [fb303_simple_mgmt.py](https://github.com/apache/thrift/blob/master/contrib/fb303/py/fb303_scripts/fb303_simple_mgmt.py)
4. edit init.py add FacebookBase.py and fb303_simple_mgmt.py

ref: 
https://github.com/apache/thrift/tree/master/contrib/fb303
https://packages.fedoraproject.org/pkgs/thrift/python-fb303/epel-7.html