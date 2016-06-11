class DependencyListener(object):
    """Class for listening to result events generated by
    DependencyDetector.  Add an instance of this class to a
    DependencyDetector instance via DependencyDetector.add_listener().
    """

    def __init__(self, options):
        self.options = options

    def set_detector(self, detector):
        self.detector = detector

    def repo(self):
        return self.detector.repo

    def new_commit(self, commit):
        pass

    def new_dependent(self, dependent):
        pass

    def new_dependency(self, dependent, dependency, path, line_num):
        pass

    def new_path(self, dependent, dependency, path, line_num):
        pass

    def new_line(self, dependent, dependency, path, line_num):
        pass

    def dependent_done(self, dependent, dependencies):
        pass

    def all_done(self):
        pass
