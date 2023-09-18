from kazoo.client import KazooClient
from kazoo.client import KazooState

def my_func(event):
    # check to see what the children are now
    print("event: ", event)
    zk.get_children(event.path, watch=my_func)
    data, stat = zk.get(path=event.path, watch=my_func)
    print(data.decode())

zk = KazooClient(hosts='localhost:2181')  # Ganti dengan alamat ZooKeeper Anda
zk.start()

# Path ke node yang akan dimonitor
node_path = '/sample'

# Membuat node jika tidak ada
if not zk.exists(node_path):
    zk.create(node_path, b'Initial Data')

zk.get_children(path=node_path, watch=my_func)
data, stat = zk.get(path=node_path, watch=my_func)
print(f"Data at {node_path}: {data.decode()}")
zk.get_children(path='/', watch=my_func)

try:
    while True:
        pass
except KeyboardInterrupt:
    pass
finally:
    zk.stop()
# if __name__ == "__main__":
#     main()

zk.stop()