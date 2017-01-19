import multiprocessing

def son(conn):

    conn.send(([1],{'name':123},[111,222]))
    conn.send(([1],{'name':123},[111,222]))

    print(('S_id',id(conn)))
    print(conn.recv())
    print(conn.recv())
    conn.close()
if __name__ == '__main__':
    p_conn,s_conn = multiprocessing.Pipe()

    p = multiprocessing.Process(target=son,args=(s_conn,))
    print('p_id',id(p_conn),'son_id',id(s_conn))
    p.start()

    print(p_conn.recv())
    print(p_conn.recv())
    p_conn.send('son,test')
    p_conn.send(11)
    p.join()