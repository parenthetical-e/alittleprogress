import sys


class Bar(object):
    def __init__(self, n):
        """A little (simple) progress bar.
        
        Parameters
        ---------
        n : int
            The number of total number of interations expected.
        """

        self.width = 50
        if n < self.width:
            self.width = n

        self.n = int(n)
        self.increment = int(self.n / self.width)

        # setup progress bar
        sys.stdout.write("[{0}]\n".format(" " * self.width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (self.width + 1))
        ## return to start of line, after '['

    def update(self, i):
        """Update the progress bar for this iteration?"""
        if (i % self.increment) == 0:
            sys.stdout.write("-")
            sys.stdout.flush()

    def end(self):
        sys.stdout.write("\n")
