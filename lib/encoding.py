import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# os.environ["PYTHONIOENCODING"] = 'UTF-8'
# sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)