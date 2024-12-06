import pickle


class Utils(object):
    def __init__(self):
        pass

    @staticmethod
    def save_var(v, filename):
        f = open(filename, 'wb')
        pickle.dump(v, f)
        f.close()
        return filename

    @staticmethod
    def load_var(filename):
        try:
            f = open(filename, 'ab+')
            r = pickle.load(f)
            f.close()
            return r
        except EOFError:
            return ""
