class Logger(object):
    def info(self, id, message):
        print "[%s] %s \033[0m" % (id, message)
