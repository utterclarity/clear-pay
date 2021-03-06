def worker(n):
    print "[{0}] hi".format(n)
    while True:  # not jobs.empty():
        if jobs.empty():
            gevent.sleep(1)
            continue
        job = jobs.get()
        print "[{0}] got {1}".format(n, job)
        gevent.sleep(0)
    print "[{0}] done".format(n)


def boss():
    for i in xrange(0, 25):
        jobs.put_nowait([i, "hello"])

t = threading.Thread(target=worker, args=(1,))
t.daemon = True
t.start()

#gevent.spawn(boss).join()
#gevent.joinall([
#    gevent.spawn(worker, "a"),
#    gevent.spawn(worker, "b"),
#    gevent.spawn(worker, "c")
#])


@app.route("/")
def index():
    return "Hnnnng!"


@app.route("/put/<int:many>")
@app.route("/put")
def put(many=1):
    jqs = jobs.qsize()
    [jobs.put([i, "foo"]) for i in xrange(many)]
    print "wat:", jqs, jobs.qsize()
    return "ok: {0}/{1}".format(jqs, jobs.qsize())


@app.route("/spawn/<int:many>")
@app.route("/spawn")
def spawn(many=1):
    gevent.joinall([gevent.spawn(worker, i) for i in xrange(many)])
    return "ok!"


@app.route("/get")
def get():
    return "{0}! :O".format(jobs.qsize())